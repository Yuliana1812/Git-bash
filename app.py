import streamlit as st
import pandas as pd   
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv('datps.csv')
st. title("PRIMERA APP")

tab1, tab2 = st.tabs (["tab1","tab2"])

with tab1:
    st.header("Análisis gráfico")
    fig, ax = plt.subplots(1,3, figsize = (10,4))
    ax[0].hist(df["edad"])
    conteo = df["sexo"].value_counts()
    ax[1].bar(conteo.index, conteo.values)
    ax[2].hist(df["salario"])
    fig.tight_layout()
    
    st.pyplot(fig)

    fig, ax = plt.subplots(1,2, figsize=(10,4))  
    sns.scatterplot(data=df, x= "edad", y= "salario", ax=ax[0])
    sns.boxplot(data=df, x= "sexo", y= "salario", ax=ax[1])  
    sns.violinplot(data=df, x= "sexo", y= "salario", ax=ax[1]) 
    fig.tight_layout()

    st.pyplot(fig)

with tab2:
    pass