from dotenv import load_dotenv
import requests
import argparse
import os

load_dotenv()

parser = argparse.ArgumentParser()

parser.add_argument("--program", "-p", required=True)
parser.add_argument("--output", "-o", required=True)
args = parser.parse_args()

outputFile = open('output.txt', 'w')

BASE_URL = "https://api.hackerone.com/v1/hackers/programs/"

auth = (os.getenv("H1_USERNAME"), os.getenv("H1_KEY"))

headers = {
    "Accept": "application/json"
}

response = requests.get(f"{BASE_URL}{args.program}", auth=auth, headers=headers)

unfiltered = response.json()["relationships"]["structured_scopes"]["data"]
filtered = [item for item in unfiltered if item["attributes"]["asset_type"]]

for scope in filtered:
    outputFile.write(f"{scope['attributes']['asset_identifier']}\n")

print("Done.")