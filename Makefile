# Run all tests.
.PHONY: test
test: test-flake8 test-unit

# Enforce style guide.
.PHONY: test-flake8
test-flake8:
	flake8 .

# Run unit tests.
.PHONY: test-unit
test-unit:
	py.test
