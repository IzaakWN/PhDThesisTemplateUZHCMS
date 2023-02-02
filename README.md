# Thesis template for UZH CMS

LaTeX template for a PhD thesis in the CMS group of the University of Zurich (UZH).
For a Master thesis in the Physics Institute, an official UZH template can also be found
[here](https://www.physik.uzh.ch/en/study/Counselling-and-forms/formulare.htm).

The main file is [`thesis.tex`](thesis.tex), which loads the chapters from [`sections/`](sections/).
If you use TeXShop, you can include `%!TEX root = ../thesis.tex` at the top of each file to compile this file.

## Title page
The faculty of natural sciences (MNF) has strict guidelines for the tile page and provides a template in MS Word.
Please see https://www.mnf.uzh.ch/en/studium/phd/checkliste-fuer-doktorierende.html.
A LaTeX version of this template can be found in [`titlepage/`](titlepage).

## Settings
The preamble with settings like page layout are set in [`settings/preamble.tex`](settings/preamble.tex).
Note that the document class is `scrreprt` from the KOMA-script bundle.

Some of the common macros and particle pennames in CMS TDR are mimicked in [`settings/macros_CMS_TDR.tex`](settings/macros_CMS_TDR.tex).
Note that for particle names, "unslanted" Greek letters are used (this is just my personal preference to separate them from variables, which are in italics).
Other common macros are loaded from [`settings/macros_user.tex`](settings/macros_user.tex).

## Figures
Some basic figures related to the SM, LHC, and CMS plus sources and can be found in [`fig/`](fig).

Please note the rules for plots with CMS data, simulation, results in PhD theses:
https://twiki.cern.ch/twiki/bin/view/CMS/PhysicsApprovals#Thesis_endorsement

## References
A bibliography style file for `BibTeX` that is adopted from the official CMS TDR style can be found in [`bib/`](bib),
as well as a bunch of BibTeX files with useful references.

## Copy/Import to Overleaf
This GitHub repo is synced to [this Overleaf project](https://www.overleaf.com/read/mspvhdpynsjb).
You can copy it to your own account.

Alternatively, you can clone this GitHub repo locally, and push it to
[Overleaf](https://www.overleaf.com/learn/how-to/Using_Git_and_GitHub).
Create a new "Blank Project" from [My Projects](https://www.overleaf.com/project)
on Overleaf. Find the git repo link of your project from the menu under "Git".
```
git clone git@github.com:IzaakWN/PhDThesisTemplateUZHCMS.git thesis
cd thesis
git remote add overleaf https://git.overleaf.com/...
git checkout master
git pull overleaf master --allow-unrelated-histories
git revert --mainline 1 HEAD
git push overleaf master
```