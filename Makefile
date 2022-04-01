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
	@docker build . --tag seek_coding_challenge

run: build_docker
	@docker run -it -v $$(pwd):/opt/app/ seek_coding_challenge

clean:
	@rm -rf data/
	@rm .envrc
