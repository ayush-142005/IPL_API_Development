import numpy as np
import pandas as pd

ipl = r'C:\Users\HP\Documents\Project3\datasetipl\matches.csv'
ipl_csv=pd.read_csv(ipl)

print(ipl_csv.head())

def teamsapi():
    team=list(set(list(ipl_csv['team1'])+list(ipl_csv['team2'])))
    team_dct={
        'teams':team
    }
    return team_dct

def team1_vs_team2(Team1,Team2):
    team_df=ipl_csv[(ipl_csv['team1']==Team1)&(ipl_csv['team2']==Team2) | (ipl_csv['team1']==Team2)&(ipl_csv['team2']==Team1)]
    total_match=team_df.shape[0]
    match_won_t1=team_df['winner'].value_counts()[Team1]
    match_won_t2=team_df['winner'].value_counts()[Team2]
    draw=(total_match)-(match_won_t1)-(match_won_t2)

    response={
        "Total Matches Played" : int(total_match),
        "Matches Won by Team1 " : int(match_won_t1),
        "Matches Won by Team2 " : int(match_won_t2),
        "Draw" : int(draw)

    }

    return response