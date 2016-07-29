all: test

test:
	filewatcher '**/*.py' 'nose2'
