# Importing pandas and matplotlib modules
import pandas as pd
import matplotlib.pyplot as plt

# loading sessions csv using pandas - indexing the most recent rank 
# Download the source csv from the dropbox link
sessions=pd.read_csv('https://www.dropbox.com/s/58l1kzbhgi623n4/A1-2_sessions_orders.csv?dl=0')
idx=sessions.groupby('unique_visitor_id')['visitor_session_rank'].transform(max) == sessions['visitor_session_rank']
last_click_attribution=sessions[idx]

# Aggregating and sorting
agg_last_click=last_click_attribution.groupby(['channel_group']).size().reset_index(name='counts')
agg_last_click=agg_last_click.sort_values('counts',ascending= False)
agg_last_click

# Plotting
fig1,ax1 = plt.subplots()
ax1.pie(agg_last_click.counts,labels=agg_last_click.channel_group,autopct='%1.1f%%')
ax1.axis('equal')
plt.tight_layout()
plt.show()
