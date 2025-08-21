import pandas as pd

#carga la cartera de la cual se hizo el envio
df1 = pd.read_csv("Dc_Cartera_junio_2025.txt", sep=",",dtype=str, encoding="latin1")
#carga el csv de los celulares a los cuales se les hizo el envio
df2 = pd.read_csv("celulares_filtrados_cartera_junio2024(segundo_Envio).csv", sep=",", dtype=str, encoding="latin1")

# Limpia los datos de la columna 'CELULAR' en ambos DataFrames
df1['CELULAR'] = df1['CELULAR'].astype(str).str.replace('.0', '', regex=False).str.strip()
df2['CELULAR'] = df2['CELULAR'].astype(str).str.replace('.0', '', regex=False).str.strip()

# Realiza el merge para obtener los datos deseados
#que en resumen, agarra los datos de los celulares que se encuentran en df2 y los datos de df1
# y los une en un nuevo DataFrame result usando la columna 'CELULAR' como clave
result = pd.merge(
    df2[['CELULAR']], 
    df1[['CELULAR', 'ID_USUARIO', 'NOMBRES', 'APELLIDOS']], 
    on='CELULAR', 
    how='inner'
)

# Elimina duplicados basados en la columna 'CELULAR'
result.drop_duplicates(subset=['CELULAR'], inplace=True)

# Añade las columnas solicitadas con valores fijos
result['TIPO_MENSAJE'] = 'MENSAJE DE TEXTO AGRESIVO'
result['MENSAJE'] = 'El instituto de Ttransito del Atlantico le informa que usted registra una deuda por Derechos de Transito 2024 y anteriores. Se le concede un plazo improrrogable de 5 dias habiles para regularizar su situacion. De no hacerlo&$ se iniciara cobro coactivo&$ con posibles medidas como embargo de cuentas&$ inmuebles y vehiculos&$ conforme a la normativa vigente&$ page ahora acerquese a la calle 40 # 45-05 de 8:00 AM a 4:30 PM jornada continua.'
result['FECHA_ENVIO'] = '11/07/2025'

# Guarda el resultado en un nuevo CSV
result.to_csv("Segundo_envio_masivo.csv", index=False, encoding="utf-8")