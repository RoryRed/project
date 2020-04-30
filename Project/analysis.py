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
    return data.versicolorpw.describe()

def SummaryPetallengthVeriscolor():
    return data.versicolorpl.describe()

def SummarySepalLengthVirginica():
    return data.virginicasl.describe()

def SumarryViriginicaSepalWidth():
    return data.virginicasw.describe()

def SumamrryVirgincaPetalLength():
    return data.virginicapl.describe()

def SummarryVirgincaPetalwidth ():
    return data.virginicapw.describe()

Iris_VersicolorsSepalLength =str(SummarySepalLengthVeriscolor())
Iris_setosaPetalLength = str(SumarryPetalLength())
Iris_setosaSepalWidth = str(SumarrySepalWidth())
Iris_setosaSepalLength =str(SummarySepalLength())
Iris_setosaPetalWidth = str(SumarryPetalWidth())
Iris_VersicolorsSepalWidth = str(SummarySepalWidthVeriscolor())
Iris_VersicolorsPetalWidth = str(SummaryPetalWidthVeriscolor())
Iris_VersicolorsPetalLength = str(SummaryPetallengthVeriscolor())
Iris_ViginicaSepalLength = str(SummarySepalLengthVirginica())
Iris_ViginicaSepalWidth = str(SumarryViriginicaSepalWidth())
Iris_ViginicaPetalLength = str(SumamrryVirgincaPetalLength())
Iris_ViginicaPetalwidth = str(SummarryVirgincaPetalwidth())
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


#histogram

data = pd.read_csv("Data.csv")
plt.title("Iris-setosa Sepal Length")
plt.hist(data.setosasl,  rwidth = 0.5)
plt.savefig("Iris-setosa Sepal Length.png")

plt.hist(data.setosasw, rwidth = 0.5)
plt.title("Iris-setosa Sepal Width")
plt.savefig("Iris-setosa Sepal Width.png")


plt.hist(data.setosapl, rwidth = 0.5)
plt.title("Iris-setosa Petal Length")
plt.savefig("Iris-setosa Petal Length")


plt.hist(data.setosapw, rwidth = 0.5 )
plt.title("Iris-setosa Petal Width")
plt.savefig("Iris-setosa Petal Width.png")

plt.hist(data.versicolorsl, rwidth = 0.5)
plt.title("Iris-versicolor Sepal Length")
plt.savefig("Iris-versicolor Sepal Length.png")

plt.hist(data.versicolorsw , rwidth = 0.5 )
plt.title("Iris-versicolor Sepal Width ")
plt.savefig("Iris-versicolor Sepal Width.png")

plt.hist(data.versicolorpl, rwidth = 0.5)
plt.title("Iris-versicolor Sepal Length")
plt.savefig("Iris-versicolor Sepal Length.png")

plt.hist(data.versicolorpw, rwidth = 0.5)
plt.title("Iris-virginica Petal Width")
plt.savefig("Iris-virginica Petal Width.png")

plt.hist(data.virginicasl, rwidth = 0.5 )
plt.title("Iris-virginica Sepal Length")
plt.savefig("Iris-virginica Sepal Length.png")

plt.hist(data.virginicasw, rwidth = 0.5)
plt.title("Iris-virginica Sepal Width")
plt.savefig("Iris-virginica Sepal Width.png")

plt.hist(data.virginicapl, rwidth = 0.5)
plt.title("Iris-virginica Petal Length")
plt.savefig("Iris-virginica Petal Length.png")

plt.hist(data.virginicapw, rwidth = 0.5)
plt.title("Iris-virginica Petal Width")
plt.savefig("Iris-virginica Petal Width.png")