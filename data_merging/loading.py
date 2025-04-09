import os
import numpy as np
import pandas as pd


# change your working directory
wd = ''
os.chdir(wd)


# load 2024
header_2024 = ['lastname', 'firstname', 'middlename', 'namesuffix', 'raddnumber', 
               'rhalfcode', 
               'rpredirection', 'rstreetname', 'rpostdirection', 
               'rapartmenttype', 'rapartment', 'raddrnonstd', 
               'rcity', 'rzip5', 'rzip4', 'mailadd1', 'mailadd2', 
               'mailadd3', 'mailadd4', 'dob', 'gender', 'enrollment', 'otherparty', 'countycode', 
               'ed', 'ld', 'towncity', 'ward', 'cd', 'sd', 'ad', 'lastvoteddate', 'prevyearvoted', 
               'prevcounty', 'prevaddress', 'prevname', 'countyvrnumber', 'regdate', 'vrsource', 
               'idrequired', 'idmet', 'status', 'reasoncode', 'inact_date', 'purge_date', 'sboeid', 'voterhistory']

df = pd.read_csv('AllNYSVoters_20240529.csv',
                sep=',',
                names = header_2024,
                encoding='ISO-8859-1',
                low_memory= False             # Alternative encoding
                )
df.head()


# change the order of columns - 2024
new_order = ['lastname', 'firstname', 'middlename', 'namesuffix', 'raddnumber', 
            'rhalfcode', 
            'rapartment', 
            'rpredirection', 'rstreetname', 'rpostdirection', 
            'rcity', 'rzip5', 'rzip4', 'mailadd1', 'mailadd2', 
            'mailadd3', 'mailadd4', 'dob', 'gender', 'enrollment', 'otherparty', 'countycode', 
            'ed', 'ld', 'towncity', 'ward', 'cd', 'sd', 'ad', 'lastvoteddate', 'prevyearvoted', 
            'prevcounty', 'prevaddress', 'prevname', 'countyvrnumber', 'regdate', 'vrsource', 
            'idrequired', 'idmet', 'status', 'reasoncode', 'inact_date', 'purge_date', 'sboeid', 'voterhistory', 
            'rapartmenttype', 'raddrnonstd', ]

df_24_reordered = df[new_order]
df_24_reordered.head()


# load 2020
header_2020 = ['lastname', 'firstname', 'middlename', 'namesuffix', 'raddnumber', 
               'rhalfcode', 
               'rapartment', 
               'rpredirection', 'rstreetname', 'rpostdirection', 
               'rcity', 'rzip5', 'rzip4', 'mailadd1', 'mailadd2', 'mailadd3', 'mailadd4', 
               'dob', 'gender', 'enrollment', 'otherparty', 'countycode', 'ed', 'ld', 'towncity',
               'ward', 'cd', 'sd', 'ad', 'lastvoteddate', 'prevyearvoted', 'prevcounty', 
               'prevaddress', 'prevname', 'countyvrnumber', 'regdate', 'vrsource', 'idrequired', 
               'idmet', 'status', 'reasoncode', 'inact_date', 'purge_date', 'sboeid', 'voterhistory']

df_2020 = pd.read_csv('AllNYSVoters_20201116.txt', 
                    sep=',', 
                    encoding='latin-1',
                    low_memory= False,
                    names = header_2020)
df_2020.head()


# add 2 columns to match 2024
df_2020['rapartmenttype'] = np.nan
df_2020['raddrnonstd'] = np.nan

df_2020.head()


# merging them together
df_20_24 = pd.concat([df_2020, df_24_reordered])
df_20_24.tail()


# reorder the columns to the original order
old_order = ['lastname', 'firstname', 'middlename', 'namesuffix', 'raddnumber', 
               'rhalfcode', 
               'rpredirection', 'rstreetname', 'rpostdirection', 
               'rapartmenttype', 'rapartment', 'raddrnonstd', 
               'rcity', 'rzip5', 'rzip4', 'mailadd1', 'mailadd2', 
               'mailadd3', 'mailadd4', 'dob', 'gender', 'enrollment', 'otherparty', 'countycode', 
               'ed', 'ld', 'towncity', 'ward', 'cd', 'sd', 'ad', 'lastvoteddate', 'prevyearvoted', 
               'prevcounty', 'prevaddress', 'prevname', 'countyvrnumber', 'regdate', 'vrsource', 
               'idrequired', 'idmet', 'status', 'reasoncode', 'inact_date', 'purge_date', 'sboeid', 'voterhistory']

df_20_24_comb = df_20_24[old_order]
df_20_24_comb.head()


# merge
df_20_24_comb.to_csv('merged_voter_data_20_24.csv', encoding='utf-8', index=False)