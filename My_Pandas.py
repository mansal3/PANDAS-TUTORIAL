import pandas as pd
dict={
    "name":["nancy","shruti","yoshi"],
    "class":["first","second","third"],
    "school":["ghps","ghps","sdips"]
}
arr=pd.DataFrame(dict)
print(arr)

arr.index=[23,24,25]
print(arr)

binar=pd.read_csv('/Users/manpreetsaluja/Downloads/binary.csv' , index_col=0)
print(binar)
print(binar['gpa'])
print(binar[['gpa']])
print(binar[2:4])

#use loc and iloc to perform just about any data selection operation.
# loc is label-based, which means that you have to specify rows and columns based on their
# row and column labels. iloc is integer index based, so you have to specify rows and columns by their integer index
print(binar.iloc[2])
#print(binar.loc['2'])

#A panel is a 3D container of data.
# The term Panel data is derived from econometrics and is partially responsible
# for the name pandas − pan(el)-da(ta)-s.
import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
p = pd.Panel(data)
print(p)

import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print(s)