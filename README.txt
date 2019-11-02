python GEDIT.py -mix mixtureFile.tsv -ref referenceFile.tsv

This uses default parameters. You can also modify the parameters by adding 3 arguments to the end in this order:

NumSigs: default = 50
SigMethod: default = "Entropy"
RowScaling: default = 0.0

e.g. 
python GEDIT.py -mix SampleMat1.csv -ref SampleMat2.csv -NumSigs 50 -SigMethod Entropy -RowScaling 0.0


This will spit out an R command, which you can execute to produce the final predictions

Dependancies include the R packages:
glmnet
RColorBrewer
gplots

python:
os
random
numpy
