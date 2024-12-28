import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from bs4 import BeautifulSoup
import os
import sys
import time
import requests
import warnings
import PyPDF3

# Ignora la advertencia InsecureRequestWarning
warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
# ----- VALORES INICIALES
jornal = 107627
usuario = '1591666'
password = 'estudioAmarillaCloss3'
controlador = 'https://unionnegocios.com.py/sistema/juicios/datos/'

# tiempo_inicio = time.time()
# # FUNCION waitclick
# def waitclick(wait_time=0.5, xpath='', driver='' ):
#     time.sleep(wait_time)
#     element = driver.find_element(By.XPATH, xpath)
#     element.click()

st.title("Dar entrada CSJ")

# CARGAR EL NUMERO DE JUICIO
query_params = st.query_params
# Extraer los valores de 'juicio', 'user' y 'pass'
juicio = query_params.get("juicio", [""])
usuario = query_params.get("u", [""])    
password = query_params.get("p", [""])   
controlador = query_params.get("controlador", [""])   
# Validar los valores obtenidos
if juicio==[""] or usuario==[""] or password==[""] or  controlador==[""]:
    st.warning("falta parametros")
    st.stop()

st.write('🚀 Iniciar proceso !!')
url = controlador + juicio

# try:
#     headers = {"Accept": "application/json"} # Cambiar Content-Type a Accept
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         if data.get("respuesta") is None:
#             id_juicio = data['id_juicios']
#             cedula = data['ci1']
#             monto = data['monto']
#             grupo = data['grupo']
#             credito_nro = data['credito_nro']
#             st.write(  "--- " + cedula + " " + data['dem1'] + " " + monto )
#         else:
#             st.write( "⚠️  Error no existe la ciudad. Ver en unionnegocios.com.py/sistema/juicios/show/" + juicio )
#             sys.exit()            
#     else:
#         st.write( "⚠️  Error {response.status_code} ")
#         sys.exit()
# except Exception as e:
#     st.write( "⚠️  Error " + str(e))
#     sys.exit()
# st.write( '⌛ procesando....')
