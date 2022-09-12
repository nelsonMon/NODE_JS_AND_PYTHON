### esto es una interfaz grafica que permite conocer la naturaleza estadistica de una variables de un dataset de datos del abalone.

### PARA LA INTERFAZ
import tkinter as tkinter
import numpy as np

#PARA EL MANEJO DE DATOS
import pandas as pd

#PARA GRAFICAR
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from scipy import stats


## PARA LA REGRESION:
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

### esta es la primera función para realizar la figura estadistica de la entrada o entradas
### seleccionadas por el usuario
def graficar(Graph1,Variables_seleccion):
    variables_gra=[]
    archivo='abalone.csv'
    df = pd.read_csv(archivo)
    df.columns=["Sexo", "longitud", "Diametro", "Altura", "peso entero ", "Peso de la cascara", "Peso de las visceras", "peso del caparazón", "anillios"]
    # columnas=["Sexo", "longitud", "Diametro", "Altura", "peso entero ", "Peso de la cascara", "Peso de las visceras", "peso del caparazón", "anillios"]
    for i in range(0,len(Variables_seleccion)):
        if Variables_seleccion[i].get()==1:
            variables_gra.append(df.columns[i+1])
    #print(variables_gra) 
    if Graph1!=3 and len(variables_gra)==1:
        root2 = tkinter.Tk()   
        root2.title('gráfico con datos atípicos de ' + variables_gra[0])      
        fig = Figure()
     
        canvas = FigureCanvasTkAgg(fig, master=root2)  # A tk.DrawingArea.
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, root2)

        if Graph1==0:
            fig.clear()
            # fig.add_subplot(111).
            ax=fig.add_subplot(111)
            #print(df[variables_gra])
            ax.hist(x=df[variables_gra])
            ax.set_title('Histograma')
            ax.set_xlabel('Datos')
            ax.set_ylabel('Amplitud de los datos')
            canvas.draw_idle()
        elif Graph1==1:
            fig.clear()
            # fig.add_subplot(111).
            ax=fig.add_subplot(111)
            ax.boxplot(x=df[variables_gra]) 
            #print(df[variables_gra])
            ax.set_title('Diagrama de cajas y bigotes')
            ax.set_xlabel(variables_gra)
            ax.set_ylabel('Amplitud de los datos')
            canvas.draw_idle()
        elif Graph1==3:
            fig.clear()
            fig.add_subplot(111).hist(x=df[variables_gra], rwidth=0.85) 
            canvas.draw_idle()
        elif Graph1==2:
            fig.clear()
            ax=fig.add_subplot(111)
            res=stats.probplot(x=df[variables_gra[0]], dist=stats.norm, plot=ax)
            ax.set_title('Diagrama de normalización')
            ax.set_xlabel('Datos')
            ax.set_ylabel('Amplitud de los datos')
            canvas.draw_idle()
        button = tkinter.Button(root2,text = "Cerrar",command = root2.destroy).pack()
        root2.mainloop()
    elif Graph1!=3 and len(variables_gra)>=1:
       root3 = tkinter.Tk()   
       root3.title('¡AVISO IMPORTANTE')
       etiqueta1ve1=tkinter.Label(root3, text="POR FAVOR DEBE SELECCIONAR UNA SOLA ENTRADA").pack()
       button = tkinter.Button(root3,text = "Cerrar",command = root3.destroy).pack()
    elif Graph1==3 and len(variables_gra)==2:
       root2 = tkinter.Tk()   
       root2.title('gráfico con datos atípicos de '+ variables_gra[0] + ' con '+ variables_gra[1])      
       fig = Figure()
       canvas = FigureCanvasTkAgg(fig, master=root2)  # A tk.DrawingArea.
       canvas.get_tk_widget().pack()
       toolbar = NavigationToolbar2Tk(canvas, root2)
       fig.clear()
       ax=fig.add_subplot(111)
       ax.scatter((df[variables_gra[0]]),(df[variables_gra[1]]))
       ax.set_title('Diagrama de dispersión')
       ax.set_xlabel('Datos')
       ax.set_ylabel('Amplitud de los datos')
       canvas.draw_idle()
       
       canvas.draw_idle()
    elif Graph1==3 and len(variables_gra)>2:
       root3 = tkinter.Tk()   
       root3.title('¡AVISO IMPORTANTE')
       etiqueta1ve1=tkinter.Label(root3, text="POR FAVOR DEBE SELECCIONAR SOLAMENTE DOS ENTRADAS").pack()
       button = tkinter.Button(root3,text = "Cerrar",command = root3.destroy).pack()
    elif Graph1==3 and len(variables_gra)<2:
       root3 = tkinter.Tk()   
       root3.title('¡AVISO IMPORTANTE')
       etiqueta1ve1=tkinter.Label(root3, text="POR FAVOR DEBE SELECCIONAR DOS ENTRADAS").pack()
       button = tkinter.Button(root3,text = "Cerrar",command = root3.destroy).pack()    

### esta función me permite limpiar los datos atípicos del conjunto de datos con un valor preestablecido por el usuario en una caja de entrada de texto
## tener en cuenta que al ejecutar esta función se dibujará la figura estadistica que se enuentra seleccionada. 
def atipicos(entry,Variables_seleccion,Graph1):
    variables_gra=[]
    archivo='abalone.csv'
    df = pd.read_csv(archivo)
    df.columns=["Sexo", "longitud", "Diametro", "Altura", "peso entero ", "Peso de la cascara", "Peso de las visceras", "peso del caparazón", "anillios"]

    for i in range(0,len(Variables_seleccion)):
        if Variables_seleccion[i].get()==1:
            variables_gra.append(df.columns[i+1])
    #print(variables_gra)
    if len(variables_gra)>1 or len(variables_gra)==0:
       root3 = tkinter.Tk()   
       root3.title('¡AVISO IMPORTANTE')
       etiqueta1ve1=tkinter.Label(root3, text="POR FAVOR DEBE SELECCIONAR UNA SOLA ENTRADA").pack()
       button = tkinter.Button(root3,text = "Cerrar",command = root3.destroy).pack()
    else: 
        indexAtipicos=[]
        temp=np.array(df[variables_gra])
        temp2=np.quantile(temp, 0.25)-float(entry)*(np.quantile(temp, 0.75)-np.quantile(temp, 0.25))
        temp3=np.quantile(temp, 0.75)+float(entry)*(np.quantile(temp, 0.75)-np.quantile(temp, 0.25))
        #print(temp3)
        for i in range(0,len(df[variables_gra])):
            if temp[i]<temp2 or temp[i]>temp3:
                indexAtipicos.append(i)
        #print(indexAtipicos) 
        a=df[variables_gra[0]].drop(indexAtipicos,axis=0)
        root2 = tkinter.Tk()   
        root2.title('gráfico SIN datos atípicos del la columna de '+ variables_gra[0])      
        fig = Figure()
     
        canvas = FigureCanvasTkAgg(fig, master=root2)  # A tk.DrawingArea.
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, root2)

        if Graph1==0:
            fig.clear()
            ax=fig.add_subplot(111)
            ax.hist(x=a)
            ax.set_title('Histograma')
            ax.set_xlabel('Datos')
            ax.set_ylabel('Amplitud de los datos')
            canvas.draw_idle()
        elif Graph1==1:
            fig.clear()
            ax=fig.add_subplot(111)
            ax.boxplot(x=a) 
            ax.set_title('Cajas y bigotes')
            ax.set_xlabel('Datos')
            ax.set_ylabel('Amplitud de los datos')
            canvas.draw_idle()
        elif Graph1==3:
            root3 = tkinter.Tk()   
            root3.title('¡AVISO IMPORTANTE')
            etiqueta1ve1=tkinter.Label(root3, text="POR FAVOR DEBE SELECCIONAR UNA SOLA ENTRADA Y OTRO TIOPO DE GRAFICO").pack()
            button = tkinter.Button(root3,text = "Cerrar",command = root3.destroy).pack()
        elif Graph1==2:
            fig.clear()
            ax=fig.add_subplot(111)
            res=stats.probplot(a, dist=stats.norm, plot=ax)
            ax.set_title('Diagrama de normalización')
            ax.set_xlabel('Datos')
            ax.set_ylabel('Amplitud de los datos')
            canvas.draw_idle()
            
        button = tkinter.Button(root2,text = "Cerrar",command = root2.destroy).pack()
        root2.mainloop()

## esta función permite relaizar la regresión lineal de una variable de entrada y otra variable de salida si existe un valor escrito en la caja de texto se procederá a eliminar los atípicos primero
## luego se dibujará los datos reales con respecto a los datos proyectados y debajo de ellos se podrá visualizar una métrica de desempeño cabe resaltar que todos los gráficos son interactivos.
def regresion(entry,Variables_seleccioninput,Variables_seleccionoutput):
    variables_input=[]
    variables_output=[]
    archivo='abalone.csv'
    df = pd.read_csv(archivo)
    df.columns=["Sex", "Length", "Diameter", "Height", "Whole weight ", "Shucked weight", "Viscera weight", "Shell weight", "Rings"]

    for i in range(0,len(Variables_seleccioninput)):
        if Variables_seleccioninput[i].get()==1:
            variables_input.append(df.columns[i+1])
    # #print(variables_input)
    
    for i in range(0,len(Variables_seleccionoutput)):
        if Variables_seleccionoutput[i].get()==1:
           variables_output.append(df.columns[i+1])
    # #print(variables_output)
    if(entry!=0):
        indexAtipicos=[]
        temp=np.array(df[variables_input])
        temp2=np.quantile(temp, 0.25)-float(entry)*(np.quantile(temp, 0.75)-np.quantile(temp, 0.25))
        temp3=np.quantile(temp, 0.75)+float(entry)*(np.quantile(temp, 0.75)-np.quantile(temp, 0.25))
        
        for i in range(0,len(temp)):
            if temp[i]<temp2 or temp[i]>temp3:
                indexAtipicos.append(i)
        # ##print(indexAtipicos) 
        a=df[variables_input].drop(indexAtipicos,axis=0)    
        b=df[variables_output].drop(indexAtipicos,axis=0)  
        x=a
        y=b
    else:
        a=df[variables_input]  
        b=df[variables_output]
        x=a
        y=b
    X_train, X_test, y_train, y_test = train_test_split(x,y,train_size= 0.5)
    
    modelo = LinearRegression()
    modelo.fit(X = np.array(X_train).reshape(-1, 1), y = y_train)
    predicciones = modelo.predict(X =(X_test))
    fig = Figure()
    root2 = tkinter.Tk()
    root2.title('Regresión entre los datos de '+ variables_input[0] + ''+ 'y '+ variables_output[0])     
    canvas = FigureCanvasTkAgg(fig, master=root2)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, root2)
    
    fig.clear()
    ax=fig.add_subplot(111)
    ax.plot(np.array(y_test).reshape(-1,1),'r--',np.array(predicciones).reshape(-1,1),'g--')
    ax.set_title('Comparación entre los datos reales y aproximados')
    ax.set_xlabel('Datos')
    ax.set_ylabel('Amplitud de los datos')
    ax.legend(["datos reales", "datos aproximados"], loc ="lower right")
    canvas.draw_idle()
    button = tkinter.Button(root2,text = "Cerrar",command = root2.destroy).pack()
    rmse = mean_squared_error(y_true  = y_test, y_pred  = predicciones)
    temp='el valor del rmse  es '+str(rmse)
    etiquetaregre1=tkinter.Label(root2, text=temp).pack()

    root2.mainloop()

### toda esta partes ya corresponde a la realización de la interfaz.  
window_width = 5
window_height = 5

root = tkinter.Tk()   
root.title("REGRESION CON DATA DE ABALONES")
        
etiqueta1=tkinter.Label(root, text="Grafica con atípicos")
etiqueta1.grid(row=0, column=0)

# text_widget = tkinter.Text(root,width=29, height=5)
# text_widget.insert(tkinter.END,"En esta sección se puede seleccionar el tipo de gráfico estadístico para ver el comportamiento de una variable de datos. Estas se puede elegir una o dos a la vez")
# text_widget.grid(row=1, column=0)
# etiqueta2=tkinter.Label(root, text="En esta sección se puede seleccionar el tipo de gráfico estadistico para ver")
# etiqueta2.grid(row=1, column=0)
      
etiqueta2=tkinter.Label(root, text="Tipo de grafico")
etiqueta2.grid(row=0, column=2)
        
Graph1=tkinter.IntVar()

che1 = tkinter.Radiobutton(root, text='Histograma',variable=Graph1, value=0) 
che1.grid(row=1, column=2)

che2 = tkinter.Radiobutton(root, text='Boxplot',variable=Graph1, value=1) 
che2.grid(row=1, column=3)

che3 = tkinter.Radiobutton(root, text='Normalización',variable=Graph1, value=2) 
che3.grid(row=2, column=2)

che4 = tkinter.Radiobutton(root, text='Disperción',variable=Graph1, value=3) 
che4.grid(row=2, column=3)

Longitud=tkinter.IntVar()
Diametro=tkinter.IntVar()
Altura=tkinter.IntVar()
peso_entero=tkinter.IntVar()
peso_cascara=tkinter.IntVar()
peso_vispera=tkinter.IntVar()
peso_caparazon=tkinter.IntVar()
anillos=tkinter.IntVar()

etiqueta3=tkinter.Label(root, text="")
etiqueta3.grid(pady=5,padx=5,row=0,column=1)
        
etiqueta3=tkinter.Label(root, text="Variables de entrada")
etiqueta3.grid(row=3, column=2)

che1=tkinter.Checkbutton(root,text = "Longitud", variable = Longitud, onvalue = 1, offvalue = 0, height=1, width = 20)
che1.grid(row=4, column=2)
che2=tkinter.Checkbutton(root,text = "Diametro", variable = Diametro, onvalue = 1, offvalue = 0, height=1, width = 20)
che2.grid(row=4, column=3)
che3=tkinter.Checkbutton(root,text = "Altura", variable = Altura, onvalue = 1, offvalue = 0, height=1, width = 20)
che3.grid(row=4, column=4)

che4=tkinter.Checkbutton(root,text = "peso entero", variable = peso_entero, onvalue = 1, offvalue = 0, height=1, width = 20)
che4.grid(row=5, column=2)
che5=tkinter.Checkbutton(root,text = "peso cascara", variable = peso_cascara, onvalue = 1, offvalue = 0, height=1, width = 20)
che5.grid(row=5, column=3)
che6=tkinter.Checkbutton(root,text = "peso viseras", variable = peso_vispera, onvalue = 1, offvalue = 0, height=1, width = 20)
che6.grid(row=5, column=4)

che7=tkinter.Checkbutton(root,text = "peso caparazon", variable = peso_caparazon, onvalue = 1, offvalue = 0, height=1, width = 20)
che7.grid(row=6, column=2)
che8=tkinter.Checkbutton(root,text = "# de anillos", variable = anillos, onvalue = 1, offvalue = 0, height=1, width = 20)
che8.grid(row=6, column=3)

Variables_seleccion=[Longitud,Diametro,Altura,peso_entero,peso_cascara,peso_vispera,peso_caparazon,anillos]
boton_graficasSinATIPICOS = tkinter.Button(text="Graficar los datos originales",command=lambda:graficar(Graph1.get(),Variables_seleccion ))
boton_graficasSinATIPICOS.grid(row=6, column=4)


etiqueta4=tkinter.Label(root, text="Gráfica sin atípicos")
etiqueta4.grid(row=8, column=0)

# text_widget2 = tkinter.Text(root,width=29, height=2)
# text_widget2.insert(tkinter.END,"El valor de alfa permite borrar más o menos atípicos")
# text_widget2.grid(row=8, column=1) 

etiquetaesp=tkinter.Label(root, text="")
etiquetaesp.grid(pady=5,padx=5,row=8, column=1)

etiquetaalfa=tkinter.Label(root, text="Valor del factor de alfa para los atípicos")
etiquetaalfa.grid(pady=5,padx=5,row=8, column=2)

var = tkinter.IntVar()
entry = tkinter.Entry(root, width=20, textvariable=var)
entry.grid(row=8, column=3)

boton_graficasSinATIPICOS = tkinter.Button(text="Eliminar atípicos",command=lambda:atipicos(entry.get(),Variables_seleccion,Graph1.get()))
boton_graficasSinATIPICOS.grid(row=8, column=4)

### regresión 

etiqueta4=tkinter.Label(root, text="REGRESIÓN")
etiqueta4.grid(row=9, column=0)

# text_widget2 = tkinter.Text(root,width=29, height=5)
# text_widget2.insert(tkinter.END,"En esta sección se creara un modelo de regresión de una sola entrada y se comparará los datos reales con los obtenidos por el modelo")
# text_widget2.grid(row=9, column=1)

etiquetaesp=tkinter.Label(root, text="")
etiquetaesp.grid(pady=5,padx=5,row=11, column=1)

etiquetaalfa=tkinter.Label(root, text="ENTRADAS") 
etiquetaalfa.grid(pady=5,padx=5,row=9, column=2)

etiquetaalfa=tkinter.Label(root, text="SALIDA") 
etiquetaalfa.grid(pady=5,padx=5,row=9, column=3)

Longitudinput=tkinter.IntVar()
Diametroinput=tkinter.IntVar()
Alturainput=tkinter.IntVar()
peso_enteroinput=tkinter.IntVar()
peso_cascarainput=tkinter.IntVar()
peso_visperanput=tkinter.IntVar()
peso_caparazoninput=tkinter.IntVar()
anillosinput=tkinter.IntVar()

che1=tkinter.Checkbutton(root,text = "Longitud", variable = Longitudinput, onvalue = 1, offvalue = 0, height=1, width = 20)
che1.grid(row=10, column=2)
che2=tkinter.Checkbutton(root,text = "Diametro", variable = Diametroinput, onvalue = 1, offvalue = 0, height=1, width = 20)
che2.grid(row=11, column=2)
che3=tkinter.Checkbutton(root,text = "Altura", variable = Alturainput, onvalue = 1, offvalue = 0, height=1, width = 20)
che3.grid(row=12, column=2)

che4=tkinter.Checkbutton(root,text = "peso entero", variable = peso_enteroinput, onvalue = 1, offvalue = 0, height=1, width = 20)
che4.grid(row=13, column=2)
che5=tkinter.Checkbutton(root,text = "peso cascara", variable = peso_cascarainput, onvalue = 1, offvalue = 0, height=1, width = 20)
che5.grid(row=14, column=2)
che6=tkinter.Checkbutton(root,text = "peso viseras", variable = peso_visperanput, onvalue = 1, offvalue = 0, height=1, width = 20)
che6.grid(row=15, column=2)

che7=tkinter.Checkbutton(root,text = "peso caparazon", variable = peso_caparazoninput, onvalue = 1, offvalue = 0, height=1, width = 20)
che7.grid(row=16, column=2)
che8=tkinter.Checkbutton(root,text = "# de anillos", variable = anillosinput, onvalue = 1, offvalue = 0, height=1, width = 20)
che8.grid(row=17, column=2)

Variables_seleccioninput=[Longitudinput,Diametroinput,Alturainput,peso_enteroinput,peso_cascarainput,peso_visperanput,peso_caparazoninput,anillosinput]


Longitudoutput=tkinter.IntVar()
Diametrooutput=tkinter.IntVar()
Alturaoutput=tkinter.IntVar()
peso_enterooutput=tkinter.IntVar()
peso_cascaraoutput=tkinter.IntVar()
peso_visperaoutput=tkinter.IntVar()
peso_caparazonoutput=tkinter.IntVar()
anillosoutput=tkinter.IntVar()

che1=tkinter.Checkbutton(root,text = "Longitud", variable = Longitudoutput, onvalue = 1, offvalue = 0, height=1, width = 20)
che1.grid(row=10, column=3)
che2=tkinter.Checkbutton(root,text = "Diametro", variable = Diametrooutput, onvalue = 1, offvalue = 0, height=1, width = 20)
che2.grid(row=11, column=3)
che3=tkinter.Checkbutton(root,text = "Altura", variable = Alturaoutput, onvalue = 1, offvalue = 0, height=1, width = 20)
che3.grid(row=12, column=3)

che4=tkinter.Checkbutton(root,text = "peso entero", variable = peso_enterooutput, onvalue = 1, offvalue = 0, height=1, width = 20)
che4.grid(row=13, column=3)
che5=tkinter.Checkbutton(root,text = "peso cascara", variable = peso_cascaraoutput, onvalue = 1, offvalue = 0, height=1, width = 20)
che5.grid(row=14, column=3)
che6=tkinter.Checkbutton(root,text = "peso viseras", variable = peso_visperaoutput, onvalue = 1, offvalue = 0, height=1, width = 20)
che6.grid(row=15, column=3)

che7=tkinter.Checkbutton(root,text = "peso caparazon", variable = peso_caparazonoutput, onvalue = 1, offvalue = 0, height=1, width = 20)
che7.grid(row=16, column=3)
che8=tkinter.Checkbutton(root,text = "# de anillos", variable = anillosoutput, onvalue = 1, offvalue = 0, height=1, width = 20)
che8.grid(row=17, column=3)

Variables_seleccionoutput=[Longitudoutput,Diametrooutput,Alturaoutput,peso_enterooutput,peso_cascaraoutput,peso_visperaoutput,peso_caparazonoutput,anillosoutput]

boton_graficasSinATIPICOS = tkinter.Button(text="Obtener regresión",command=lambda:regresion(entry.get(),Variables_seleccioninput,Variables_seleccionoutput))
boton_graficasSinATIPICOS.grid(row=20, column=3)


root.mainloop()
