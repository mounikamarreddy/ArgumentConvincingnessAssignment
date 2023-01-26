import pandas as pd
import os

df = pd.read_csv("total.csv",sep="\t")

count  = 0
c5 = 0
c6 = 0
c7 = 0

for i in range(len(df)):
    labels = []
    for item in df["Labels"][i].split(","):
        labels.append(item.split("_")[0])
    cnt = 0
    f5 = 0
    f6 = 0
    f7 = 0
    l = [0,0,0]
    if "o5" in labels:
        cnt += 1
        l[0] = labels.count("o5")
        f5 = 1
    if "o6" in labels:
        cnt += 1
        l[1]  = labels.count("o6")
        f6 = 1
    if "o7" in labels:
        cnt += 1
        l[2] = labels.count("o7")
        f7 = 1
    if cnt == 1 and f5 == 1 and l[0] == 1:
        df["Labels"][i] = "o5"
        c5 += 1
        continue
    elif cnt == 1 and f6 == 1 and l[1] == 1:
        df["Labels"][i] = "o6"
        c6 += 1
        continue
    elif cnt == 1 and f7 == 1 and l[2] == 1:
        df["Labels"][i] = "o7"
        c7 += 1
        continue
    else:
        df.drop(i,inplace=True, axis="index")
print(c5,c6,c7)
df.to_csv("train.csv",sep="\t")