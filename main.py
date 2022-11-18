from time import sleep
from datetime import datetime
import sys
import requests

def displayHelp():
  print("Usage: python3 ./main.py <webpage / api> <out file> [interval]")
  exit()

def writeToFile(fileName, contents):
  with open(fileName, "a") as file:
    file.writelines(contents)
    file.close()

def fetchData(apiPath, filePath, interval):
  print("Started Data Miner")
  print(f"\tWebpage: {apiPath}")
  print(f"\tOut File: {filePath}")
  print(f"\tInterval: {interval}\n")

  while True:
    # write the state of the API to a file
    apiState = requests.get(apiPath)
    writeToFile(filePath, f"{apiState.text}\n")

    now = datetime.now()
    printOutDate = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"{printOutDate}: Took Recoding")

    # sleep for a predetermined amount of time
    sleep(int(interval))

def main():
  apiPath = None
  filePath = None
  interval = 900

  try:
    apiPath = sys.argv[1]
    filePath = sys.argv[2]

    if len(sys.argv) > 3:
      interval = sys.argv[3]
  except:
    displayHelp()

  if apiPath == None or filePath == None or apiPath == "--help":
    displayHelp()

  fetchData(apiPath, filePath, interval)

main()
