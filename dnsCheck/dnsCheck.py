import dns.resolver
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("--input", "-i", type=str, required=True)
parser.add_argument("--output", "-o", type=str, required=True)
args = parser.parse_args()

inputFile = open(args.input, 'r')
outputFile = open(args.output, 'w')

for subdomain in inputFile:
    try:
        answers = dns.resolver.resolve(subdomain, 'CNAME')
        for rdata in answers:
            outputFile.write(f"{subdomain}:{rdata}")
    except dns.resolver.NoAnswer:
        pass

print('Done.')