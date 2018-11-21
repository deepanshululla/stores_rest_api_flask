
TEST_PATH = ./tests
VENV_PATH = ../venv
CODE_PATH = .

.DEFAULT: help
help:
	@echo "make test"
	@echo "       run tests"
	@echo "make run"
	@echo "       run project"
	@echo "make clean"
	@echo "       clean project"
	@echo "make install"
	@echo "       install project dependencies"
	@echo "make lint"
	@echo "       lint project"

clean:
	find . -name '*.pyc' -exec rm {} \;
	find . -name '*.pytest_cache' -exec rm -rf {} \;

isvirtualenv: clean;
	@if [ -z "$(VIRTUAL_ENV)" ]; then echo "ERROR: Not in a virtualenv." 1>&2; exit 1; fi

run: isvirtualenv; \
	python $(CODE_PATH)/app.py; \

test: isvirtualenv; \
	$(VENV_PATH)/bin/py.test --verbose --color=yes $(TEST_PATH); \
	# python -m unittest discover -s $(TEST_PATH) -t $(TEST_PATH) -v

lint: isvirtualenv; \
	find $(CODE_PATH) -name "*.py" -depth -exec $(VENV_PATH)/bin/autopep8 --in-place --aggressive '{}' \;

install: isvirtualenv; \
	$(VENV_PATH)/bin/pip install -r requirements.txt; \
