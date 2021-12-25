import requests
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("--program", "-p", required=True)
parser.add_argument("--output", "-o", required=True)

args = parser.parse_args()

BASE_URL = "https://api.hackerone.com/"
H1_KEY = os.environ.get("H1_KEY")

headers = {
    "Accept": "application/json"
}

response = requests.get('')