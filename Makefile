# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = content
BUILDDIR      = build

DOCKMAN = $(shell command -v podman || command -v docker || echo "docker")

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

build/html.tar: html
	tar cf build/html.tar -C build/html .

docker-html: build/docker-html.tar

.PHONY: docker-html

build/docker-html.tar:
	mkdir -p build
	${DOCKMAN} build --target artifact -t blog-v3:artifact .
	${DOCKMAN} create --replace --name blog-v3-artifact blog-v3:artifact /bin/true
	${DOCKMAN} cp blog-v3-artifact:/html.tar build/docker-html.tar
	${DOCKMAN} rm blog-v3-artifact
	@echo "Docker HTML artifact created at build/docker-html.tar"


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
