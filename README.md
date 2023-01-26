# Argument Convincingness Assignment

1. The initial step is to preprocess the data to the required form. To filter out rows which are classified under single label of either "o5","o6","o7" , I have selected rows which have only one of the labels. 
parse.py parses all the csv files in the data/CSV-format folder and then gives a final csv file consisting of 9112 rows. 
prepare.py then filters out rows accordingly as mentioned in the 4.2 section of the paper and then stores in train.csv, which is then further used by the models to train the classifiers.
