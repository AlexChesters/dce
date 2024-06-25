install:
	poetry install

run:
	cd ../../modules && \
	api_url=$$(terraform output -raw api_url) && \
	cd ../tools/dce-api/ && \
	AWS_PROFILE=dce-master poetry run python -m api.main --api-url $${api_url}
