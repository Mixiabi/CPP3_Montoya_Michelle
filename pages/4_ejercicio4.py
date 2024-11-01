import time
import streamlit as st
from estilo import pg_bg_pgs
import math

st.markdown(pg_bg_pgs,unsafe_allow_html=True)

st.title('Ejercicio 04')
'''
**Crear un programa, que permita hallar el área y perímetro de
una circunferencia. Utilizar procedimientos.**
'''
def areaCircunferencia(radio):
    if radio is None:
        return '🚨 **Campo radio debe ser llenado**'
    try:
        area = math.pi * radio ** 2
        return area
    except (ValueError, TypeError):
        return None

def perimetroCircunferencia(radio):
    if radio is None:
        return '🚨 **Campo radio debe ser llenado**'
    try:
        perimetro = 2*math.pi*radio
        return perimetro
    except ValueError:
        return None
    
def reiniciar():
    aviso = st.info('Calculo Reiniciado')
    time.sleep(1.5)
    aviso.empty()
        
def main():
    st.subheader('**Calcular Area y/o Perimetro**')
    nuevoRadio = st.number_input('**Ingresa el radio de la Circunferencia**', value=None, format='%.f')

    if st.button('**Hallar el Área**'):
        resultado_area = areaCircunferencia(nuevoRadio)
        if isinstance(resultado_area, str):
            a = st.error(resultado_area)
            time.sleep(2)
            a.empty()
        else:
            st.write(f'**Área de la Circunferencia es:** {resultado_area}')
    
    if st.button('**Hallar el Perimetro**'):
        resultado_perimetro = perimetroCircunferencia(nuevoRadio)
        if isinstance(resultado_perimetro,str):
            a = st.error(resultado_perimetro)
            time.sleep(2)
            a.empty()
        else:
            st.write(f'**Perimetro de la Circunferencia es:** {perimetroCircunferencia(resultado_perimetro)}')
    
    if st.button('**Hallar Area y Perimetro**'):
        st.write(f'**Area de la Circunferencia es:** {areaCircunferencia(nuevoRadio)}')
        st.write(f'**Perimetro de la Circunferencia es:** {perimetroCircunferencia(nuevoRadio)}')
        
    if st.button('Reiniciar',type='primary'):
        reiniciar()

if __name__ == "__main__":
    main()