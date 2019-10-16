SHELL            = bash
PYTHON           = python3
PIPENV           = pipenv

VENV             = .venv


.PHONY: usage
usage:
	@echo "Usage: ${MAKE} TARGET"
	@echo ""
	@echo "Targets:"
	@echo "  init           init for develop"
	@echo "  lint           run flake8"
	@echo "  format         run some formatter"
	@echo "  clean          clean current directory"

.PHONY: init
init:
	${PIPENV} sync

.PHONY: lint
lint:
	${PIPENV} run flake8 qiitacli

.PHONY: format
format:
	${PIPENV} run autoflake -ir \
	    --remove-all-unused-imports \
	    --ignore-init-module-imports \
	    --remove-unused-variables \
	    qiitacli
	${PIPENV} run isort -rc qiitacli
	${PIPENV} run autopep8 -ir qiitacli

.PHONY: clean
clean:
	${PIPENV} --rm
