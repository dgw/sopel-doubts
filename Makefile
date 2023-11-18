build:
	rm -rf build/ dist/
	python -m build --sdist --wheel --outdir dist/ .
	rm -rf build/

upload:
	python -m twine upload -r asak dist/*
	rm -rf build/ dist/ *.egg-info/

clean:
	rm -rf build/ dist/ *.egg-info/
