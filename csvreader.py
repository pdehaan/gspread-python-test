import csv

with open("locust.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["Name"] == "Aggregated":
            print(list(row.values()))
