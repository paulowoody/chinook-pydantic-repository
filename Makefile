# Makefile for paulowoody/chinook-pydantic-repository on cloudsmith
-include .env
export

.DEFAULT_GOAL := help

DIST_DIR        := dist
CLOUDSMITH_ORG  := paulowoody
CLOUDSMITH_REPO := chinook-pydantic-repository
CLOUDSMITH_URL  := https://python.cloudsmith.io/$(CLOUDSMITH_ORG)/$(CLOUDSMITH_REPO)/

.PHONY: clean build sign publish release audit sbom fixdeps verify help

help:
	@echo "Targets:"
	@echo "  build   - build the distribution"
	@echo "  audit   - audit the distribution"
	@echo "  sbom    - generate SBOM"
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

sbom:
	@echo "Generating Software Bill of Materials (SBOM) with licenses..."
	@mkdir -p $(DIST_DIR)
	uvx --from cyclonedx-bom cyclonedx-py environment \
		--output-format JSON \
		--gather-license-texts \
		--output-file $(DIST_DIR)/sbom.json

clean:
	rm -rf $(DIST_DIR)

build: clean audit sbom
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
	cloudsmith push raw $(CLOUDSMITH_ORG)/$(CLOUDSMITH_REPO) $(DIST_DIR)/sbom.json -k $(CLOUDSMITH_API_KEY) --republish
	for file in $(DIST_DIR)/*.sigstore.json; do \
		cloudsmith push raw $(CLOUDSMITH_ORG)/$(CLOUDSMITH_REPO) $$file -k $(CLOUDSMITH_API_KEY) --republish; \
	done

