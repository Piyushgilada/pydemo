import numpy as np
import random
import pygame
# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a, index = ["x", "y", "z"])
# # print(myvar["y"])
# print(myvar)

import pandas as pd
df = pd.read_json('main.json')
print(df)

print(df.to_string())
# print(df)
# pd.options.display.max_rows = 9999
# print(pd.options.display.max_rows)
# print(df.to_string())