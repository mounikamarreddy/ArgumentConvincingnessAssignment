import pandas as pd
import glob
import os

files = glob.glob("./data/CSV-format/"+ "/*.csv")

pairid = []
labels = []
arg1 = []
arg2 = []

for file in files:
    df = pd.read_csv(file, delimiter="\t",header=None)
    for i in range(len(df)):
        pairid.append(df[0][i])
        labels.append(df[1][i])
        arg1.append(df[2][i])
        arg2.append(df[3][i])

list_of_tuples = list(zip(pairid, labels,arg1,arg2))
df = pd.DataFrame(list_of_tuples, columns = ['pair ID', 'Labels', 'Argument 1','Argument 2'])
df.to_csv("total.csv",sep="\t")







