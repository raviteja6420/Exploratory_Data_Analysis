import streamlit as st

st.header('IPL - Indian Premier League :cricket_bat_and_ball:')

col11,col12,col13 =  st.columns([2,8,2])

with col12:
    st.image('data/IPL_Logo.png')
    


with st.expander("History of IPL"):
    st.write("""**History of the Indian Premier League (IPL)**

**Introduction:**
- The Indian Premier League (IPL) is a professional Twenty20 cricket league in India.
- Launched by the Board of Control for Cricket in India (BCCI) in 2008.

**Key Milestones:**
- **2008:** Inaugural season with eight teams representing various cities.
- **2009:** Relocated to South Africa due to general elections in India.
- **2010:** Chennai Super Kings clinched their first title.
- **2011:** The tournament expanded to 10 teams with the addition of Pune Warriors India and Kochi Tuskers Kerala.
- **2012:** Kolkata Knight Riders won their first IPL title.
- **2013:** Mumbai Indians won their first IPL title.
- **2014:** The tournament returned to India after being held in part in the UAE due to the general elections.
- **2015:** Mumbai Indians won their second IPL title.
- **2016:** Sunrisers Hyderabad clinched their first IPL title.
- **2018:** Chennai Super Kings won their third IPL title.
- **2019:** Mumbai Indians won their fourth IPL title, becoming the most successful team.
- **2020:** Due to the COVID-19 pandemic, the tournament was held in the United Arab Emirates.
- **2021:** Chennai Super Kings won their fourth IPL title.

**Format and Teams:**
- Consists of franchise teams representing different cities and states.
- Each team plays a total of 14 matches in the league stage.
- Top four teams qualify for the playoffs, consisting of Qualifier 1, Eliminator, Qualifier 2, and the Final.
- Players from around the world participate, making it a truly global event.

**Impact and Legacy:**
- Revolutionized cricket with its fast-paced format and entertainment value.
- Provides a platform for young talent to showcase their skills alongside international stars.
- Has contributed significantly to the growth of cricket in India and globally.
- Generates substantial revenue through broadcasting rights, sponsorships, and merchandise.

**Conclusion:**
- The IPL has become one of the most-watched cricket leagues globally, captivating audiences with its thrilling matches and star-studded line-ups. It continues to evolve, leaving an indelible mark on the world of cricket.""")
  
  
  
with st.expander("About Each Team"):
    st.write("""
**Chennai Super Kings (CSK):**
- 2008: Reached the final but lost to Rajasthan Royals.
- 2009: Finished as semi-finalists.
- 2010: Won their first IPL title under the leadership of MS Dhoni.
- 2011: Successfully defended their title, winning the IPL for the second consecutive year.
- 2012: Reached the final but lost to Kolkata Knight Riders.
- 2013: Once again reached the final but lost to Mumbai Indians.
- 2014: Qualified for the playoffs but couldn't progress beyond the eliminator stage.
- 2015: Made it to the final but lost to Mumbai Indians.
- 2016: Suspended for two years due to involvement in the IPL betting scandal.
- 2018: Made a triumphant comeback by winning their third IPL title.
- 2019: Finished as runners-up after losing to Mumbai Indians in the final.
- 2020: Qualified for the playoffs but couldn't advance to the final.
- 2021: Crowned champions for the fourth time by defeating Kolkata Knight Riders in the final.

**Mumbai Indians (MI):**
- 2008: Finished in 5th place.
- 2009: Ended the season in 7th place.
- 2010: Reached the final but lost to Chennai Super Kings.
- 2011: Made it to the playoffs but couldn't progress further.
- 2012: Qualified for the playoffs but couldn't reach the final.
- 2013: Won their first IPL title by defeating Chennai Super Kings in the final.
- 2014: Made it to the playoffs but couldn't defend their title.
- 2015: Clinched their second IPL title by defeating Chennai Super Kings in the final.
- 2016: Finished in 5th place.
- 2017: Won their third IPL title by defeating Rising Pune Supergiant in the final.
- 2018: Finished in 5th place.
- 2019: Topped the league stage and went on to win their fourth IPL title by defeating Chennai Super Kings in the final.
- 2020: Topped the league stage but lost to Delhi Capitals in the first qualifier.
- 2021: Qualified for the playoffs but couldn't defend their title.

**Kolkata Knight Riders (KKR):**
- 2008: Finished in 6th place.
- 2009: Ended the season at the bottom of the table.
- 2010: Finished in 6th place.
- 2011: Reached the playoffs but couldn't advance further.
- 2012: Won their first IPL title by defeating Chennai Super Kings in the final.
- 2013: Qualified for the playoffs but couldn't defend their title.
- 2014: Lifted their second IPL trophy by defeating Kings XI Punjab in the final.
- 2015: Finished in 5th place.
- 2016: Ended the season in 4th place.
- 2017: Finished in 3rd place.
- 2018: Ended the season in 3rd place.
- 2019: Finished in 5th place.
- 2020: Finished in 5th place.
- 2021: Finished in 7th place.

**Royal Challengers Bangalore (RCB):**
- 2008: Finished in 7th place.
- 2009: Reached the final but lost to Deccan Chargers.
- 2010: Finished in 3rd place.
- 2011: Once again reached the final but lost to Chennai Super Kings.
- 2012: Finished in 5th place.
- 2013: Ended the season in 5th place.
- 2014: Finished in 7th place.
- 2015: Reached the playoffs but lost in the eliminator.
- 2016: Once again reached the final but lost to Sunrisers Hyderabad.
- 2017: Finished in 8th place.
- 2018: Ended the season in 6th place.
- 2019: Finished in 8th place.
- 2020: Qualified for the playoffs but lost in the eliminator.
- 2021: Finished in 3rd place.

**Sunrisers Hyderabad (SRH):**
- 2013: Finished in 4th place.
- 2014: Ended the season in 6th place.
- 2015: Finished in 6th place.
- 2016: Won their first IPL title by defeating Royal Challengers Bangalore in the final.
- 2017: Reached the playoffs but lost in the eliminator.
- 2018: Once again reached the final but lost to Chennai Super Kings.
- 2019: Finished in 4th place.
- 2020: Finished in 3rd place.
- 2021: Finished in 8th place.

**Delhi Capitals (DC):**
- 2008: Semi-finalists.
- 2009: Semi-finalists.
- 2010: Finished in 5th place.
- 2011: Ended the season in 10th place.
- 2012: Finished at the bottom of the table.
- 2013: Once again finished at the bottom of the table.
- 2014: Finished in 8th place.
- 2015: Ended the season in 7th place.
- 2016: Finished at the bottom of the table.
- 2017: Finished in 6th place.
- 2018: Finished in 8th place.
- 2019: Finished in 3rd place.
- 2020: Reached the final but lost to Mumbai Indians.
- 2021: Once again reached the final but lost to Chennai Super Kings.

**Punjab Kings (PBKS):**
- 2008: Semi-finalists.
- 2009: Finished at the bottom of the table.
- 2010: Finished in 8th place.
- 2011: Ended the season in 5th place.
- 2012: Finished in 6th place.
- 2013: Finished in 6th place.
- 2014: Reached the final but lost to Kolkata Knight Riders.
- 2015: Finished in 8th place.
- 2016: Once again finished in 8th place.
- 2017: Finished at the bottom of the table.
- 2018: Finished in 7th place.
- 2019: Finished in 6th place.
- 2020: Finished in 6th place.
- 2021: Finished in 6th place.           
             """)
  
    
