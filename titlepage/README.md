# UZH MNF Title Page

The faculty of natural sciences (MNF) has strict guidelines for the tile page and provides a template in MS Word.
Please see https://www.mnf.uzh.ch/en/studium/phd/checkliste-fuer-doktorierende.html.

For a Master thesis in the Physics Institute, an official UZH template with a different title page can also be found
[here](https://www.physik.uzh.ch/en/study/Counselling-and-forms/formulare.htm).

MS Word template:
- `titlepage_UZH_MNF2011.doc`: as provided by MNF with instructions & comments
- `titlepage_UZH_PhD.doc`: with instructions & comments removed
- `titlepage_UZH_PhD.pdf`: PDF version of the above template
- `titlepage_UZH_PhD_red.pdf`: PDF version of the above template in red for comparison

LaTeX template:
- `titlepage.tex`: loaded by `thesis.tex` via `\include{titlepage/titlepage}`
- `titlepage_test.tex`: standalone file for testing
- `titlepage_test.pdf`: output from the above file
- `titlepage_test_overlay.pdf`: output from the above file, plus overlay of `titlepage_UZH_PhD_red.pdf` for comparison
