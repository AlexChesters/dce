install:
	poetry install

run:
	cd ../../modules && \
	api_url=$$(terraform output -raw api_url) && \
	cd ../tools/apitest/ && \
	AWS_PROFILE=dce-master poetry run python api_test.py --api-url $${api_url}
