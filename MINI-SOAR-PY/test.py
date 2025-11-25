import os 
import json
import sys

def main():
    for i in range(1, 11):
        if i < len(sys.argv):
            print(sys.argv[i])
    

if __name__ == "__main__":
    main()