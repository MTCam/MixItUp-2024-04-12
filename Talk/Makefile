all: all-redirect

BASENAME=mixitup-2024-04-12
LATEX = pdflatex --shell-escape
FIGURES := $(shell find Figures -type f \( -name "*.pdf" -o -name "*.png" -name "*.py" -name "*.tikz" \))
SUBTALKS := $(shell ls subtalk-*.tex) ../ceesd-acknowledgement.tex ../ceesd-macros.tex

.SUFFIXES: .pdf .tex

.tex.pdf: 
	$(LATEX) $*

all-redirect: $(BASENAME).pdf

$(BASENAME).pdf: $(BASENAME).tex $(SUBTALKS) $(FIGURES)

clean:
	rm -fr _mint* *.vrb *.tex~ *.toc *.aux *.log *.nav *.out *.snm *.flc

realclean: clean
	rm -f $(BASENAME).pdf

