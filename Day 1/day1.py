"""
We are gonna create a model about properties for sale in Bogotá, Colombia
and how their prices are choosen.

"""
import pandas as pd

data=pd.read_csv(r"C:\Users\Emmanuel\OneDrive - Instituto Politecnico Nacional\GITHUB\Inmersion-datos-aiura-Latam\Inmersion-datos-Aiura-LATAM\Day 1\inmuebles_bogota.csv")
print(data.info()) #gives a table with the name of columns,
# number of empty values
# types of the columns
print(data.head()) # First 5 rows, if you put a number into brackets, gives that number
#of rows
print(data.tail()) # Last 5 rows, same as head with brackets
print(data.sample(10)) #Gives 10 random rows from the dataset
print(data.columns) #gives an object type
print(data.columns.values.tolist())# gives the name values in a list 

#To change some column values, you can create a dictionary
# key = actual column name
# value = new column name

cols={
    "Baños":"Banos",
    "Área":"Area"
}

data.rename(cols, axis=1, inplace=True) #My favorite way to rewrite column names
#Another way to rewrite column names
data=data.rename(columns=cols)#Will give the same result as the function above


#functions
#attributes
#variables
#strings
