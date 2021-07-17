import streamlit as st
import pandas as pd
import numpy as np
from database_ops import db_execute_fetch

def main():
    st.title("TellCo Data Analytics Dashboard")

    st.sidebar.write("Navigation")
    app_mode = st.sidebar.selectbox("Choose Here", ("Home", "Univariate Analysis","Regression Model"))
    if app_mode == 'Home':
        st.write('''
        ## Introduction
        In this project, we are analyzing the customer information of a company called TellCo, an existing mobile service provider in the 
        Republic of Pefkakia. Our objective is to provide a report to analyze opportunities for growth and make a recommendation on whether 
        TellCo is worth buying or selling.
        ''')
        dataframe = db_execute_fetch("Select * from satisfaction_scores;", dbName = 'telecom_user_satisfaction')
        st.write('''
        ## Some overview of the data
        ''')
        st.table(dataframe.sample(5))
        
    elif app_mode == 'Univariate Analysis':
        st.write('''
        ## Here are a few plots of the variables
        ''')
        dataframe = db_execute_fetch("Select * from satisfaction_scores;", dbName = 'telecom_user_satisfaction')

        st.subheader('Engagement Score Plot')
        hist_values = np.histogram(dataframe['Engagement_Score'], bins=50)[0]
        st.bar_chart(hist_values)

        st.subheader('Experience Score Plot')
        hist_values = np.histogram(dataframe['Experience_Score'], bins=50)[0]
        st.bar_chart(hist_values)

        st.subheader('Satisfaction Score Plot')
        hist_values = np.histogram(dataframe['Satisfaction_Score'], bins=50)[0]
        st.bar_chart(hist_values)

        st.subheader('Cluster Plot')
        hist_values = np.histogram(dataframe['Cluster'], bins=2)[0]
        st.bar_chart(hist_values)
    elif app_mode == 'Regression Model':
        st.write('''
        ## Regression Model
        ''')
        #st.image('cloud.png')
    
if __name__ == "__main__":
    main()