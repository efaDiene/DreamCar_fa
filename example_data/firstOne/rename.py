import os

for filename in os.listdir("."):
    print(filename)
    if filename.startswith("FRONT_RIGHT_"):
        os.rename(filename, filename[12:])