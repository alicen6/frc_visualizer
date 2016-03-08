import sqlite3
from PIL import Image, ImageDraw


sqlite_file = '/Users/alicen/git/frc_visualizer/db.sqlite3'
table_name = 'match_information'
id_column = 'id'
shorthand = 'shorthand'
red_one = 'red_one'
red_two = 'red_two'
red_three = 'red_three'
blue_one = 'blue_one'
blue_two = 'blue_two'
blue_three = 'blue_three'
red_score = 'red_score'
blue_score = 'blue_score'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('SELECT * FROM {tn} WHERE shorthand ="2016waspo"'.
          format(tn=table_name, r1=red_one))
all_rows = c.fetchall()

width = len(all_rows) * 30
print len(all_rows)
height = 650
image = Image.new('RGB', (width, height), "white")
image_two = Image.new('RGB', (width, height), "white")
first_x_point = 0
second_x_point = 15
third_x_point = 30

for entry in all_rows:
    red_red = int(entry[1] / 24.5)
    blue_red = int(entry[2] / 24.5)
    green_red = int(entry[3] / 24.5)

    red_blue = int(entry[4] / 24.5)
    blue_blue = int(entry[5] / 24.5)
    green_blue = int(entry[6] / 24.5)

    red_score = entry[7]
    blue_score = entry[8]

    red_value = 325 - (int(red_score) * 3)
    blue_value = 325 + (int(blue_score) * 3)

    draw = ImageDraw.Draw(image)
    draw.polygon([(first_x_point, 325), (second_x_point, red_value),
                  (third_x_point, 325)], fill=(red_red, blue_red, green_red))
    draw.polygon([(first_x_point, 325), (second_x_point, blue_value),
                  (third_x_point, 325)], fill=(red_blue, blue_blue, green_blue))
    draw_two = ImageDraw.Draw(image_two)
    draw_two.polygon([(first_x_point, 325), (first_x_point, red_value),
                      (third_x_point, red_value), (third_x_point, 325)], fill=(red_red, blue_red, green_red))
    draw_two.polygon([(first_x_point, 325), (first_x_point, blue_value),
                      (third_x_point, blue_value), (third_x_point, 325)], fill=(red_blue, blue_blue, green_blue))
    first_x_point += 30
    second_x_point += 30
    third_x_point += 30
image.show()
image_two.show()
image.save("2016waspo.jpeg", "JPEG")
image_two.save("2016waspo2.jpeg", "JPEG")
