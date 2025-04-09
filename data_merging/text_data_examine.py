import os
import numpy as np
import pandas as pd

with open('AllNYSVoters_20201116.txt', 'r', encoding='latin-1') as file:
    lines = file.readlines()
    for line in lines[:1000]:  # print the first 100 lines
        print(line)