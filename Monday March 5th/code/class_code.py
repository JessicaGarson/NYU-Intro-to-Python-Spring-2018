schools = {
    "geometry": {
        "coordinates": [
            -81.50572799999999,
            39.21675500000001
        ],
        "type": "Point"
    },
    "properties": {
        "address": "300 Campus Drive, Parkersburg, WV 26104",
        "marker-color": "#3F3040",
        "marker-symbol": "circle",
        "name": "West Virginia University at Parkersburg"
    },
    "type": "Feature"
}


# Question 1:  How can we get a dictionary with the key of "coordinates" and a value containing a list of two decimal numbers?

geometry = schools['geometry']['coordinates']
print(geometry)
print(coordinates)

# Question 2: How can we get address of the school?
address = schools['properties']['address']
print(address)

# Question 3: How can we get name of the school?

print(schools['properties']['name'])

# Question 4: How can we get the latitude of the school?
latitude = schools ['geometry']['coordinates'][0]
print(latitude)

# Question 5 (bonus): How can we get the marker-color without the hashtag in front?

marker = schools ['properties']['marker-color'][1:]
print(marker)
