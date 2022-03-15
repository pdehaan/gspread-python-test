import csv
import gspread

gc = gspread.service_account()

# Open a sheet from a spreadsheet in one go
# https://docs.google.com/spreadsheets/d/1JqMThnZHBcKVs3GcmfD6r-FcDXhP8Tzl_kgfRrxydAc/edit#gid=0
wks = gc.open("gspread test sheet").sheet1

with open("locust.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["Name"] == "Aggregated":
            # Convert Dict to List
            values = list(row.values())
            wks.append_row(values)
