FILENAME = HEPML

date = $(shell date +%Y-%m-%d)
output_file = draft_$(date).pdf

LATEX = lualatex
BIBTEX = bibtex

all: default

default: document copy_draft

document:
	latexmk -$(LATEX) -logfilewarnings -halt-on-error $(FILENAME)

copy_draft:
	rsync $(FILENAME).pdf $(output_file)

clean:
	rm -f *.aux *.bak *.bbl *.blg *.dvi *.idx *.lof *.log *.lot *.toc \
		*.glg *.gls *.glo *.xdy *.nav *.out *.snm *.vrb *.mp \
		*.synctex.gz *.run.xml *.bcf *.brf *.fls *.fdb_latexmk

realclean: clean
	rm -f *.ps *.pdf

final:
	if [ -f *.aux ]; \
		then make clean; \
	fi
	make document
