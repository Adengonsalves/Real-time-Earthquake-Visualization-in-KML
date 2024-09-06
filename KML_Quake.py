import pandas as pd


def create_placemark(place,mag,latitude,longitude,time):
    return f'''
    <Placemark>
        <name>{place}</name>
        <description>
            &lt;h1&gt;{mag} Magnitude earthquake at {time}&lt;/h1&gt;
        </description>
        <Point>
            <coordinates>{latitude},{longitude}</coordinates>
        </Point>
    </Placemark>
    '''
myDict = {}

# URL pointing to the CSV file
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'

# Reading the CSV file from the URL
df = pd.read_csv(url)

kml = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
'''


for index, row in df.iterrows():
    myDict[row['place']] = list = [row['latitude'], row['longitude']]
    kml += create_placemark(row['place'],row['mag'],row['longitude'],row['latitude'],row['time'])

kml += '''
    </Document>
</kml>
'''

# Write the KML to a file
with open('testing.kml', 'w') as file:
    file.write(kml.strip())  # Using strip() to remove any leading/trailing whitespace
