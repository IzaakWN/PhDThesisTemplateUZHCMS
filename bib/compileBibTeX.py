#! /usr/bin/env python3
# Author: Izaak Neutelings (July 2023)
# Description:
#   Compile BibTeX.
# Instructions:
#   ./compileBibTeX.py thesis.bib
from __future__ import print_function
import os, re, stat
rexp_ref = re.compile(r"\s*@\w+\{\s*([\w\.-]+\s*),")


def printsep(w=120,n=2,c='#',wl=True):
  """Print seperator."""
  if wl: print()
  for i in range(n): print(c*w)
  if wl: print()
  

def ensuredir(dname,verb=0):
  """Make directory if it does not exist."""
  if not os.path.exists(dname):
    if verb>=1:
      print(f">>> Making directory {dname}...")
    os.makedirs(dname)
  return dname
  

def getrefs(fname):
  """Get all references from .bib file."""
  refs = [ ]
  with open(fname,'r') as file:
    for line in file:
      match = rexp_ref.match(line)
      if match:
        refs.append(match.group(1))
  return refs
  

def writeComparisonFiles(bibfname,texfname,refs,compile=False,cmstdr=False):
  """Create TeX document to compare PDF output in order to validate reformatted BibTeX file."""
  import shutil, subprocess
  from datetime import datetime
  outdir = "." #os.path.dirname(outfname)
  if not texfname:
    texfname = bibfname[:-4]+'.tex' #os.path.join(outdir,os.path.basename()
  texdir = os.path.join(texfname)
  #bibpath  = os.path.join(texdir,os.path.basename(infname)) # full path
  #shutil.copyfile(bibfname,bibpath)
  print(f">>> Writing citations from {bibfname} to {texfname}...")
  with open(texfname,'w') as texfile:
    texfile.write(f"% Auto-generated by compileBibTeX.py on {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}\n")
    texfile.write(f"% for comparing compiled PDFs via https://www.diffchecker.com/pdf-diff/\n")
    if cmstdr:
      maxchars = 68
      texfile.write('\n')
      texfile.write(r'{\small'+'\n')
    else:
      maxchars = 80
      texfile.write(r"\documentclass[11pt]{article}"+'\n')
      texfile.write(r"\usepackage[margin=2cm]{geometry}"+'\n')
      texfile.write(r"\usepackage{amsmath,hyperref}"+'\n')
      texfile.write(r"\usepackage[hyperref=true,natbib=true,backend=bibtex,style=numeric,sorting=none]{biblatex}"+'\n')
      texfile.write(r"\newcommand*{\DOI}[1]{\textsc{doi:}~\href{http://dx.doi.org/#1}{\texttt{#1}}}"+"\n")
      #texfile.write(fr"\bibliography{{{os.path.basename(bibpath)}}}"+"\n")
      #texfile.write(fr"\addbibresource{{{os.path.basename(bibpath)}}}"+"\n")
      texfile.write(fr"\bibliography{{{os.path.basename(bibfname)}}}"+"\n")
      texfile.write(fr"\addbibresource{{{os.path.basename(bibfname)}}}"+"\n")
      texfile.write(r"\begin{document}"+"\n\n")
    texfile.write(fr"Citing from \verb|{bibfname}|:\\"+'\n')
    nchars = 0
    ###refs = refs[:50] # for debugging
    for i, ref in enumerate(refs,1):
      line = fr"\verb|{ref}|~\cite{{{ref}}}"
      nchars += len(ref)+3
      if i==len(refs): # last citation
        line += r".\\"+"\n\n"
      elif nchars<maxchars:
        line += ", "
      else: # wrap/break line
        line = r"\\"+'\n'+line+r", "
        nchars = len(ref)+3
      texfile.write(line)
    if cmstdr:
      texfile.write(r'}'+'\n')
      texfile.write(r"\bibliography{auto_generated}"+"\n\n")
    else:
      texfile.write(r"\printbibliography"+"\n\n")
      texfile.write(r"\end{document}"+'\n')
  
  # PREPARE COMMANDS / SCRIPT
  print(f">>> Prepare script...")
  sname = texfname.replace('.tex','.sh') #os.path.join(texdir,texfname.replace('.tex','.sh'))
  if outdir in ['','.','./']:
    sname = os.path.join('./',sname)
  cmds = [ f"cd {texdir}" ]
  scripts = [ sname ]
  with open(sname,'w') as script:
    script.write('#! /bin/bash')
    script.write(f"# Auto-generated by compileBibTeX.py on {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}\n")
    script.write('function peval { echo -e ">>> $@"; eval "$@"; }\n')
    if cmstdr:
      style = 'paper' if '/papers/' in texfname else 'an' if '/notes/AN-' in texfname else 'pas' #tdr/note/an/pas/cr/in/paper
      cmds.append(f"../../utils/tdr --preview --style={style} --noclean --temp_dir=. b {texfname}")
    else:
      auxfname = texfname[:-4]+'.aux'
      pdffname = texfname[:-4]+'.pdf'
      pdfcmd   = f"pdflatex -interaction=nonstopmode {texfname}"
      cmds.append(f"{pdfcmd} && bibtex {auxfname} && {pdfcmd} && {pdfcmd} && open {pdffname}")
    for cmd in cmds:
      script.write(f'peval "{cmd}"\n')
  os.chmod(sname,stat.S_IRWXU)
  
  # COMPILE
  if compile:
    for script in scripts:
      printsep()
      print(f">>>\n>>> Executing script {script}...")
      os.system(script)
      #process = subprocess.Popen(subcmd,stdout=subprocess.PIPE,shell=True)
      #print(process.communicate())
    printsep()
    print(f">>> Please find comparison output in {outdir}")
  else:
    print(">>> Compile with:")
    for cmd in cmds:
      print(f">>>   {cmd}")
  print(">>> Compare PDFs on https://www.diffchecker.com/pdf-diff/ or with Adobe Acrobat")
  

def main(args):
  """Main routine."""
  
  # USER INPUT
  infnames  = args.infnames # .bib file
  outfname  = args.outfname # .tex file
  compile   = args.compile  # compile comparison files
  cmstdr    = args.cmstdr   # prepare TeX files for CMS's TDR script
  verbosity = args.verbosity
  
  for infname in infnames:
    
    # GET ALL REFERENCES
    refs = getrefs(infname)
    
    # WRITE TEX FILE
    writeComparisonFiles(infname,outfname,refs,cmstdr=cmstdr,compile=compile)
  

if __name__ == '__main__':
  from argparse import ArgumentParser
  description = """Clean BibTeX file: key ordering, capitalization, indentation, spacing, ... and detect potential issues."""
  parser = ArgumentParser(prog="plot",description=description,epilog="Good luck!")
  parser.add_argument('infnames',       nargs='+', help="filename of BibTeX file to reformat" )
  parser.add_argument('-o','--outfname',help="output filename of reformatted BibTeX file")
  parser.add_argument('-x','--compile', action='store_true',
                                        help="compile comparison LaTeX files")
  parser.add_argument('-T','--cmstdr',  action='store_true',
                                        help="create comparison LaTeX files for CMS's TDR script")
  parser.add_argument('-v','--verbose', dest='verbosity', type=int, nargs='?', const=1, default=0, action='store',
                                        help="set verbosity")
  args = parser.parse_args()
  main(args)
  #print(">>> Done")
  
