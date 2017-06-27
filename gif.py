#!/bin/python3

import sys
import datetime
import time
import imageio
import MySQLdb

startTime = time.time()

db = MySQLdb.connect(host="localhost",
                     user="root",
                     db="gif_creator")       


def create_gif(duration, pictures):
    images = []
    for picture in pictures:
        snap = imageio.imread(picture)
        images.append(snap)
    output_file = "gif-%s.gif" % datetime.datetime.now().strftime("%d.%m.%Y-%H:%M")
    imageio.mimwrite(output_file, images, duration = duration)
    
if __name__ == "__main__":
    script = sys.argv.pop(0)
    formats = ("png", "jpg", "tiff", "bmp")

    if len(sys.argv) < 2:
        print("Instructions: python {} <duration of each image> <path to images separated by space>".format(script))
        sys.exit(1)

    duration = float(sys.argv.pop(0))
    pictures = sys.argv


    if not all(picture.lower().endswith(formats) for picture in pictures):
        print("Please use only images.")
        sys.exit(1)

    create_gif(duration, pictures)
    creation_duration = time.time() - startTime
    print("The creation of the gif took {} seconds".format(creation_duration))
    sql = "INSERT INTO gifs (duration) VALUES (%d)" % (creation_duration) 
    cursor = db.cursor()

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
