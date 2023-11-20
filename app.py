import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
#import -r requirements.txt

#from utils.b2 import B2

# ------------------------------------------------------
#                      APP CONSTANTS
# ------------------------------------------------------
REMOTE_DATA = './data/train.csv'


# ------------------------------------------------------
#                        CONFIG
# ------------------------------------------------------
load_dotenv()


# ------------------------------------------------------
#                         APP
# ------------------------------------------------------
st.write(
'''
## Toxic Comment data 
We pull data from our Github storage, was facing issues with Backblaze bucket, and render it in Streamlit using `st.dataframe()`.
''')


df_ = pd.read_csv(os.environ['REMOTE_DATA'])
st.dataframe(df_)




# ------------------------------
# PART 2 : Plot
# ------------------------------

st.write(
'''
### Quantitative Question 
What kind of Toxic comments are present in the dataset? what is the count of each toxicity - based on different types (i.e. Sever_toxic, obscene, threat, insult, identity_hate)? 
''')

fig, ax = plt.subplots()
df_count = df_.iloc[:,2:].sum()
#df_count
ax.bar(x= df_count.index,height = df_count.values, alpha=0.6)
ax.set_xlabel('Features/ Toxicity Type')
ax.set_ylabel('No. of occurances')

show_graph = st.checkbox('Show Graph', value=True)

if show_graph:
    st.pyplot(fig)
