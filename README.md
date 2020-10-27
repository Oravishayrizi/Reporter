This is a minimal example for the a code that compiles all the figures and tables into one report.
It contains a "typical" project folder with scripts that located in the sub-folder "codes".
The output of these scripts is saved into "figures" and "tables" sub-folders.

The makereport.py is a python code does two seperate jobs:
1. Takes all the figures and tables from their tables and place them in one LATEX file (saved as reports/reports.tex).
2. The Python scripts ask you whether you want to compile this .tex file into PDF file for convinient (saved as reports/reports.PDF).

To run this Python script easily I wrote batch file- run.bat, you just need to double click it

requirements:
Python 3, (including these packages: os, fnmatch, subprocess, time)
pdflatex

Here is a structure of the project directory
|   makereport.py
|   run.bat
|   
+---codes
|       makefigures.R
|       maketables.R
|       
+---figures
|       iris_histogram.pdf
|       mpg_line_plot.jpeg
|       scatter plot.pdf
|       
+---reports
|       reports.tex
|       
+---tables
|       mpg_desc_stat.tex
|       mpg_head.tex        
