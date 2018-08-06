PYTHON=python3

.DEFAULT: help
help:
	@echo "make init"
	@echo "       install all requirements"
	@echo "make run"
	@echo "       run project"

setup:
	${PYTHON} -m pip install -r requirements.txt 
		
run:
	${PYTHON} employees/__init__.py