#!/usr/bin/env python
import subprocess
import sys
import csv

def main():
        hostname = sys.argv[1]
        cmd = ['fping', '-g', hostname]
	former, sys.stdout = sys.stdout, open('output.csv', 'w+')
        with open('output.csv', 'w+') as out:
   		subprocess.call(cmd, stdout=out)
        with open('output.csv', 'r') as inp:
                for line in inp:
                	print line.replace("is","").replace("unreachable","free").replace("alive","use").replace("  "," ").replace(" ",",")
	results,sys.stdout = sys.stdout, former
        results.close()

if __name__ == '__main__':
        main() 
