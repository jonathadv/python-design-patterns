.SILENT: test

# Run tests with pytest
test:
	python3 -m unittest -v

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

