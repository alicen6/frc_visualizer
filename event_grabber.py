import sqlite3 as lite
import os
from bs4 import BeautifulSoup
import requests


def save_to_database():

    con = lite.connect('/Users/alicen/git/frc_visualizer/db.sqlite3')

    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS match_information(
            id INTEGER PRIMARY KEY, red_one INT,
                red_two INT, red_three INT,
                blue_one INT, blue_two INT,
                blue_three INT, red_score INT,
                blue_score INT, shorthand TEXT);
    """)
    cur.close()

    base_url = "http://www.thebluealliance.com/event/"  # THIS IS REAL
    for folder_name in os.listdir("."):
        if os.path.isdir(folder_name) and folder_name.startswith("2"):
            url = base_url + folder_name
            print folder_name, url

            # url = "http://www.thebluealliance.com/event/2016week0"  # THIS IS ONLY FOR DEVELOPING

            resp = requests.get(url=url)
            data = resp.content
            soup = BeautifulSoup(data, "html.parser")
            texts = soup.findAll("table", class_="match-table")
            if len(texts) > 0:
                rows = texts[0].findChildren(['th', 'tr'])
                if len(rows) > 50:
                    for row in rows:
                        try:
                            visible = dict(row.attrs)["class"]
                        except:
                            pass
                        if "visible"in visible[0]:
                            # print row
                            cells = row.findChildren('td')
                            print cells[1].string  # Qual
                            scores = {}
                            for cell in range(len(cells)):
                                # value = cells[cell].string  # cells is a list; cell
                                # is an int
                                try:
                                    classes = dict(cells[cell].attrs)["class"]
                                    if "red" in classes[0] and cell == 2:
                                        scores["red_one"] = cells[2].string
                                        print scores["red_one"]
                                        # write the team into db here
                                    elif "red" in classes[0] and cell == 3:
                                        scores["red_two"] = cells[3].string
                                        print scores["red_two"]
                                    elif "red" in classes[0] and cell == 4:
                                        scores["red_three"] = cells[4].string
                                        print scores["red_three"]
                                        pass
                                    elif "blue" in classes[0] and cell == 5:
                                        scores["blue_one"] = cells[5].string
                                        print scores["blue_one"]
                                    elif "blue" in classes[0] and cell == 6:
                                        scores["blue_two"] = cells[6].string
                                        print scores["blue_two"]
                                    elif "blue" in classes[0] and cell == 7:
                                        scores["blue_three"] = cells[7].string
                                        print scores["blue_three"]
                                        # write the team into db here
                                        pass
                                    elif "red" in classes[0] and cell == 8:
                                        scores["red_score"] = cells[8].string
                                        print scores["red_score"]
                                        # write the score into db here
                                    elif "blue" in classes[0] and cell == 9:
                                        scores["blue_score"] = cells[9].string
                                        print scores["blue_score"]
                                        # write the score into db here
                                except KeyError:
                                    pass
                            cur = con.cursor()
                            cur.execute("""
                                INSERT INTO match_information(
                                    id, red_one, red_two, red_three,
                                    blue_one, blue_two, blue_three,
                                    red_score, blue_score, shorthand)
                                        VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                            """, [scores["red_one"], scores["red_two"], scores["red_three"],
                                  scores["blue_one"], scores["blue_two"], scores["blue_three"],
                                  scores["red_score"], scores["blue_score"], folder_name])
                            cur.close()
                            con.commit()


if __name__ == "__main__":
    save_to_database()
