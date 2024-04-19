import streamlit as st
import numpy as np
import pandas as pd


st.header('Team Performance Overview :stadium:')
df = pd.read_csv('data/merged_ipl.csv')

df.loc[df['BattingTeam']==df['Team1'], 'BowlingTeam'] = df['Team2']
df.loc[df['BattingTeam']==df['Team2'], 'BowlingTeam'] = df['Team1']

team_mapping = {'Delhi Capitals':'Delhi Capitals',
                'Delhi Daredevils':'Delhi Capitals', 
                'Kings XI Punjab':'Punjab Kings',
                'Rising Pune Supergiants':'Rising Pune Supergiant',
                'Gujarat Lions':'Gujarat Titans'}
df['BattingTeam'] = df['BattingTeam'].map(team_mapping).fillna(df['BattingTeam'])
df['BowlingTeam'] = df['BowlingTeam'].map(team_mapping).fillna(df['BowlingTeam'])

team_names = df['BattingTeam'].unique()
selected_team = st.selectbox('Select Team', team_names)
season_and_matches = df[(df['BattingTeam']==selected_team) | (df['BowlingTeam']==selected_team)].groupby(['year','ID'])
total_matches_played = season_and_matches['total_run'].sum().reset_index()['ID'].nunique()
total_seasons_played = season_and_matches['total_run'].sum().reset_index()['year'].nunique()
no_of_matches_won = df[df['WinningTeam']==selected_team].groupby(['year', 'ID'])['total_run'].sum().reset_index()['ID'].nunique()
win_rate = round((no_of_matches_won / total_matches_played) * 100, 2)

st.subheader(f'Summary about {selected_team}')

col11,col12,col13,col14 =  st.columns(4)

with col11:
    st.metric('No.of Seasons Played: ', value=total_seasons_played, delta=df['year'].nunique(), delta_color='off')

with col12:
    st.metric('No.of Matches Played: ', value=total_matches_played)

with col13:
    st.metric('No.of Matches Won: ', value=no_of_matches_won)

with col14:
    st.metric('Winning Rate: ', value=win_rate)
#----------------------------------------------------------------------------------------------------------------------
matches = pd.read_csv('data/matches.csv')
matches['season'] = matches['Season'].apply(lambda x: x.split('-')[1]).astype('int32')

matches['team1'] = matches['team1'].map(team_mapping).fillna(matches['team1'])
matches['team2'] = matches['team2'].map(team_mapping).fillna(matches['team2'])
matches['toss_winner'] = matches['toss_winner'].map(team_mapping).fillna(matches['toss_winner'])
matches['winner'] = matches['winner'].map(team_mapping).fillna(matches['winner'])


toss_won = matches[((matches['team1']==selected_team) | (matches['team2']==selected_team) & (matches['toss_winner']==selected_team))]

no_of_times_toss_won = toss_won.count()[0]
toss_decision = toss_won['toss_decision'].mode()[0]

ipl_matches =pd.read_csv('data/IPL_Matches_2008_2022.csv')
titles_won = len(ipl_matches[(ipl_matches['WinningTeam']==selected_team) & (ipl_matches['MatchNumber']=='Final')])

col21,col22,col23,col24 =  st.columns(4)

with col21:
    st.metric('No.of Times Toss Won: ', value=no_of_times_toss_won)

with col22:
    st.metric("Toss Decision Most Times: ", value=toss_decision)

with col23:
    st.metric("No.of Titles Won: ", value=titles_won)

# with col24:
#     st.metric("Total 100's : ", value=_100s)


