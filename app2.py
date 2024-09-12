import altair as alt
from vega_datasets import data
import pandas as pd
import streamlit as st

emp = pd.read_csv("c:\\data\\emp.csv")
source = emp[['ename','sal']]

bars = alt.Chart(source).mark_bar().encode(
    x='sal',
    y="ename"
)

text = bars.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='sal'
)

a = (bars + text).properties(height=500)

st.dataframe(emp)  # Same as st.write(df)
st.altair_chart(a, use_container_width=True)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


money = pd.read_csv("money_data7.csv")

option = st.selectbox(
    'How would you like to choice year ?',
    ('2020', '2021', '2022'))

option2 = int(option)

st.write('You selected:', option)

money = money[:] [money['A_YEAR']== option2]

fig, ax = plt.subplots(2,2, figsize=(12,8))

plt.subplot(221)
plt.plot(  list( money['A_MONTH'] ), list( money['A_RATE'] ), color='red' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('America rate')


plt.subplot(222)
plt.plot(  list( money['A_MONTH'] ), list( money['K_RATE'] ), color='blue' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('Korea rate')

plt.subplot(223)
plt.plot(  list( money['A_MONTH'] ), list( money['KOSPI'] ), color='green' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('Kospi Rate')

plt.subplot(224)
plt.plot(  list( money['A_MONTH'] ), list( money['HOUSE_PRICE'] ), color='yellow' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('House Price')

st.pyplot(fig)

