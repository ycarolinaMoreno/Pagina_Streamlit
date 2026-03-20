from turtle import width
from PIL import Image
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


#icono de página
icono = Image.open("Icono_diabetes.png")

##Configurar nombre de pagina
st.set_page_config(page_title="Mi APP_Diabetes", page_icon=icono, layout="wide")

##Agregar titulo y descripcion
st.sidebar.header("Información general")
st.markdown("<h1 style='color:blue;'>Predicción de la Diabetes</h1>", unsafe_allow_html=True)
st.write("La diabetes es una condición crónica que afecta la forma en que el cuerpo utiliza la glucosa, su principal fuente de energía. Existen diferentes tipos de diabetes, y cada uno requiere cuidados especiales para mantener una buena calidad de vida. El objetivo de esta página es brindar información básica, fomentar la conciencia sobre la importancia de la prevención y promover hábitos saludables que ayuden a controlar la enfermedad.")



with open("ReflexivoDiabetes.mp4", "rb") as video_file:
    st.video(video_file.read(), start_time=0)


 #cargar dataset
def cargar_datos():
    df = pd.read_csv('diabetes_risk_dataset.csv')
    df.columns = df.columns.str.strip()
    df.rename(columns={'age': 'edad', 'gender': 'Genero', 'bmi': 'IMC', 'blood_pressure': 'Presión Arterial', 'fasting_glucose_level': 'Glucosa en ayunas', 'insulin_level': 'Nivel de insulina', 'HbA1c_level': 'Nivel de insulina Glicosilada', 'cholesterol_level': 'Nivel de colesterol', 'triglycerides_level': 'Nivel de trigliceridos', 'physical_activity_level': 'Nivel de actividad fisica', 'daily_calorie_intake': 'Ingesta diaria de caloria', 'sugar_intake_grams_per_day': 'Ingesta de azucar g/dia', 'sleep_hours': 'Horas de sueño', 'stress_level':'Nivel de estres', 'family_history_diabetes': 'Historial Familiar', 'waist_circumference_cm': 'Circunferencia de cintura cm', 'diabetes_risk_score': 'Puntuacion de riesgo', 'diabetes_risk_category': 'Categoria de riesgo'}, inplace=True)
    return df
df=cargar_datos()
st.dataframe(df)

## Separador visual
###
st.header("Objetivos")

st.write("""- Analizar factores de riesgo asociados a la diabetes.
- Identificar patrones en variables como edad, glucosa y BMI.
- Visualizar tendencias y distribución de los datos.
""")
##Seccion de genero de los pacientes