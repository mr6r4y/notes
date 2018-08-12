# Documenting - LaTeX, PDF/DOCX Generation, etc.

## LaTeX

Initializing `tlmgr` (LaTeX package manager):

    $ tlmgr init-usertree
    $ sudo apt install xzdec
    $ tlmgr update --all
    $ tlmgr list

## Pandoc

Presentation with `beamer`:

    pandoc -t beamer habits.txt -o habits.pdf

When Cyrillic must be used font:

    pandoc --latex-engine=xelatex -t latex -o report.pdf -V mainfont="Liberation Serif" report.md

---

When generating report with TOC on separate pages:

    pandoc report.md --toc --include-in-header ./titlesec.tex --toc-depth=5 -o report.pdf

where `titlesec.tex` contains:

    \usepackage{sectsty} \sectionfont{\clearpage}

---

Include this in document instead of previous. This includes a package for verbatim line wrapping.

    ---
    header-includes:
     - \usepackage{sectsty} \sectionfont{\clearpage}
     - \usepackage{fvextra}
     - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
    ---

---

Latex beamer style for coloring the HREFs:

    \definecolor{links}{HTML}{2A1B81}
    \hypersetup{colorlinks,linkcolor=,urlcolor=links}

---

    pandoc report.md --toc --latex-engine=xelatex --toc-depth=5 -o report.pdf

---

Using beamer, include latex style headers:

    pandoc -t beamer --include-in-header styles.tex -o presentation.pdf presentation.md
