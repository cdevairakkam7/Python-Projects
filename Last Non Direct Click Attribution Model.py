# Importing pandas and matplotlib modules
import pandas as pd
import matplotlib.pyplot as plt

# loading sessions csv into pandas
# Download the source csv from the dropbox link
sessions=pd.read_csv('https://www.dropbox.com/s/58l1kzbhgi623n4/A1-2_sessions_orders.csv?dl=0')

# Splitting  single seesions per anonymous id from multiple sessions per anonymous id
sessions_one_value = sessions.loc[sessions['visitor_session_rank']==1.0]
sessions_more_than_one_temp = sessions.loc[sessions['visitor_session_rank']>1.0]

# Removing  "Direct " channel_group from multiple sessions
sessions_more_than_one =sessions_more_than_one_temp.loc[sessions_more_than_one_temp['channel_group'] != 'Direct']

# Appending single sessions with multiple sessions
sessions_final=sessions_one_value.append(sessions_more_than_one,ignore_index=True)

# indexing the most recent rank
idx=sessions_final.groupby('unique_visitor_id')['visitor_session_rank'].transform(max) == sessions_final['visitor_session_rank']
last_non_direct_click_attribution=sessions_final[idx]

# Aggregating and sorting
agg_last_non_direct_click=last_non_direct_click_attribution.groupby(['channel_group']).size().reset_index(name='counts')
agg_last_non_direct_click

# Plotting
fig1,ax1 = plt.subplots()
ax1.pie(agg_last_non_direct_click.counts,labels=agg_last_non_direct_click.channel_group,autopct='%1.1f%%')
ax1.axis('equal')
plt.tight_layout()
plt.show()

