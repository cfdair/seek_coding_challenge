ifneq (,$(wildcard ./.envrc))
    include .envrc
    export
endif

.envrc:
	@bash bin/setup_envrc.bash \
		&& echo "Exiting here to allow these envvars to be loaded in the next step." \
		&& exit 1

clean:
	@rm .envrc