
import csv
import matplotlib.pyplot as plt
import scipy
import numpy as np
import json
from collections import defaultdict
city_names = ["Aberdeen", "Abilene", "Akron", "Albany", "Albuquerque", "Alexandria", "Allentown", "Amarillo", "Anaheim", "Anchorage", "Ann Arbor", "Antioch", "Apple Valley", "Appleton", "Arlington", "Arvada", "Asheville", "Athens", "Atlanta", "Atlantic City", "Augusta", "Aurora", "Austin", "Bakersfield", "Baltimore", "Barnstable", "Baton Rouge", "Beaumont", "Bel Air", "Bellevue", "Berkeley", "Bethlehem", "Billings", "Birmingham", "Bloomington", "Boise", "Boise City", "Bonita Springs", "Boston", "Boulder", "Bradenton", "Bremerton", "Bridgeport", "Brighton", "Brownsville", "Bryan", "Buffalo", "Burbank", "Burlington", "Cambridge", "Canton", "Cape Coral", "Carrollton", "Cary", "Cathedral City", "Cedar Rapids", "Champaign", "Chandler", "Charleston", "Charlotte", "Chattanooga", "Chesapeake", "Chicago", "Chula Vista", "Cincinnati", "Clarke County", "Clarksville", "Clearwater", "Cleveland", "College Station", "Colorado Springs", "Columbia", "Columbus", "Concord", "Coral Springs", "Corona", "Corpus Christi", "Costa Mesa", "Dallas", "Daly City", "Danbury", "Davenport", "Davidson County", "Dayton", "Daytona Beach", "Deltona", "Denton", "Denver", "Des Moines", "Detroit", "Downey", "Duluth", "Durham", "El Monte", "El Paso", "Elizabeth", "Elk Grove", "Elkhart", "Erie", "Escondido", "Eugene", "Evansville", "Fairfield", "Fargo", "Fayetteville", "Fitchburg", "Flint", "Fontana", "Fort Collins", "Fort Lauderdale", "Fort Smith", "Fort Walton Beach", "Fort Wayne", "Fort Worth", "Frederick", "Fremont", "Fresno", "Fullerton", "Gainesville", "Garden Grove", "Garland", "Gastonia", "Gilbert", "Glendale", "Grand Prairie", "Grand Rapids", "Grayslake", "Green Bay", "GreenBay", "Greensboro", "Greenville", "Gulfport-Biloxi", "Hagerstown", "Hampton", "Harlingen", "Harrisburg", "Hartford", "Havre de Grace", "Hayward", "Hemet", "Henderson", "Hesperia", "Hialeah", "Hickory", "High Point", "Hollywood", "Honolulu", "Houma", "Houston", "Howell", "Huntington", "Huntington Beach", "Huntsville", "Independence", "Indianapolis", "Inglewood", "Irvine", "Irving", "Jackson", "Jacksonville", "Jefferson", "Jersey City", "Johnson City", "Joliet", "Kailua", "Kalamazoo", "Kaneohe", "Kansas City", "Kennewick", "Kenosha", "Killeen", "Kissimmee", "Knoxville", "Lacey", "Lafayette", "Lake Charles", "Lakeland", "Lakewood", "Lancaster", "Lansing", "Laredo", "Las Cruces", "Las Vegas", "Layton", "Leominster", "Lewisville", "Lexington", "Lincoln", "Little Rock", "Long Beach", "Lorain", "Los Angeles", "Louisville", "Lowell", "Lubbock", "Macon", "Madison", "Manchester", "Marina", "Marysville", "McAllen", "McHenry", "Medford", "Melbourne", "Memphis", "Merced", "Mesa", "Mesquite", "Miami", "Milwaukee", "Minneapolis", "Miramar", "Mission Viejo", "Mobile", "Modesto", "Monroe", "Monterey", "Montgomery", "Moreno Valley", "Murfreesboro", "Murrieta", "Muskegon", "Myrtle Beach", "Naperville", "Naples", "Nashua", "Nashville", "New Bedford", "New Haven", "New London", "New Orleans", "New York", "New York City", "Newark", "Newburgh", "Newport News", "Norfolk", "Normal", "Norman", "North Charleston", "North Las Vegas", "North Port", "Norwalk", "Norwich", "Oakland", "Ocala", "Oceanside", "Odessa", "Ogden", "Oklahoma City", "Olathe", "Olympia", "Omaha", "Ontario", "Orange", "Orem", "Orlando", "Overland Park", "Oxnard", "Palm Bay", "Palm Springs", "Palmdale", "Panama City", "Pasadena", "Paterson", "Pembroke Pines", "Pensacola", "Peoria", "Philadelphia", "Phoenix", "Pittsburgh", "Plano", "Pomona", "Pompano Beach", "Port Arthur", "Port Orange", "Port Saint Lucie", "Port St. Lucie", "Portland", "Portsmouth", "Poughkeepsie", "Providence", "Provo", "Pueblo", "Punta Gorda", "Racine", "Raleigh", "Rancho Cucamonga", "Reading", "Redding", "Reno", "Richland", "Richmond", "Richmond County", "Riverside", "Roanoke", "Rochester", "Rockford", "Roseville", "Round Lake Beach", "Sacramento", "Saginaw", "Saint Louis", "Saint Paul", "Saint Petersburg", "Salem", "Salinas", "Salt Lake City", "San Antonio", "San Bernardino", "San Buenaventura", "San Diego", "San Francisco", "San Jose", "Santa Ana", "Santa Barbara", "Santa Clara", "Santa Clarita", "Santa Cruz", "Santa Maria", "Santa Rosa", "Sarasota", "Savannah", "Scottsdale", "Scranton", "Seaside", "Seattle", "Sebastian", "Shreveport", "Simi Valley", "Sioux City", "Sioux Falls", "South Bend", "South Lyon", "Spartanburg", "Spokane", "Springdale", "Springfield", "St. Louis", "St. Paul", "St. Petersburg", "Stamford", "Sterling Heights", "Stockton", "Sunnyvale", "Syracuse", "Tacoma", "Tallahassee", "Tampa", "Temecula", "Tempe", "Thornton", "Thousand Oaks", "Toledo", "Topeka", "Torrance", "Trenton", "Tucson", "Tulsa", "Tuscaloosa", "Tyler", "Utica", "Vallejo", "Vancouver", "Vero Beach", "Victorville", "Virginia Beach", "Visalia", "Waco", "Warren", "Washington", "Waterbury", "Waterloo", "West Covina", "West Valley City", "Westminster", "Wichita", "Wilmington", "Winston", "Winter Haven", "Worcester", "Yakima", "Yonkers", "York", "Youngstown"]

with open("carbon.csv") as carbon:
    reader = csv.reader(carbon, delimiter = ",", quotechar = '"')
    data_carbon = {}
    for row in reader:
        if row[1] == "United States" and row[0] not in data_carbon:
            data_carbon[row[0]] = [0, 0, 0]
        if row[1] == "United States" and "2019" in row[2]:
            data_carbon[row[0]][0] = data_carbon.get(row[0], [0,0,0])[0] + float(row[4])

        if row[1] == "United States" and "2020" in row[2]:
            data_carbon[row[0]][1] = data_carbon.get(row[0], [0,0,0])[1] + float(row[4])

        if row[1] == "United States" and "2021" in row[2]:
            data_carbon[row[0]][2] = data_carbon.get(row[0], [0,0,0])[2] + float(row[4])

x_label = []
x = []
y = []

a = []

counties= {}

with open("county.csv") as county:
    reader = csv.reader(county, delimiter = ",", quotechar = '"')
    for row in reader:
        counties[row[1]] = [a.lower() for a in row[7].split(", ")]

counties["New York"] = ["Bronx County", "Kings County", "New York County", "Queens County", "Richmond County"]
counties["Houston"] = ["Harris County"]

with open("trans.json") as f:
    data = {a.split(",")[0].strip(): b for a, b in json.load(f).items()}

x_lists = {}
trans_data = defaultdict(list)

def merge(t_list):
    output = {}
    for t in t_list:
        for cat in t:
            if cat not in output:
                output[cat] = {}
            for field in t[cat]:
                if field in output[cat]:
                    output[cat][field] += float(t[cat][field])
                else:
                    output[cat][field] = float(t[cat][field])

    return output
x_label = []
with open("solar.csv") as solar:
    reader = csv.reader(solar, delimiter = ",", quotechar = '"')
    for row in reader:
        if row[1] not in data_carbon:
            print(row[1])

        else:
            if row[4] == "N/A":
                continue
            city = row[1]

            if "(" in city:
                 city = city.split("(")[0].strip()

            for county in counties[city]:
                if county.title() == "N/A":
                    continue
                trans_data[city.lower()].append(data[county.title()])

            merged_t = merge(trans_data[city.lower()])
            added = False
            for category in merged_t:
                if category not in x_lists:
                    x_lists[category] = {}
                for field in merged_t[category]:
                    if field not in x_lists[category]:
                        x_lists[category][field] = []
                    added = True
                    x_lists[category][field].append(merged_t[category][field])

            if added:
                x_label.append(row[1].title())
                y.append(data_carbon[row[1]][0])

#print(json.dumps(x_lists, indent=4))

print(x_label)

a = []

d = []
label = []
height = []
for category in x_lists:
    for field in x_lists[category]:
        a.append(field)
        x = x_lists[category][field]
        if field == "Trips less than 1 mile":
            fig, ax = plt.subplots()
            ax.scatter(x, y)
            
            for i, txt in enumerate(x_label):
                ax.annotate(txt, (x[i], y[i]))
            m, b, r_value, p_value, std_err = scipy.stats.linregress(x, y)
            
            ax.plot(x, m*np.array(x)+ b)
            print('r^2: ' + str("{:.2f}".format(r_value**2)))
            plt.show()
        m, b, r_value, p_value, std_err = scipy.stats.linregress(x, y)
        d.append((field, r_value**2))
        print(field + 'r^2: ' + ("-" if m < 0 else "") + str("{:.2f}".format(r_value**2)))

#plt.xticks(rotation=45, ha="right")
# print(d)
d.sort(key=lambda m: m[1])
d = [a for a in d if "Hispanic" not in a[0]]
label = [a[0] for a in d]
height = [a[1] for a in d]
# print(label, height)
fig, ax = plt.subplots(figsize=(8,8))
plt.subplots_adjust(left=0.5)
bars = plt.barh(label, height)

ax.spines[['right', 'top', 'bottom']].set_visible(False) 
# ax.xaxis.set_visible(False)

# ax.bar_label(bars, fmt="%.2f")
plt.show()
# print(a)
