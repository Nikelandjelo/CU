INVENV = $(shell pip3 -V | grep 'harbour_venv')
current_dir = $(shell pwd)

prereqs: venvcheck FORCE
	pip install -r requirements.txt

venv: FORCE
	python3 -m venv harbour_venv

docs:
	pdoc  --html ./src/*.py --force

venvcheck:
ifeq ($(INVENV),)
	$(error You should only run this from within the venv. Use '. ./harbour_venv/bin/activate')
else
	@echo "venv check passed\n"
endif


start_target:
	-docker kill harbourmaster_target
	-docker rm harbourmaster_target
	docker run -t --name harbourmaster_target csx239/harbourmaster_target:latest




FORCE:
