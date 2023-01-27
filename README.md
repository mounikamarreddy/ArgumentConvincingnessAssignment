# Argument Convincingness Assignment

1. The initial step is to preprocess the data to the required form. To filter out rows which are classified under single label of either "C5","C6","C7" , I have selected rows which have only one of the labels. 
"parse.py" file parses all the csv files in the data/CSV-format folder and then gives a final csv file consisting of 9112 rows. 
"prepare.py" then filters out rows accordingly as mentioned in the 4.2 section of the paper and then stores in train.csv, which is then further used by the models to train the classifiers. 
The "train.csv" file contains the data with "C5", "C6", and "C7" labels. 

2. I applied BERT on the "train.csv" data. The explanation of code and visualizations are mentioned clearly in the attached "FineTuneBERT_ArgumentConvincingness.ipynb" notebook. The task1 solution and its alternatives are explained in the attached document "DOCNAME and Attach".

3. The task2 scientific review is present in the attached document "DOCNAME and Attach".
