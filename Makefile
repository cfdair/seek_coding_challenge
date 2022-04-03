ifneq (,$(wildcard ./.envrc))
    include .envrc
    export
endif

.envrc:
	@bash bin/setup_envrc.bash \
		&& echo "Exiting here to allow these envvars to be loaded in the next step." \
		&& exit 1

download: .envrc
	@bash bin/download_dataset.bash

build_docker:
	@docker build . --build-arg UID=$$(id -u) --tag seek_coding_challenge

build_docker_dev:
	@docker build . --build-arg UID=$$(id -u) --build-arg POETRY_DEV_OPTION= --tag seek_coding_challenge_dev

run: build_docker
	@docker run -it -v $$(pwd):/opt/app/ seek_coding_challenge

test: build_docker_dev
	@docker run -it seek_coding_challenge_dev pytest

clean:
	@rm -rf data/
	@rm .envrc
