python GEDIT.py -mix mixtureFile.tsv -ref referenceFile.tsv

This uses default parameters. You can also modify the parameters by adding 3 arguments to the end in this order:

NumSigs: default = 50
SigMethod: default = "Entropy"
RowScaling: default = 0.0

e.g. 
python GEDIT.py -mix SampleMat1.csv -ref SampleMat2.csv -NumSigs 50 -SigMethod Entropy -RowScaling 0.0


This will spit out an R command to standard out (or in the log file if job submitted), which you can execute to produce the final predictions.

Requires R >= 3.5.0


on hoffman setup:

module load R/3.6.0
install.packages('gplots', dependencies=TRUE)
install.packages('RColorBrewer', dependencies=TRUE)
install.packages('glmnet', dependencies=TRUE)

type: yes
choose option: 58


Then run final Rscript command printed to standard out.



Dependancies include the R packages:
glmnet
RColorBrewer
gplots

python:
os
random
numpy
