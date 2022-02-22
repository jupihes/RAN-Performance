
Here is a very short summary guide on steps need to be done for *Sample Data analysis workflow with Pandas*.

Sample python codes and URL links provided so that you could read details.    

https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html 

## read files – part 1
```python
import pandas as pd
import numpy as np

file1_add = r".\input_file1.xlsx"
df1 = pd.read_excel(file_add1)

file2_add = r".\input_file2.xlsx"
df2 = pd.read_excel(file_add2)
```
## Join part – part 2
[Merging tables](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html# )
```python
## Join part – part 2

#do join based on your need and save result in 'summary'.

```
## Pivot part – part 3
Read below links
[pandas-pivot-table-explained](https://pbpython.com/pandas-pivot-table-explained.html)
```python
## Pivot part – part 3
d = pd.pivot_table(summary, index=['Province','4G LTE CELL'], values=["Carrier"], aggfunc = np.unique)
```
## writing result – part 4 

```python
## writing result – part 4 
writer = pd.ExcelWriter(r'.\ Output.xlsx', engine= 'xlsxwriter')
d.to_excel(writer, 'Summary', index = False)
writer.save()
