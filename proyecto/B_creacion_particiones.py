import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import Aux_fun as af

df=pd.read_csv("datos_generados.csv")

def df_quartile(df,y,porc,quartile,ascending):
    total_filas=len(df)
    tamanio_q=int(total_filas*porc)-1
    print(tamanio_q)

    if quartile=="first":
        indice_inicio=0
        indice_fin_inclusivo=tamanio_q-1
    elif quartile=="second":
        indice_inicio=tamanio_q
        indice_fin_inclusivo=2*tamanio_q-1
    elif quartile=="third":
        indice_inicio=2*tamanio_q
        indice_fin_inclusivo=3*tamanio_q-1
    elif quartile=="fourth":
        indice_inicio=3*tamanio_q
        indice_fin_inclusivo=4*tamanio_q-1
    elif quartile=="center":
        indice_inicio=int(1.5*tamanio_q)
        indice_fin_inclusivo=int(2.5*tamanio_q)-1

    valores_ordenados=af.shell_sort(df['y'].tolist(),ascendente=ascending)
    tabla_ordenada=df.set_index('y').loc[valores_ordenados].reset_index()
    # tabla_ordenada=df.sort_values(by=y,ascending=ascending,kind='mergesort')
    tabla_ordenada.to_csv("tabla_ordenada.csv", index=False)

    tabla_resultado=tabla_ordenada.iloc[indice_inicio:indice_fin_inclusivo+1]

    orden="asc" if ascending else "desc"
    porc_str=str(porc).replace(".", "")
    filename=f"tabla_{quartile}_{porc_str}_{orden}.csv"

    tabla_resultado.to_csv(filename, index=False)
    print(f"Guardado {filename}")
    return tabla_resultado


B2C=df_quartile(df,'y',porc=0.50,quartile="first",ascending=False)
W2C=df_quartile(df,'y',porc=0.50,quartile="first",ascending=True)

B4C=df_quartile(df,'y',porc=0.25,quartile="first",ascending=False)
W4C=df_quartile(df,'y',porc=0.25,quartile="first",ascending=True)

B8C=df_quartile(df,'y',porc=0.125,quartile="first",ascending=False)
W8C=df_quartile(df,'y',porc=0.125,quartile="first",ascending=True)

B16C=df_quartile(df,'y',porc=0.0625,quartile="first",ascending=False)
W16C=df_quartile(df,'y',porc=0.0625,quartile="first",ascending=True)

df['Label']='df'
B2C['Label']='B2C'
W2C['Label']='W2C'
B4C['Label']='B4C'
W4C['Label']='W4C'
B8C['Label']='B8C'
W8C['Label']='W8C'
B16C['Label']='B16C'
W16C['Label']='W16C'

dataframes=[df,B2C,W2C,B4C,W4C,B8C,W8C,B16C,W16C]
all_data=pd.concat(dataframes)

colors={
    'df': '#6C3483',
    'B2C': '#FF5733',
    'W2C': '#FF5733',
    'B4C': '#FFC300',
    'W4C': '#FFC300',
    'B8C': '#52BE80',
    'W8C': '#52BE80',
    'B16C': '#3498DB',
    'W16C': '#3498DB'
}

plt.figure(figsize=(12, 4))

for label, group_data in all_data.groupby('Label'):
    sns.kdeplot(group_data['y'], label=label, fill=True, alpha=0.5, color=colors[label])

plt.title('Densidad de y entre df y subconjuntos')
plt.xlabel('y')
plt.ylabel('Densidad')
plt.legend()
plt.show()

B4C['y']=1
W4C['y']=0

dfabc4c=pd.concat([B4C,W4C],ignore_index=True)
dfabc4c.head(3)