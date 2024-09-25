build:
	rm -rf build/ dist/
	python -m build --sdist --wheel --outdir dist/ .
	rm -rf build/

clean:
	rm -rf build/ dist/ *.egg-info/
