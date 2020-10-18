# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:00:44 2019

@author: lenovo
"""

import pandas as pd
import numpy as np

#stdout()


shot_df = pd.read_csv('../../Dataset/nba-shot-logs/shot_logs.csv')
#shot_df = shot_df[(shot_df['player_name'] == 'james harden')]


defender_pair = pd.concat([shot_df['player_id'],\
                           shot_df['player_name'], shot_df['CLOSEST_DEFENDER_PLAYER_ID'], shot_df['CLOSEST_DEFENDER']], axis=1, keys=['PLAYER_ID', 'PLAYER','DEFENDER_ID', 'DEFENDER'])


defender_pair = defender_pair.drop_duplicates()

solu = pd.DataFrame()


for index, row in defender_pair.iterrows():
#    print("____________________")
    player_id = row['PLAYER_ID']
    defender_id = row['DEFENDER_ID']
    test = shot_df[(shot_df['player_id'] == player_id)\
                   & (shot_df['CLOSEST_DEFENDER_PLAYER_ID'] == defender_id)]
    
    defender_pair.loc[(defender_pair['PLAYER_ID'] == player_id)\
                    & (defender_pair['DEFENDER_ID'] == defender_id), 'MADE']\
                    = test[(test['SHOT_RESULT'] == 'made')]['player_id'].count()
#    print("-----------")
    defender_pair.loc[(defender_pair['PLAYER_ID'] == player_id)\
                    & (defender_pair['DEFENDER_ID'] == defender_id), 'TOTAL']\
                    = test['player_id'].count()

    defender_pair['FEAR_SORE'] = defender_pair['MADE'] / defender_pair['TOTAL']


player_id = defender_pair['PLAYER_ID'].drop_duplicates()


defender_pair2 = defender_pair[(defender_pair['TOTAL'] > 15)]

#defender_pair2 = defender_pair[(defender_pair['TOTAL'] > 5)]
for player in player_id:
    
    diff_df = defender_pair2[(defender_pair2['PLAYER_ID'] == player)].sort_values(by='FEAR_SORE', axis=0, ascending=True, inplace=False)
    
    solu = solu.append(diff_df.head(1), ignore_index = True)
