#%%
import pandas as pd
pd.set_option('display.max_columns', None)
navigation_events = pd.read_csv("data/navigation_events.csv", parse_dates=['event_time', 'event__eventTime'])
assignments = pd.read_csv("data/additional/assignments.csv")
discussion_topics = pd.read_csv("data/additional/discussion_topics.csv")
discussions = pd.read_csv("data/additional/discussions.csv")
enrollments = pd.read_csv("data/additional/enrollments.csv") 
files = pd.read_csv("data/additional/files.csv") 
gradebook = pd.read_csv("data/additional/gradebook.csv") 
module_items = pd.read_csv("data/additional/module_items.csv") 
pages = pd.read_csv("data/additional/pages.csv")
# %%
discussions['discussion_topic_title'].value_counts().sort_index()