install:
	python setup.py install
uninstall:
	pip uninstall rfkill_manager
clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
