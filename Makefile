
ORIGDIR=corpora
FLIPDIR=corpora_by_format
INNER_READMES=inner_READMEs

all: clean create_dirs flip_dirs

flip_dirs:
	@rm -rf $(FLIPDIR)
	@echo
	@echo "Flipping '$(ORIGDIR)' to '$(FLIPDIR)'"
	@echo "using README.md files from '$(ORIGDIR)/$(INNER_READMES)'."
	@echo
	python3 flipdirs.py --origdir $(ORIGDIR) --flipdir $(FLIPDIR) --inner_READMEs $(INNER_READMES)
	@echo

create_dirs:
	@rm -rf $(ORIGDIR)
	@echo
	@echo "Creating '$(ORIGDIR)'."
#
	@mkdir -p $(ORIGDIR)/corpus1/raw
	@echo "This is corpus1 in raw format." > $(ORIGDIR)/corpus1/raw/corpus1.raw
	@mkdir -p $(ORIGDIR)/corpus1/spl
	@echo "This is corpus1 in spl format." > $(ORIGDIR)/corpus1/spl/corpus1.spl
	@mkdir -p $(ORIGDIR)/corpus1/noske
	@echo "This is corpus1 in noske format." > $(ORIGDIR)/corpus1/noske/corpus1.noske
	@echo "Some info on corpus1." > $(ORIGDIR)/corpus1/README.md
#
	@mkdir -p $(ORIGDIR)/corpus2/raw
	@echo "This is corpus2 in raw format." > $(ORIGDIR)/corpus2/raw/corpus2.raw
	@mkdir -p $(ORIGDIR)/corpus2/spl
	@echo "Some info on corpus2." > $(ORIGDIR)/corpus2/README.md
#
	@mkdir -p $(ORIGDIR)/corpus3/raw
	@echo "Some info on corpus3." > $(ORIGDIR)/corpus3/README.md
#
	@mkdir -p $(ORIGDIR)/inner_READMEs
	@echo "Some info on raw format." > $(ORIGDIR)/inner_READMEs/README.raw.md
	@echo "Some info on spl format." > $(ORIGDIR)/inner_READMEs/README.spl.md

clean:
	@echo
	@echo "Removing '$(ORIGDIR)' and '$(FLIPDIR)'."
	@rm -rf $(ORIGDIR)
	@rm -rf $(FLIPDIR)

