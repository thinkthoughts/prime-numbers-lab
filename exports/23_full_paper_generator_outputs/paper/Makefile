.PHONY: all clean

all:
	latexmk -pdf main.tex

fallback:
	pdflatex main.tex
	pdflatex main.tex

clean:
	latexmk -c
	rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.bbl *.blg
