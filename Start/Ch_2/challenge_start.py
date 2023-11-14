# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter
from collections import defaultdict

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


# using counter
types = list(quake["properties"]["type"] for quake in data["features"])

c1 = Counter(types)
for key, val in c1.items():
    print(f"{key}: {val}")

# using default dict
totals = defaultdict(int)

for quake in data["features"]:
    totals[quake["properties"]["type"]] += 1

for key, val in totals.items():
    print(f"{key}: {val}")