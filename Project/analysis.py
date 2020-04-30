import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

data = pd.read_csv("Data.csv")
def SummarySepalLength():
    return data.setosasl.describe()

def SumarrySepalWidth():
    return data.setosasw.describe()

def SumarryPetalLength():
    return data.setosapl.describe()

def SumarryPetalWidth():
    return data.setosapw.describe()

def SummarySepalLengthVeriscolor():
    return data.versicolorsl.describe()

def SummarySepalWidthVeriscolor():
    return data.versicolorsw.describe()

def SummaryPetalWidthVeriscolor():
    return data.veriscolorpw.describe()

def SummaryPetallengthVeriscolor():
    return data.veriscolorpl.describe()

def SummarySepalLengthVirginica():
    return data.virginicasl.describe()

def SumarryViriginicaSepalWidth():
    return data.virginicasw.describe()

def SumamrryVirgincaPetalLength():
    return data.virigincapl.describe()

def SummarryVirgincaPetalwidth ():
    return data.virigincapw.describe()

Iris_VersicolorsSepalLength =str(SummarySepalLengthVeriscolor())
Iris_setosaPetalLength = str(SumarryPetalLength())
Iris_setosaSepalWidth = str(SumarrySepalWidth())
Iris_setosaSepalLength =str(SummarySepalLength())
Iris_setosaPetalWidth = str(SumarryPetalWidth())
Iris_VersicolorsSepalWidth = str(SummarySepalWidthVeriscolor())
Iris_VersicolorsPetalWidth = str(SummaryPetalWidthVeriscolor())
Iris_VersicolorsPetalLength = str(SummaryPetallengthVeriscolor())
Iris_ViginicaSepalLength = str(SummarySepalLengthVirginica())
Iris_ViginicaSepalWidth = str(SumarryViriginicaPetalWidth())
Iris_ViginicaPetalLength = str(SumamrryVirgincaPetalLength())
Iris_ViginicaPetalwidth = str(SumamrryVirgincaPetalwidth ())
Iris_VeriscolorSepalLength = str(SummarySepalLengthVeriscolor())
 #converts series into string
file = open("analysis.txt", "w") #opens text file and makes it writable 
file.write(Iris_setosaSepalLength)
file.write(Iris_setosaSepalWidth)
file.write(Iris_setosaPetalLength) #writes summary to text
file.write(Iris_setosaPetalWidth)
file.write(Iris_VersicolorsSepalLength)
file.write(Iris_VersicolorsSepalWidth )
file.write(Iris_VersicolorsPetalWidth)
file.write(Iris_VeriscolorSepalLength )
file.write(Iris_ViginicaSepalLength)
file.write(Iris_ViginicaSepalWidth)
file.write(Iris_ViginicaPetalLength)
file.write(Iris_ViginicaPetalwidth)
file.close()


