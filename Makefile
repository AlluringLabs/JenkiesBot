all: test-watch

test:
	nose2

test-watch:
	filewatcher '**/*.py' 'nose2'
