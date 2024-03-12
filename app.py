import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')
df= pd.read_csv('startup_cleaned.csv')
def load_investor_details(investor):
    st.title(investor)
    # load recent investor
    recnet_investment= df[df['investors'].str.contains('investor')].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('most recent investment')
    st.dataframe(recnet_investment)

    # biggest investment
    col1, col2 = st.columns(2)
    with col1:
     big_series= df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
     st.subheader('Biggest investment')
     st.dataframe(big_series)
     fig, ax = plt.subplots()
     ax.bar(big_series.index, big_series.values)

     st.pyplot(fig)
     with col2:
      vertical_series= df[df['investor'].str.contains('IDG Ventures')].groupby('vertical')['amount'].sum()
      st.subheader('sectors invested in')
      fig1, ax1 = plt.subplots()
      ax1.pie(vertical_series)

    st.pyplot(fig1)
# data cleaning
df['investors']= df['investors'].fillna('undisclosed')
#st.dataframe(df)

st.sidebar.title('startup funding analysis')

option= st.sidebar.selectbox('select one',['Overall analysis', 'Startup','Investor'])

if option == 'Overall Analysis':
    st.sidebar('Overall Analysis')
elif option == 'Startup':
    st.sidebar.selectbox('select Startup',sorted(df['startup'].unique().tolist()))
    btn1= st.sidebar.button('Find startup Details')
    st.title('Startup Analysis')
else:
    selected_investor= st.sidebar.selectbox('select investors',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find investor Details')
    if btn2:
     load_investor_details(selected_investor)

