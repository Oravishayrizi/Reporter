import os
import fnmatch
import subprocess
import time

#Based on Q from: https://latex.org/forum/viewtopic.php?t=3622
__file__ = 'makereport.py'
### Put this file in the WD
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

### The name of the file you will make is: "reports.tex"

stream = open("reports/reports.tex", "w")

stream.write("\\documentclass{article}\n")
stream.write("\\usepackage{graphicx}\n")
stream.write("\\usepackage{booktabs}\n")
stream.write("\\usepackage{float}\n")
stream.write("\\usepackage[T1]{fontenc}% http://ctan.org/pkg/fontenc \n\n")


stream.write("\\makeatletter\n")
stream.write("\\newcommand\\newlof{% \n")
stream.write("	\\section{\\protect\\listfigurename}% \n	\\@mkboth{\\MakeUppercase\\listfigurename}% \n	{\\MakeUppercase\\listfigurename}% \n	\\@starttoc{lof}% \n")
stream.write("} \n\\makeatother \n \n")



stream.write("\\begin{document}\n \n")

stream.write("\\listoftables\n")
stream.write("\\clearpage\n \n")

stream.write("\\newlof\n")
stream.write("\\clearpage\n")

#look for all "tex" files in sub-folder "tables" 
#and make a string "\input{tables/* for each tex file
for table_tex in sorted(fnmatch.filter(os.listdir("tables"), "*.tex")):
     stream.write("\\input{../tables/%s}\n" % table_tex)

#same for figures
# I use *.* as I make plots using different extensions...

for fig in sorted(fnmatch.filter(os.listdir("figures"), "*.*")):
    stream.write("\n")
    stream.write("\\begin{figure}[H]\n")
    stream.write("\\centering\n")
    stream.write("\\includegraphics[width=1\\textwidth]{../figures/%s}\n" % fig)
    stream.write("\\caption{\\protect\\detokenize{%s}}\n" % fig)
    stream.write("\\end{figure}\n")
    stream.write("\\clearpage\n")



stream.write("\\end{document}\n")
stream.close()

answer = input("Tex file was made, would you like to compile it to PDF? Y/N ") 
if answer == "Y":
    print("Compiling report.tex into report.pdf")
    #print(os.getcwd())
    os.chdir('reports') 
    print(os.getcwd())
    #os.system("pdflatex \"reports\".tex");
    subprocess.Popen(['pdflatex', 'reports.tex'])
    time.sleep(1.5)
    subprocess.Popen(['pdflatex', 'reports.tex'])
    print("Press any key to quit")

elif answer == "N":
    print("Quit")
else:
    print("Please enter Y(yes) or N(no). Quits Now, reload the Bat file")
    
