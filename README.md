# Argument Convincingness Assignment

1. The initial step is to preprocess the data to the required form. To filter out rows that are classified under a single label of either "C5", "C6", or "C7", I have selected rows that have only one of the labels. 
* "parse.py" file parses all the 16 debates CSV files in the data/CSV-format folder and gives a final CSV file consisting of 9112 rows. 
* "prepare.py" then filters out rows accordingly, as mentioned in the 4.2 section of the paper, and then stores in train.csv, which is then further used by the model to train the classifier. 
* The "train.csv" file contains the data with "C5", "C6", and "C7" labels. 

2. The BERT-base fine-tuning details, hyper-parameter selection, and the number of epochs are mentioned in the attached "FineTuneBERT_ArgumentConvincingness.ipynb" notebook. The task1 solution and its alternatives are explained in the attached document "Task1_SolutionDocument.PDF".

3. The task2 scientific review is in the attached document "Task2_ScientificReview.PDF".
