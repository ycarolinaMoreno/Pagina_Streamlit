from turtle import width
from PIL import Image
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


 #cargar dataset
def cargar_datos():
    df = pd.read_csv('diabetes_risk_dataset.csv')
    df.columns = df.columns.str.strip()
    df.rename(columns={'age': 'edad', 'gender': 'Genero', 'bmi': 'IMC', 'blood_pressure': 'Presión Arterial', 'fasting_glucose_level': 'Glucosa en ayunas', 'insulin_level': 'Nivel de insulina', 'HbA1c_level': 'Nivel de insulina Glicosilada', 'cholesterol_level': 'Nivel de colesterol', 'triglycerides_level': 'Nivel de trigliceridos', 'physical_activity_level': 'Nivel de actividad fisica', 'daily_calorie_intake': 'Ingesta diaria de caloria', 'sugar_intake_grams_per_day': 'Ingesta de azucar g/dia', 'sleep_hours': 'Horas de sueño', 'stress_level':'Nivel de estres', 'family_history_diabetes': 'Historial Familiar', 'waist_circumference_cm': 'Circunferencia de cintura cm', 'diabetes_risk_score': 'Puntuacion de riesgo', 'diabetes_risk_category': 'Categoria de riesgo'}, inplace=True)
    return df
    
df=cargar_datos()

df['Genero'] = df['Genero'].replace({
        'Male': 'Hombre',
        'Female': 'Mujer'
    })

df_cuenta = df.groupby('Genero').count().reset_index()
fig = px.pie(df_cuenta, names='Genero', values='Patient_ID', title='Distribución de Pacientes por Género')
st.plotly_chart(fig, width=800)


fig.update_layout(
    title={
        'text': 'Distribución de Pacientes por Género',
        'x': 0.5,
        'xanchor': 'center'})


promedios_genero = df.groupby('Genero')['Horas de sueño'].mean().reset_index()

fig = px.bar(
    promedios_genero,
    x='Genero',
    y='Horas de sueño',
    color='Genero',
    title='Promedio de horas de sueño por género',
    labels={'Horas de sueño': 'Horas promedio de sueño'},
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig.update_layout(
    title={'x': 0.5},
    showlegend=False,
    template='plotly_white'
)

# Mostrar valores encima de las barras
fig.update_traces(text=promedios_genero['Horas de sueño'].round(2), textposition='outside')

st.plotly_chart(fig, use_container_width=True)