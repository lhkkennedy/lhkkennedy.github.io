import pandas as pd
import os


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


filename = "DebtGDP.csv"
df = pd.read_csv(filename)
qs = df['date'].str.replace(r'(\d+) (Q\d)', r'\1-\2')
df['date'] = pd.PeriodIndex(qs, freq='Q').to_timestamp()

filelocation = os.getcwd()
print("Saving as:  [ " + filename + " ]  in:  [ " + filelocation + " ] ")
df.to_csv(filename)
