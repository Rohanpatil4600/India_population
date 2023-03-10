import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
st.set_page_config(layout='wide')
df = pd.read_csv('india.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')
st.sidebar.title('India Analysis')
selected_state = st.sidebar.selectbox('Select a State',list_of_states)
primary = st.sidebar.selectbox('Select Primary Paramter', sorted(list(df.columns[5:])))
Secondary = st.sidebar.selectbox('Select Secondary Paramter', sorted(list(df.columns[5:])))
plot = st.sidebar.button('Plot')
if plot:
    st.text('Size represents Primary Parameter')
    st.text('Color represents Secondary Parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',size= primary, color = Secondary, zoom=3.5,size_max=35, mapbox_style="carto-positron", width=1200, height =800,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df['State']== selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=Secondary, zoom=6,
                                size_max=35, mapbox_style="carto-positron", width=1200, height=800,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)