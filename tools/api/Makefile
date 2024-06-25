install:
	poetry install

run:
	cd ../../modules && \
	api_url=$$(terraform output -raw api_url) && \
	cd ../tools/api/ && \
	AWS_PROFILE=dce-master poetry run python api.py --api-url $${api_url}
