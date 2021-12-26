from resolvers import cloudflare, google
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", "-i", type=str, required=True)
parser.add_argument("--output", "-o", type=str, required=True)
parser.add_argument("--resolver", "-r", type=str, required=True)
args = parser.parse_args()

inputFile = open(args.input, 'r')
outputFile = open(args.output, 'w')

for subdomain in inputFile:
    if args.resolver == "google":
        data = google(subdomain, "CNAME")

        if "Authority" in data:
            print(f"{subdomain}: No records")
        elif "Authority" in data:
            outputFile.write(f"{subdomain}:{data['Answer'][0]['data']}")
            print(f"{subdomain}:{data['Answer'][0]['data']}")
        else:
            print("Unknown response.")
    elif args.resolver == "cloudflare":
        data = cloudflare(subdomain, "CNAME")

        if "Authority" in data:
            print(f"{subdomain}: No records")
        elif "Answer" in data:
            outputFile.write(f"{subdomain}:{data['Answer'][0]['data']}")
            print(f"{subdomain}:{data['Answer'][0]['data']}")
        else:
            print("Unknown response.")
    else:
        print("Unknown resolver.")
        exit()

print('Done.')