import pandas as pd

def sapo(df):
    for num in df["dbh"]:
        new_num = ""
        for char in num:
            if char.isnumeric():
                new_num += char
            num = float(new_num)

df = pd.read_csv("bprd_trees(in).csv")

mask_known = df["date_plant"].notna() & (df["date_plant"] != "--")
years = []
num = 0
for str_year in df["date_plant"]:
    if mask_known[num]:
        str_year = str_year.strip()
        list_year = str_year.split(" ")
        years.append(int(list_year[1]))
    num += 1
df.loc[mask_known, "plant_year"] = years
