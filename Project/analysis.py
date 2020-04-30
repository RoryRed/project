import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

data = pd.read_csv("Data.csv") #reads from data set
def SummarySepalLength(): #function to describe sepal length
    return data.setosasl.describe() # returns summary for setosa iris sepal length

def SumarrySepalWidth(): #function for setosa sepal width
    return data.setosasw.describe() # returns summary for setosa iris sepal width

def SumarryPetalLength(): #function for setosa petal length
    return data.setosapl.describe() # returns summary for setosa iris petal length

def SumarryPetalWidth(): #function for setosa petal width
    return data.setosapw.describe() # returns summary for setosa iris petal width

def SummarySepalLengthVeriscolor(): # function for veriscolor sepal length
    return data.versicolorsl.describe() # returns summary for veriscolor iris length

def SummarySepalWidthVeriscolor(): # function for veriscolor sepal width
    return data.versicolorsw.describe() # returns summary for veriscolor iris width

def SummaryPetalWidthVeriscolor(): # function for veriscolor sepal width
    return data.versicolorpw.describe() #returns summary for veriscolor iris petal width

def SummaryPetallengthVeriscolor(): # function for veriscolor Petal Length
    return data.versicolorpl.describe() #returns summary for versicolor petal length

def SummarySepalLengthVirginica(): # function for virginica sepal length
    return data.virginicasl.describe() # returns summary for veriscolor sepal length

def SumarryViriginicaSepalWidth(): # function for  of virginica sepal width
    return data.virginicasw.describe() # returns summary for virginica sepal width

def SumamrryVirgincaPetalLength(): # function for  of viginica petal length
    return data.virginicapl.describe() # returns summary for virginica petal length

def SummarryVirgincaPetalwidth (): # function for virginca petal width
    return data.virginicapw.describe() # returns summary for virginica petal width

Iris_VersicolorsSepalLength =str(SummarySepalLengthVeriscolor()) #convers series to a string
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
file.write(Iris_setosaSepalLength) # writes summary to text file
file.write(Iris_setosaSepalWidth)
file.write(Iris_setosaPetalLength) #writes summary to text file has to be done for each one individually 
file.write(Iris_setosaPetalWidth)
file.write(Iris_VersicolorsSepalLength)
file.write(Iris_VersicolorsSepalWidth )
file.write(Iris_VersicolorsPetalWidth)
file.write(Iris_VeriscolorSepalLength )
file.write(Iris_ViginicaSepalLength)
file.write(Iris_ViginicaSepalWidth)
file.write(Iris_ViginicaPetalLength)
file.write(Iris_ViginicaPetalwidth)
file.close() # closes file


#histogram
plt.figure(figsize = (15,5))
plt.title("Iris-setosa Sepal Length")
plt.hist(data.setosasl,  rwidth = 0.5)
plt.savefig("Iris-setosa Sepal Length.png")

plt.figure(figsize = (15,5))
plt.hist(data.setosasw, rwidth = 0.5)
plt.title("Iris-setosa Sepal Width")
plt.savefig("Iris-setosa Sepal Width.png")

plt.figure(figsize = (15,5))
plt.hist(data.setosapl, rwidth = 0.5)
plt.title("Iris-setosa Petal Length")
plt.savefig("Iris-setosa Petal Length")

plt.figure(figsize = (15,5))
plt.hist(data.setosapw, rwidth = 0.5 )
plt.title("Iris-setosa Petal Width")
plt.savefig("Iris-setosa Petal Width.png")

plt.figure(figsize = (15,5))
plt.hist(data.versicolorsl, rwidth = 0.5)
plt.title("Iris-versicolor Sepal Length")
plt.savefig("Iris-versicolor Sepal Length.png")

plt.figure(figsize = (15,5))
plt.hist(data.versicolorsw , rwidth = 0.5 )
plt.title("Iris-versicolor Sepal Width ")
plt.savefig("Iris-versicolor Sepal Width.png")


plt.figure(figsize = (15,5))
plt.hist(data.versicolorpl, rwidth = 0.5)
plt.title("Iris-versicolor Sepal Length")
plt.savefig("Iris-versicolor Sepal Length.png")


plt.figure(figsize = (15,5))
plt.hist(data.versicolorpw, rwidth = 0.5)
plt.title("Iris-virginica Petal Width")
plt.savefig("Iris-virginica Petal Width.png")

plt.figure(figsize = (15,5))
plt.hist(data.virginicasl, rwidth = 0.5 )
plt.title("Iris-virginica Sepal Length")
plt.savefig("Iris-virginica Sepal Length.png")


plt.figure(figsize = (15,5))
plt.hist(data.virginicasw, rwidth = 0.5)
plt.title("Iris-virginica Sepal Width")
plt.savefig("Iris-virginica Sepal Width.png")


plt.figure(figsize = (15,5))
plt.hist(data.virginicapl, rwidth = 0.5)
plt.title("Iris-virginica Petal Length")
plt.savefig("Iris-virginica Petal Length.png")


plt.figure(figsize = (15,5))
plt.hist(data.virginicapw, rwidth = 0.5)
plt.title("Iris-virginica Petal Width")
plt.savefig("Iris-virginica Petal Width.png")

plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.setosasw,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title(" Iris-setosa Petal Width vs  Petal Length ")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.setosapl , "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.setosapw,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Sepal Length")
plt.ylabel("Petal Width")
plt.title("Iris-Setosa Sepal Length Vs Petal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.versicolorsl,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Sepal Length")
plt.ylabel("Versicolor Sepal Length")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Sepal Width")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.versicolorsw,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Sepal Length")
plt.ylabel("Versicolor Sepal Width")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Sepal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.versicolorpl,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Sepal Length")
plt.ylabel("Versicolor Petal Length")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Petal Length")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.versicolorpw,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Sepal Length")
plt.ylabel("Versicolor Petal width")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Petal width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.virginicasl,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Sepal Length")
plt.ylabel(" Virginica Iris Sepal Length")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Sepal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.virginicasw,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Sepal Length")
plt.ylabel(" Virginica Iris Sepal width")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Sepal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.virginicapl,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Sepal Length")
plt.ylabel(" Virginica Iris Petal Length")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Petal length")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.virginicapw,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Sepal Length")
plt.ylabel(" Virginica Iris Petal Width")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Petal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.setosapl,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel(" Setosa Iris Pelat Length")
plt.title("Iris-Setosa Sepal Width Vs Iris-Setosa Petal Length")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.setosapw,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel(" Setosa Iris Pelat Width")
plt.title("Iris-Setosa Sepal Width Vs Iris-Setosa Petal Width")
plt.show()



plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.versicolorsl,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel("Versicolor Iris Sepal Length")
plt.title("Iris-Setosa Sepal Width Vs Iris-Versicolar Sepal Length")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.versicolorsw,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel("Versicolor Iris Sepal Width")
plt.title("Iris-Setosa Sepal Width Vs Iris-Versicolor Sepal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.versicolorpl,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel("Versicolor Iris Petal Length")
plt.title("Iris-Setosa Sepal Width Vs Iris-Versicolor Petal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.versicolorpw,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel("Versicolor Iris Petal width")
plt.title("Iris-Setosa Sepal Width Vs Iris-Versicolor Petal width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.virginicasl,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel("Versicolor Iris Petal width")
plt.title("Iris-Setosa Sepal Width Vs Iris-Virginica Sepal  Length")
plt.show()
