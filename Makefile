TARGET ?= target
NAME = pbs-builder-model
ENV_NAME = pbs-research-build
INVOKER ?= podman run --rm -v $$(pwd):/git:Z -w /git/tex --network none $(ENV_NAME)

env: env.json

env.json: Containerfile
	podman build -t $(ENV_NAME) . && podman image inspect $(ENV_NAME) > env.json

update-env:
	podman build -t $(ENV_NAME) . && podman image inspect $(ENV_NAME) > env.json

clean-env:
	podman rmi $(ENV_NAME)