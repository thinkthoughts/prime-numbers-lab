PDF=main.pdf
TEX=main.tex
all:
	latexmk -pdf $(TEX)
pdflatex:
	pdflatex $(TEX)
	bibtex main || true
	pdflatex $(TEX)
	pdflatex $(TEX)
clean:
	latexmk -C
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.fls *.fdb_latexmk
