# Makefile for paulowoody/chinook-pydantic-repository on cloudsmith
-include .env
export

.DEFAULT_GOAL := help

DIST_DIR        := dist
CLOUDSMITH_ORG  := paulowoody
CLOUDSMITH_REPO := chinook-pydantic-repository
CLOUDSMITH_URL  := https://python.cloudsmith.io/$(CLOUDSMITH_ORG)/$(CLOUDSMITH_REPO)/

.PHONY: clean build sign publish release help

help:
	@echo "Targets:"
	@echo "  build   - build the distribution"
	@echo "  sign    - build and sign artefacts"
	@echo "  publish - build, sign, and publish to Cloudsmith"
	@echo "  release - full pipeline including sigstore bundles"
	@echo "  clean   - remove dist/"

clean:
	rm -rf $(DIST_DIR)

build: clean
	uv build

sign: build
	sigstore sign $(DIST_DIR)/*.whl $(DIST_DIR)/*.tar.gz

publish: sign
	@test -n "$${UV_PUBLISH_TOKEN}" || (echo "UV_PUBLISH_TOKEN not set — source .env?"; exit 1)
	uv publish --index cloudsmith \
	--check-url https://dl.cloudsmith.io/public/paulowoody/chinook-pydantic-repository/python/simple/

release: publish
	for file in $(DIST_DIR)/*.sigstore.json; do \
		cloudsmith push raw $(CLOUDSMITH_ORG)/$(CLOUDSMITH_REPO) $$file -k $(CLOUDSMITH_API_KEY) --republish; \
	done

