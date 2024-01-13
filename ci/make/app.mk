# include tf.mk

test:
	- (poetry shell && poetry install && poetry run pytest)