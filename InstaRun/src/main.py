from sys import *
import os

def run():
    data = argv[1]
    os.system("sand run " + data)
    print("\n\nFinished!")
    os.system("pause")

run()