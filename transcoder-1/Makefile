INVENV = $(shell pip3 -V | grep 'venv')
current_dir = $(shell pwd)

prereqs: venvcheck FORCE
	pip install -r requirements.txt

venv: FORCE
	python3 -m venv venv

docs:
	pdoc  --html ./src/transcoder.py --force

venvcheck:
ifeq ($(INVENV),)
	$(error You should only run this from within the venv. Use '. ./venv/bin/activate')
else
	@echo "venv check passed\n"
endif


test: FORCE venvcheck
	py.test -v  tests/ 


FORCE:
