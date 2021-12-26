from resolvers import cloudflare, google
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", "-i", type=str, required=True)
parser.add_argument("--output", "-o", type=str, required=True)
parser.add_argument("--resolver", "-r", type=str, required=True)
args = parser.parse_args()

inputFile = open(args.input, 'r')
outputFile = open(args.output, 'w')

for line in inputFile:
    strippedLine = line.strip()
    if args.resolver == "google":
        data = google(strippedLine, "CNAME")

        if "Authority" in data:
            print(f"{strippedLine}: No records")
        elif "Answer" in data:
            outputFile.write(f"{strippedLine}:{data['Answer'][0]['data']}\n")
            print(f"{strippedLine}:{data['Answer'][0]['data']}")
        else:
            print(f"Unknown response.")
    elif args.resolver == "cloudflare":
        data = cloudflare(strippedLine, "CNAME")

        if "Authority" in data:
            print(f"{strippedLine}: No records")
        elif "Answer" in data:
            outputFile.write(f"{strippedLine}:{data['Answer'][0]['data']}\n")
            print(f"{strippedLine}:{data['Answer'][0]['data']}")
        else:
            print(f"Unknown response.")
    else:
        print("Unknown resolver.")
        exit()

print('Done.')