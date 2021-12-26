import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", "-i", type=str, required=True)
parser.add_argument("--output", "-o", type=str, required=True)
args = parser.parse_args()

inputFile = open(args.input, 'r')
outputFile = open(args.output, 'w')

print('Done.')