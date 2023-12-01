import pickle
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt

page = st.sidebar.selectbox('Select Page',['Home','Grafik','Pencarian'])

model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))

if page=='Home':
    st.title('Prediksi Harga Mobil')
    st.image('mobill.jpg',width=400)
    st.header('Dataset')

    df1 = pd.read_csv('CarPrice.csv')
    st.dataframe(df1)

elif page=='Grafik':
    df1 = pd.read_csv('CarPrice.csv')
    chart_highwaympg = pd.DataFrame(df1, columns=["highwaympg"])
    chart_curbweight = pd.DataFrame(df1, columns=["curbweight"])
    chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])

    grafik = st.selectbox('Pilih Grafik', ['Highway-mpg', 'Curbweight', 'Horsepower'])
    if grafik=='Highway-mpg':
        chart = st.selectbox('Silahkan pilih :' , ['line chart' , 'area chart', 'bar chart'])
        if chart=='line chart':
            st.write('Grafik line Higway-mpg')
            st.line_chart(chart_highwaympg)
        elif chart=='area chart':
            st.write('Grafik area Higway-mpg')
            st.area_chart(chart_highwaympg)
        elif chart=='bar chart':
            st.write('Grafik bar Higway-mpg')
            st.bar_chart(chart_highwaympg)
    if grafik=='Curbweight':
        chart = st.selectbox('Silahkan pilih :' , ['line chart' , 'area chart', 'bar chart'])
        if chart=='line chart':
            st.write('Grafik line Curbweight')
            st.line_chart(chart_curbweight)
        elif chart=='area chart':
            st.write('Grafik area Curbweight')
            st.area_chart(chart_curbweight)
        elif chart=='bar chart':
            st.write('Grafik bar Curbweight')
            st.bar_chart(chart_curbweight)
    if grafik=='Horsepower':
        chart = st.selectbox('Silahkan pilih :' , ['line chart' , 'area chart', 'bar chart'])
        if chart=='line chart':
            st.write('Grafik line Horsepower')
            st.line_chart(chart_horsepower)
        elif chart=='area chart':
            st.write('Grafik area Horsepower')
            st.area_chart(chart_horsepower)
        elif chart=='bar chart':
            st.write('Grafik bar Horsepower')
            st.bar_chart(chart_horsepower)
    
elif page=='Pencarian':
    df1 = pd.read_csv('CarPrice.csv')
    highwaympg = st.number_input("Highway ", 0,10000000)
    curbweight = st.number_input("curbweight ", 0,10000000)
    horsepower = st.number_input("horsepower ", 0,10000000)

    if st.button('Prediksi'):
        carprediction = model.predict([[highwaympg, curbweight, horsepower]])

        harga_mobil_str = np.array(carprediction)
        harga_mobil_float = float(harga_mobil_str[0])

        harga_mobil_formatted = "{:,.2f}".format(harga_mobil_float)
        st.markdown(harga_mobil_formatted)
