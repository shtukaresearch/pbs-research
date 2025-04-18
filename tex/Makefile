TARGET ?= $$(pwd)/target
NAME = pbs-builder-model
ENV_NAME = pbs-research-build
INVOKER ?= podman run --rm -v $$(pwd):/tex:Z -v $(TARGET):/tex/target:Z -w /tex --network none $(ENV_NAME)

all: $(TARGET)/$(NAME).pdf

$(TARGET):
	mkdir -p $@

$(TARGET)/$(NAME).pdf: $(NAME).tex document.tex common/macro.tex $(TARGET)/$(NAME).bbl | $(TARGET)
	$(INVOKER) lualatex -synctex=1 -interaction=batchmode -output-directory=target $(NAME)

$(TARGET)/$(NAME).bbl: $(TARGET)/$(NAME).bcf bib/$(NAME).bib | $(TARGET)
	$(INVOKER) biber target/$(NAME) --quiet

$(TARGET)/$(NAME).bcf: $(NAME).tex | $(TARGET)
	$(INVOKER) lualatex -synctex=1 -interaction=batchmode -output-directory=target $(NAME)

build-once: | $(TARGET)
	$(INVOKER) lualatex -synctex=1 -interaction=batchmode -output-directory=target $(NAME)

debug: | $(TARGET)
	$(INVOKER) lualatex -synctex=1 -output-directory=target $(NAME)

clean: | $(TARGET)
	rm $(TARGET)/*

shell:
	podman run -ti --network none --rm -v $$(pwd):/tex:Z -w /tex $(ENV_NAME)
