# USC setup:

source /usr/usc/python/2.7.6/setup.sh 
pip install statistics --user
pip install os --user
pip install random --user
pip install numpy --user

source /usr/usc/R/3.6.0/setup.sh

R

install.packages('gplots', dependencies=TRUE)
install.packages('RColorBrewer', dependencies=TRUE)
install.packages('glmnet', dependencies=TRUE)

type: yes
choose option: 58


cd GEDITv1.4

python GEDIT.py -mix path/to/Gene_Name_Matrix.csv -ref references/LM22_Full.tsv

This will spit out an R command to standard out (or in the log file if job submitted), which you can execute to produce the final predictions, which will be generated inside the predictions folder.


# hoffman setup:

module load python/2.7
pip install statistics --user
pip install os --user
pip install random --user
pip install numpy --user

module load R/3.6.0

R

install.packages('gplots', dependencies=TRUE)
install.packages('RColorBrewer', dependencies=TRUE)
install.packages('glmnet', dependencies=TRUE)

type: yes
choose option: 58

cd GEDITv1.4

python GEDIT.py -mix path/to/Gene_Name_Matrix.csv -ref references/LM22_Full.tsv

This will spit out an R command to standard out (or in the log file if job submitted), which you can execute to produce the final predictions, which will be generated inside the predictions folder.



										------extended options-------



python GEDIT.py -mix mixtureFile.tsv -ref referenceFile.tsv

This uses default parameters. You can also modify the parameters by adding 3 arguments to the end in this order:

NumSigs: default = 50
SigMethod: default = "Entropy"
RowScaling: default = 0.0

e.g. 
python GEDIT.py -mix SampleMat1.csv -ref SampleMat2.csv -NumSigs 50 -SigMethod Entropy -RowScaling 0.0


This will spit out an R command to standard out (or in the log file if job submitted), which you can execute to produce the final predictions, which will be generated inside the predictions folder.


Dependancies include the R packages:
glmnet
RColorBrewer
gplots

python:
os
random
numpy
