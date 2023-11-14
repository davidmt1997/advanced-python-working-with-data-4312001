# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print(f"Total earthquakes {len(data['features'])}")
quakes_felt = (quake['properties']['felt'] is not None and quake['properties']['felt'] >= 100 
          for quake in data['features'])
print(sum(quakes_felt))


def sortFelt(quake):
    num_felt = quake["properties"]["felt"]
    if num_felt == None:
        return 0
    return float(num_felt)

max_quake = max(data['features'], key=sortFelt)
print(max_quake["properties"]["place"], max_quake["properties"]["felt"])

def sortSig(quake):
    sig = quake["properties"]["sig"]
    if sig is None:
        return 0
    return float(sig)

data['features'].sort(key=sortSig, reverse=True)

for i in range(10):
    print(f"""{data['features'][i]["properties"]["place"]}: {data['features'][i]["properties"]["felt"]}""")
