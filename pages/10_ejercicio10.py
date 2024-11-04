import streamlit as st
from estilo import pg_bg_pgs

st.markdown(pg_bg_pgs,unsafe_allow_html=True)
st.title('Ejercicio 10')
'''
Crear una calculadora de las cuatro operaciones básicas,
donde se envíe los parámetros a operar y este retorne los resultados.
'''

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return '🚨 **No se puede dividir por cero.**'
    return a / b

def main():

    num1 = st.number_input('Ingrese el primer número:', format="%.f")
    num2 = st.number_input('Ingrese el segundo número:', format="%.f")

    operacion = st.selectbox('Seleccione la operación:', ('Suma', 'Resta', 'Multiplicación', 'División'))

    if st.button('Calcular'):
        if operacion == 'Suma':
            resultado = sumar(num1, num2)
        elif operacion == 'Resta':
            resultado = restar(num1, num2)
        elif operacion == 'Multiplicación':
            resultado = multiplicar(num1, num2)
        elif operacion == 'División':
            resultado = dividir(num1, num2)

        # Mostrar el resultado
        st.write(f'Resultado: {resultado:.2f}')

if __name__ == "__main__":
    main()
