import argparse
import client

parser = argparse.ArgumentParser()

parser.add_argument("--input", "-i", type=str, required=True)
parser.add_argument("--output", "-o", type=str, required=True)
args = parser.parse_args()

inputFile = open(args.input, 'r')
outputFile = open(args.output, 'w')

for subdomain in inputFile:
    response = client.query(subdomain, "CNAME")

    if len(response) == 0:
        print(f"{subdomain}: No records.")
    else:
        outputFile.write(f"{subdomain}:{response[0]}")
        print(f"{subdomain}:{response[0]}")

print('Done.')