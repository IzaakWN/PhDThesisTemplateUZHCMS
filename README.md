# Thesis template for UZH CMS

LaTeX template for a PhD thesis in the CMS group of the University of Zurich (UZH).

The main file is [`thesis.tex`](thesis.tex), which loads the chapters from [`sections/`](sections/).

## Title page
The faculty of natural sciences (MNF) has strict guidelines for the tile page and provides a template in MS Word.
Please see https://www.mnf.uzh.ch/en/studium/phd/checkliste-fuer-doktorierende.html
A LaTeX version of this template can be found in [`titlepage/`](titlepage).

## Settings
The preamble with settings like page layout are set in [`settings/preamble.tex`](settings/preamble.tex).
Note that the document class is `scrreprt` from KOMA-script bundle.

Some of the common macros and particle pennames in CMS TDR are mimicked in [`settings/macros_CMS_TDR.tex`](settings/macros_CMS_TDR.tex).
Note that for particle names, "unslanted" Greek letters are used (this is just my personal preference to separate them from variables, which are in italics).
Other common macros are loaded from [`settings/macros_user.tex`](settings/macros_user.tex).

## Figures
Some basic figures related to the SM, LHC, and CMS can be found in [`fig/`](fig).
Please note the rules for plots with CMS data, simulation, results in PhD theses:
https://twiki.cern.ch/twiki/bin/view/CMS/PhysicsApprovals#Thesis_endorsement

## References
A bibliography style file for `BibTeX` that is adopted from the official CMS TDR style can be found in [`bib/`](bib).

## Import to Overleaf
Please see the instructions [here](https://www.overleaf.com/learn/how-to/Using_Git_and_GitHub).