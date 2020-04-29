import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Data.csv")
plt.plot( data.setosapl,  "mo" ,  marker = "o" ,Label= "Iris-Setosa")
plt.plot( data.versicolorpl , "bo" , marker = "o", Label = "Iris-Veriscolor" )
plt.plot( data.virginicapl, "ro", Label = "Iris-Virginca", marker = "o"  )
plt.legend()
plt.xlabel("Petal Length")
plt.title("Petal Length ")

plt.savefig("histogram.png")

