r"""
import json
with open(r'D:\python_t\data_json.json') as fo:
    x=json.load(fo)
print(x)
print('name is:',x['name'])

import json
data={"name":"cinderella",
      "age":"20",
      "job":"chores"
      }
with open(r"D:\\python_t\\output.json","w") as json_file:
    json.dump(data,json_file)

import pandas as pd
#print(pd.__version__)
x=pd.read_json(r"D:\\python_t\\output.json")
print(x)
print("data frame")
#print(pd.DataFrame(x))

import pandas as pd
data = {
    "Roll Number": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Maths": [85, 90, 78, 88, 92],
    "Science": [80, 95, 75, 85, 89]
}
df = pd.DataFrame(data)
print("\n=== DataFrame from Dictionary ===")
print(df)
"""

