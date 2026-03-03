import streamlit as st
import pandas as pd

st.set_page_config(page_title='Zalates Media Engagement', layout='wide')

st.title('Zalates Media Engagement Dashboard')
st.caption('Prototype dashboard for Ethiopian Government social media engagement.')

data = pd.DataFrame({
    'account': ['MoH', 'MoE', 'MoFA'],
    'total_engagement': [1200, 1050, 700],
    'avg_engagement_rate': [3.2, 2.7, 1.9],
})

st.markdown('### Sample Data (placeholder)')
st.dataframe(data)

st.markdown('### Total Engagement')
st.bar_chart(data.set_index('account')['total_engagement'])
