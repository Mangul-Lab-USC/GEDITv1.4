import MatrixTools
"""
Parses the input submitted by the user. Checks that each input is valid.
If all inputs valid, returns them as a list. If an input is invalid,
returns False, ErrorMessage
"""
def checkInputs(InputString):
  argDict = argsToDict(InputString)
  
  if "mix" not in argDict:
    return False, "Mixture matrix not specified. Please indicate\
               a mixture file using the argument -mix myfile.tsv"

  MixFName = argDict["mix"]
  Mix = MatrixTools.readMatrix(MixFName)
  mixCheck = checkMatrix(Mix)
  if mixCheck != True:
    return False, "An error was detected with your\
     submitted mixture file:\n" + mixCheck

  if "ref" not in argDict:
    return False, "reference matrix not specified. Please indicate\
               a reference file using the argument -ref myfile.tsv"
  RefFName = argDict["ref"]
  Ref = MatrixTools.readMatrix(RefFName)
  refCheck = checkMatrix(Ref)
  if refCheck != True:
    return False,"An error was detected with your\
                 submitted reference file:\n" + refCheck
  
  if "numSigs" in argDict:
    totalSigs = argDict["numSigs"]
    try:
      totalSigs  = int(totalSigs)
      if totalSigs < 1 or totalSigs > 10000:
        return False, "invalid numSigs:  " + totalSigs
    except:
      return False, "invalid numSigs:  " + totalSigs
  else:
    totalSigs = 50

  if "minSigs" in argDict:
    minSigs = argDict["minSigs"]
    try:
      MinSigsPerCT = int(MinSigsPerCT)
      if MinSigsPerCT < 1 or MinSigsPerCT > totalSigs:
        return False, "invalid MinSigsPerCT" + MinSigsPerCT
    except:
      return False, "invalid MinSigsPerCT" + MinSigsPerCT
  else:
    MinSigsPerCT = totalSigs

  if "method" in argDict:
    SigMethodList = argDict["method"] 
    for SigMethod in SigMethodList.split(","):
      if SigMethod not in ["Intensity","Entropy",\
      "Zscore","MeanRat","MeanDiff","fsRat","fsDiff","IntEnt"]:
        return False, "invalid sigMethod" + SigMethodList
  else:
    SigMethodList = "Entropy"

  if "RS" in argDict:
    try:
      RowScaling = float(argDict["RS"])
      if float(RowScaling) > 1.0 or float(RowScaling) < 0.0:
        print "invalid RowScaling", RowScaling
        return False
    except:
      print "invalid RowScaling", argDict["RS"]
      return False
  else:
    RowScaling = 0.0
  return [Mix, Ref, totalSigs, MinSigsPerCT, SigMethodList, RowScaling, MixFName, RefFName]

def argsToDict(ArgList):
  argDict = {}
  for i in range(len(ArgList)):
     if ArgList[i][0] == "-":
       argDict[ArgList[i][1:]] = ArgList[i+1]
  return argDict

def checkMatrix(matrix):
  """
  returns True if matrix is ok, otherwise returns text describing error
  """

  nameLength = len(matrix[0])

  for row in matrix[1:]:
     if len(row) != nameLength:
       print matrix[0]
       return "this row is not of the same length as the first: \n" + "\t".join(row[:10])#  + "\n FirstRow: \n" + "\t".join(matrix[0])

     if len(row) == 1:
       return "The system is detecting only 1 column in your\
        matrix. Please check that the fields in your file \
        are separated by commas or tab charectors"
     for el in row[1:]:
       try:
         float(el)
       except:
         return "non-numeric value in the matrix: " + str(el)
  
  return True
