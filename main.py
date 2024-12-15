from spotify import RUN_SPOTIFY
from youtube import search_youtube
from youtify import search_youtube as sy
import csv
try:
    path = RUN_SPOTIFY()
    # path = "shdak.csv"
    print("/" + path)

    with open(path, 'r',encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row[0])
            if row[0].startswith(",") or row[0].startswith(" ") or row[0] == "" or row[0] == None:
                # print("Skipping...")
                continue
            try:
                search_youtube(row[0], row[1])
                print("Method failed try another method...")
            except:
                links = sy(row[0], row[1])
                # ! Print the links
                # print(links)
            # sy(row[0], row[1])
except KeyboardInterrupt:
    print("Keyboard Interrupted")
except Exception as e:
    print(e)
    print("Error Occured")