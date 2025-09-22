import pandas as pd

#top 10 baby names 2010's
b_names = ["Noah", "Liam", "Jacob", "William", "Mason", "James", "Ethan", "Michael", "Alexander", "James"]
g_names = ["Emma", "Olivia", "Sophia", "Isabella", "Ava", "Abigail", "Emily", "Charlotte", "Madison", "Lily"]

b_freq = [183330, 173981, 163266, 159945, 157875, 149082, 145171, 142142, 139652, 137093]
g_freq = [195028, 184528, 181132, 170559, 155844, 129088, 118713, 117626, 102470, 98419]

df = pd.DataFrame(
    {
    'Boy Names':b_names, 
    'bFreq':b_freq, 
    'Girl Names':g_names,
    'gFreq':g_freq
    })
print(df)
print(df.describe())