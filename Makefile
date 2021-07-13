MODULE_NAME = patterns
TEST_DIR =
IN_VENV = pipenv run

.SILENT: test

default: help

# Run tests with pytest
test:
	python3 -m unittest -v

# Format with black
format:
	$(IN_VENV) black $(MODULE_NAME) $(TEST_DIR)

# Generate documentation
doc_html:
	$(IN_VENV) $(MAKE) -C docs html


# Display this help
help:
	@ echo
	@ echo '  Usage:'
	@ echo ''
	@ echo '	make <target> [flags...]'
	@ echo ''
	@ echo '  Targets:'
	@ echo ''
	@ awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?:/{ print "   ", $$1, comment }' ./Makefile | column -t -s ':' | sort
	@ echo ''
	@ echo '  Flags:'
	@ echo ''
	@ awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?\?=/{ print "   ", $$1, $$2, comment }' ./Makefile | column -t -s '?=' | sort
	@ echo ''

