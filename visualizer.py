# where the data in the db turns into something visual
# each team is one of the three numbers for an RGB code
# divide team number by 24.5 to get the value for RGB
# create data point on Y-axis of score value
# red is positive, blue is negative
# X-axis is matches in numerical order
# each match is two "units" wide
# create triangle to data point of match score
# colors created by alliance are the fill for each triangle
import sqlite3


db = sqlite3.connect("localhost","testuser","test123","match_information" )

cursor = db.cursor()

cursor.execute("SELECT red_one()")

data = cursor.fetchone()

db.close()
