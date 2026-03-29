# Makefile for paulowoody/chinook-pydantic-repository on cloudsmith
-include .env
export

.DEFAULT_GOAL := help

DIST_DIR        := dist
CLOUDSMITH_ORG  := paulowoody
CLOUDSMITH_REPO := chinook-pydantic-repository
CLOUDSMITH_URL  := https://python.cloudsmith.io/$(CLOUDSMITH_ORG)/$(CLOUDSMITH_REPO)/

.PHONY: clean build sign publish release audit fixdeps verify help

help:
	@echo "Targets:"
	@echo "  build   - build the distribution"
	@echo "  audit   - audit the distribution"
	@echo "  fixdeps - safely update dependencies"
	@echo "  sign    - build and sign artefacts"
	@echo "  publish - build, sign, and publish to Cloudsmith"
	@echo "  release - full pipeline including sigstore bundles"
	@echo "  clean   - remove dist/"

fixdeps:
	@echo "Attempting to update dependencies to patched versions..."
	uv lock --upgrade

audit: fixdeps
	@echo "Scanning for vulnerabilities..."
	uv pip freeze | uv run pip-audit $$(test -f audit-ignore.txt && awk '{print "--ignore-vuln " $$1}' pip-audit-ignore.txt)

clean:
	rm -rf $(DIST_DIR)

build: clean audit
	uv build

sign: build
	sigstore sign $(DIST_DIR)/*.whl $(DIST_DIR)/*.tar.gz

verify: audit
	uv run pytest tests/

publish: verify sign
	@test -n "$${UV_PUBLISH_TOKEN}" || (echo "UV_PUBLISH_TOKEN not set — source .env?"; exit 1)
	uv publish --index cloudsmith \
	--check-url https://dl.cloudsmith.io/public/paulowoody/chinook-pydantic-repository/python/simple/

release: publish 
	for file in $(DIST_DIR)/*.sigstore.json; do \
		cloudsmith push raw $(CLOUDSMITH_ORG)/$(CLOUDSMITH_REPO) $$file -k $(CLOUDSMITH_API_KEY) --republish; \
	done

# e.g. Check if a newer version of Pygments exists than 2.19.2
check-fix:
	@echo "Checking PyPI for Pygments updates..."
	@uv pip list --outdated | grep "pygments" || echo "No updates found for Pygments yet."

