include ../../ci/make/tf.Makefile

help:
	@echo "Help..."

test:
	- (poetry shell && poetry install && poetry run pytest)