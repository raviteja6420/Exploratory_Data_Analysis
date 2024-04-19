import streamlit as st
import pandas as pd

def check(match,team):
    return len(match[(match['Team1'] == team) | (match['Team2'] == team)])

def count(S,team):
    try :
        return S[S.index == team].values[-1]
    except:
        return 0

match = pd.read_csv(r'Data/IPL_Matches_2008_2022.csv')
win = match.groupby(['WinningTeam'])['WinningTeam'].count()
playoff = match[match['MatchNumber'].isin(['Qualifier 1','Eliminator','Semi Final'])]
final = match[match['MatchNumber'].isin(['Final'])]['WinningTeam'].value_counts()
teamnames = sorted(match['Team1'].unique().tolist())
team = st.selectbox('Select Team',teamnames)

col1, col2 = st.columns(2)

with col1:
    images = st.image(f'Logo/{team}.png')
with col2:
    st.write("Total Matches ",check(match,team))
    st.write("Total Won ",win[win.index == team].iloc[-1])
    st.write("Play off Qualifies",check(playoff,team))
    st.write("Title Won",count(final,team))
    st.write("Toss Won",count(match['TossWinner'].value_counts(),team))
    