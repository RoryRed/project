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
file.write(Iris_setosaPetalWidth) # write command only accepts one argument therefore each variable had to be written seperatley
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
plt.figure(figsize = (15,5)) #isolates the data to one graph and sets its size
plt.title("Iris-setosa Sepal Length")# title
plt.hist(data.setosasl,  rwidth = 0.5) #creates a histogram with a distance between the bars
plt.savefig("Iris-setosa Sepal Length.png") #saves the graph as a png file
#second histogram same as above
plt.figure(figsize = (15,5))
plt.hist(data.setosasw, rwidth = 0.5)
plt.title("Iris-setosa Sepal Width")
plt.savefig("Iris-setosa Sepal Width.png")
#third histogram
plt.figure(figsize = (15,5))
plt.hist(data.setosapl, rwidth = 0.5)
plt.title("Iris-setosa Petal Length")
plt.savefig("Iris-setosa Petal Length")
#fourth histogram
plt.figure(figsize = (15,5))
plt.hist(data.setosapw, rwidth = 0.5 )
plt.title("Iris-setosa Petal Width")
plt.savefig("Iris-setosa Petal Width.png")
#fifth histogram
plt.figure(figsize = (15,5))
plt.hist(data.versicolorsl, rwidth = 0.5)
plt.title("Iris-versicolor Sepal Length")
plt.savefig("Iris-versicolor Sepal Length.png")
#sixth histogram
plt.figure(figsize = (15,5))
plt.hist(data.versicolorsw , rwidth = 0.5 )
plt.title("Iris-versicolor Sepal Width ")
plt.savefig("Iris-versicolor Sepal Width.png")

#seventh histogram
plt.figure(figsize = (15,5))
plt.hist(data.versicolorpl, rwidth = 0.5)
plt.title("Iris-versicolor Sepal Length")
plt.savefig("Iris-versicolor Sepal Length.png")

#8th histogram
plt.figure(figsize = (15,5))
plt.hist(data.versicolorpw, rwidth = 0.5)
plt.title("Iris-virginica Petal Width")
plt.savefig("Iris-virginica Petal Width.png")

#9th histogram
plt.figure(figsize = (15,5))
plt.hist(data.virginicasl, rwidth = 0.5 )
plt.title("Iris-virginica Sepal Length")
plt.savefig("Iris-virginica Sepal Length.png")

#10th histogram
plt.figure(figsize = (15,5))
plt.hist(data.virginicasw, rwidth = 0.5)
plt.title("Iris-virginica Sepal Width")
plt.savefig("Iris-virginica Sepal Width.png")

#11th histogram
plt.figure(figsize = (15,5))
plt.hist(data.virginicapl, rwidth = 0.5)
plt.title("Iris-virginica Petal Length")
plt.savefig("Iris-virginica Petal Length.png")

#12th histogram
plt.figure(figsize = (15,5))
plt.hist(data.virginicapw, rwidth = 0.5)
plt.title("Iris-virginica Petal Width")
plt.savefig("Iris-virginica Petal Width.png")

#plot
plt.figure(figsize = (15,5))#size of figure
plt.plot(data.setosasl, data.setosasw,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")#plot with datA SET up to be a scatter plot
plt.legend() #adds legend
plt.xlabel("Sepal Length")#labels x axis
plt.ylabel("Sepal Width")# labeels y axis
plt.title(" Iris-setosa Petal Width vs  Petal Length ")#titles graph
plt.show() #ouputs graph

#plot2
plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.setosapl , "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()

#plot3
plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.setosapw,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.legend()
plt.xlabel("Sepal Length")
plt.ylabel("Petal Width")
plt.title("Iris-Setosa Sepal Length Vs Petal Width")
plt.show()

#plot4
plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.versicolorsl,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Sepal Length")
plt.ylabel("Versicolor Sepal Length")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Sepal Width")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.versicolorsw,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Sepal Length")
plt.ylabel("Versicolor Sepal Width")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Sepal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.versicolorpl,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Sepal Length")
plt.ylabel("Versicolor Petal Length")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Petal Length")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.versicolorpw,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Sepal Length")
plt.ylabel("Versicolor Petal width")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Petal width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.virginicasl,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Sepal Length")
plt.ylabel(" Virginica Iris Sepal Length")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Sepal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.virginicasw,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Sepal Length")
plt.ylabel(" Virginica Iris Sepal width")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Sepal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.virginicapl,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Sepal Length")
plt.ylabel(" Virginica Iris Petal Length")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Petal length")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosasl, data.virginicapw,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Sepal Length")
plt.ylabel(" Virginica Iris Petal Width")
plt.title("Iris-Setosa Sepal Length Vs Iris Versicolor Petal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.setosapl,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel(" Setosa Iris Pelat Length")
plt.title("Iris-Setosa Sepal Width Vs Iris-Setosa Petal Length")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.setosapw,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel(" Setosa Iris Pelat Width")
plt.title("Iris-Setosa Sepal Width Vs Iris-Setosa Petal Width")
plt.show()



plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.versicolorsl,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel("Versicolor Iris Sepal Length")
plt.title("Iris-Setosa Sepal Width Vs Iris-Versicolar Sepal Length")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.versicolorsw,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel("Versicolor Iris Sepal Width")
plt.title("Iris-Setosa Sepal Width Vs Iris-Versicolor Sepal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.versicolorpl,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel("Versicolor Iris Petal Length")
plt.title("Iris-Setosa Sepal Width Vs Iris-Versicolor Petal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.versicolorpw,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel("Versicolor Iris Petal width")
plt.title("Iris-Setosa Sepal Width Vs Iris-Versicolor Petal width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.virginicasl,  "mo" ,  marker = "o")
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel("Versicolor Iris sepal width")
plt.title("Iris-Setosa Sepal Width Vs Iris-Virginica Sepal  Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.virginicasw,  "mo" ,  marker = "o")
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel("Versicolor Iris Sepal width")
plt.title("Iris-Setosa Sepal Width Vs Iris-Virginica Sepal  width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.virginicapl,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel("Versicolor Iris Petal Length")
plt.title("Iris-Setosa Sepal Width Vs Iris-Virginica Petal Length")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosasw, data.virginicapw,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Sepal Width")
plt.ylabel("Versicolor Iris Petal Width")
plt.title("Iris-Setosa Sepal Width Vs Iris-Virginica Petal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosapl, data.setosapw,  "mo" ,  marker = "o")
plt.xlabel("Setosa Iris Petal Length")
plt.ylabel("Setosa Iris Petal Width")
plt.title("Iris-Setosa Sepal Width Vs Iris-Setosa Petal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosapl, data.versicolorsl,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Petal Length")
plt.ylabel("Versicolor Iris Sepal Length")
plt.title("Iris-Setosa Sepal Width Vs Iris-Versicolor Sepal Length")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosapl, data.versicolorsw,  "mo" ,  marker = "o")
plt.xlabel("Setosa Iris Petal Length")
plt.ylabel("Versicolor Iris Sepal width")
plt.title("Iris-Setosa Sepal Width Vs Iris-Versicolor Sepal Width")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosapl, data.versicolorpl,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Petal Length")
plt.ylabel("Versicolor Iris Petal Length")
plt.title("Iris-Setosa Sepal Width Vs Iris-Versicolor Petal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosapl, data.versicolorpl,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Petal Length")
plt.ylabel("Versicolor Iris Petal Length")
plt.title("Iris-Setosa Sepal Width Vs Iris-Versicolor Petal Length")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosapl, data.versicolorpw,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Sepal Length")
plt.ylabel("Versicolor Iris Petal Width")
plt.title("Iris-Setosa Petal Length Vs Iris-Versicolor Petal Width")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.setosapl, data.virginicasw,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Sepal Length")
plt.ylabel("Virginica Iris Sepal Width")
plt.title("Iris-Setosa Petal Length Vs Iris-Virginica sepal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosapl, data.virginicapl,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Sepal Length")
plt.ylabel("Virginica Iris Petal Length")
plt.title("Iris-Setosa Petal Length Vs Iris-Virginica Petal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.setosapl, data.virginicapw,  "mo" ,  marker = "o" )
plt.xlabel("Setosa Iris Sepal Length")
plt.ylabel("Virginica Iris Petal Width")
plt.title("Iris-Setosa Petal Length Vs Iris-Virginica Petal Width")
plt.show()



plt.figure(figsize = (15,5))
plt.plot(data.versicolorsl, data.versicolorsw,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Sepal Length")
plt.ylabel("Versicolor Iris Sepal width")
plt.title("Iris-Setosa Petal Length Vs Iris-Versicolor Sepal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorsl, data.versicolorpl,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Sepal Length")
plt.ylabel("Versicolor Iris Petal Length")
plt.title("Iris-Setosa Petal Length Vs Iris-Versicolor Petal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorsl, data.versicolorpw,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Sepal Length")
plt.ylabel("Versicolor Iris Petal Width")
plt.title("Iris-Setosa Petal Length Vs Iris-Versicolor Petal Width")
plt.show()



plt.figure(figsize = (15,5))
plt.plot(data.versicolorsl, data.virginicasl,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Sepal Length")
plt.ylabel("Virginica Iris Sepal Length")
plt.title("Iris-Setosa Petal Length Vs Iris-Virginica Sepal Length")
plt.show()



plt.figure(figsize = (15,5))
plt.plot(data.versicolorsl, data.virginicasw,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Sepal Length")
plt.ylabel("Virginica Iris Sepal Width")
plt.title("Iris-Setosa Petal Length Vs Iris-Virginica Sepal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorsl, data.virginicapl,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Petal Length")
plt.ylabel("Virginica Iris Petal Length")
plt.title("Iris-Setosa Petal Length Vs Iris-Virginica Petal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorsl, data.virginicapw,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Petal Length")
plt.ylabel("Virginica Iris Petal Width")
plt.title("Iris-Setosa Petal Length Vs Iris-Virginica Petal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorsw , data.versicolorpl,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Petal Length")
plt.ylabel("Virginica Iris Petal Length")
plt.title("Iris-Setosa Width Length Vs Iris-Virginica Petal Length")
plt.show()



plt.figure(figsize = (15,5))
plt.plot(data.versicolorsw, data.versicolorpw,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Petal Length")
plt.ylabel("Virginica Iris Petal Width")
plt.title("Iris-Setosa Petal Width Vs Iris-Virginica Petal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorsw, data.virginicasl,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Sepal Length")
plt.ylabel("Virginica Iris Sepal Length")
plt.title("Iris-Setosa Petal Width Vs Iris-Virginica Sepal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorsw, data.virginicasw,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Sepal Width")
plt.ylabel("Virginica Iris Sepal Width")
plt.title("Iris-Versicolor sepal Width Vs Iris-Virginica Sepal Width")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.versicolorsw, data.virginicapl,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Sepal Width")
plt.ylabel("Virginica Iris Petal Length")
plt.title("Iris-Setosa sepal Width Vs Iris-Virginica Petal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorsw, data.virginicapw,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Sepal Width")
plt.ylabel("Virginica Iris Petal Width")
plt.title("Iris-Setosa sepal Width Vs Iris-Virginica Petal width")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.versicolorpl, data.versicolorpw,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Petal Length")
plt.ylabel("Versicolor Iris Petal Width")
plt.title("Iris-Versicolor Petal Length Vs Iris- versicolor  Petal width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorpl, data.virginicasw,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Petal Length")
plt.ylabel("Virginica Iris Sepal Width")
plt.title("Iris-Versicolor Petal Length Vs Iris-Virginica Petal width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorpl, data.virginicasl,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Petal Length")
plt.ylabel("Virginica Iris Sepal length")
plt.title("Iris-Versicolor Petal Length Vs Iris-Virginica Petal length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorpl, data.virginicapl,  "mo" ,  marker = "o")
plt.xlabel("Versicolor Iris Petal Length")
plt.ylabel("Virginica Iris Petal length")
plt.title("Iris-Versicolor Petal Length Vs Iris-Virginica Petal length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorpl, data.virginicapw,  "mo" ,  marker = "o")
plt.xlabel("Versicolor Iris Petal Length")
plt.ylabel("Virginica Iris Petal Width")
plt.title("Iris-Versicolor Petal Length Vs Iris-Virginica Petal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorpw, data.virginicasl,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Petal Width")
plt.ylabel("Virginica Iris Sepal Length")
plt.title("Iris-Versicolor Petal Width Vs Iris-Virginica Petal Width")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.versicolorpw, data.virginicasw,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Petal Width")
plt.ylabel("Virginica Iris Sepal Width")
plt.title("Iris-Versicolor Petal Width Vs Iris-Virginica Sepal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorpw, data.virginicapl,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Petal Width")
plt.ylabel("Virginica Iris Petal Length")
plt.title("Iris-Versicolor Petal Width Vs Iris-Virginica Petal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.versicolorpw, data.virginicapw,  "mo" ,  marker = "o" )
plt.xlabel("Versicolor Iris Petal Width")
plt.ylabel("Virginica Iris Petal Width")
plt.title("Iris-Versicolor Petal Width Vs Iris-Virginica Petal Width")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.virginicasw, data.virginicasl,  "mo" ,  marker = "o" )
plt.xlabel("Virginica Iris Sepal Width")
plt.ylabel("Virginica Iris Sepal Length")
plt.title("Iris-Versicolor Sepal Width Vs Iris-Virginica Sepal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.virginicasw, data.virginicapl,  "mo" ,  marker = "o" )
plt.xlabel("Virginica Iris Sepal width")
plt.ylabel("Virginica Iris Petal Length")
plt.title("Iris-Versicolor Sepal Width Vs Iris-Virginica Petal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.virginicasw, data.virginicapw,  "mo" ,  marker = "o")
plt.xlabel("Virginica Iris Sepal Length")
plt.ylabel("Virginica Iris Petal Width")
plt.title("Iris-Versicolor Sepal Width Vs Iris-Virginica Petal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.virginicasl, data.virginicapl,  "mo" ,  marker = "o" )
plt.xlabel("Virginica Iris Sepal Length")
plt.ylabel("Virginica Iris Petal Length")
plt.title("Iris-Versicolor Sepal Length Vs Iris-Virginica Petal Length")
plt.show()

plt.figure(figsize = (15,5))
plt.plot(data.virginicasl, data.virginicapw,  "mo" ,  marker = "o" )
plt.xlabel("Virginica Iris Sepal Length")
plt.ylabel("Virginica Iris Petal Width")
plt.title("Iris-Versicolor Sepal Length Vs Iris-Virginica Petal Width")
plt.show()


plt.figure(figsize = (15,5))
plt.plot(data.virginicapl, data.virginicapw,  "mo" ,  marker = "o" )
plt.xlabel("Virginica Iris Petal Length")
plt.ylabel("Virginica Iris Petal Width")
plt.title("Iris-Versicolor Petal Length Vs Iris-Virginica Petal Width")
plt.show()

#references
#https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.figure.html
#https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
#https://www.mathworks.com/matlabcentral/answers/122388-how-would-i-open-multiple-figures-from-one-script
#https://www.youtube.com/watch?v=UO98lJQ3QGI&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_
#https://www.tutorialspoint.com/python_pandas/python_pandas_descriptive_statistics.htm
#http://www.datasciencemadesimple.com/descriptive-summary-statistics-python-pandas/


