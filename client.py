import csv
from app import predict

# Read CSV and convert to dictionary
with open("data/future_unseen_examples.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # Reads each row as a dict
    data_list = [row for row in reader]  # List of dictionaries

# Example: pass the first row to a function


res = predict(data_list[0])
print(res)