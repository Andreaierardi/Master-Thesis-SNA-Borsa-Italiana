

import os
import pandas as pd

dirs = os.listdir()

instr_dict = dict()
for f in dirs:
    if f!= "get_mean.py":
        print(f)
        file = open(f,"r")
        for lines in file:
            for l in lines.split("\n"):
                if "Number of nodes" in l or "======" in l:
                   # print(l)
                    print(l.split("  - ")[0].split("=")[-1])
#                    instr_dict[]


#            print(line)
#print(dirs)
#file = open("","r")àà
#def get_results_mean(file):