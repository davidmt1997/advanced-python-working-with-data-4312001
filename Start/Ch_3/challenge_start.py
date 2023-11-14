# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
def getSig(quake):
    sig = quake["properties"]["sig"]
    if sig is None:
        return 0
    return float(sig)

def getDate(quake):
    date = quake["properties"]["time"]
    return date

significant_events = sorted(data["features"], key=getSig, reverse=True)
significant_events = significant_events[:40]
significant_events.sort(key= lambda x: x["properties"]["time"], reverse=True)
header = ["Magnitude", "Place", "Felt reports", "Date", "Google Maps Link"]
rows = []

for event in significant_events:
    thedate = datetime.date.fromtimestamp(
        int(event["properties"]["time"]) / 1000)
    lat = event["geometry"]["coordinates"][1]
    long = event["geometry"]["coordinates"][0]
    gmaplink = f"https://maps.google.com/maps/search/?api=1&query={lat}%2C{long}"

    rows.append([event["properties"]["mag"],
                event["properties"]["place"],
                0 if event["properties"]["felt"] is None else event["properties"]["felt"],
                thedate,
                gmaplink])    
with open('significant_quakes.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)