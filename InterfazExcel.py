from tkinter import filedialog
from tkinter import *
import os
import pandas as pd

# Crear una clase
class VentanaEjemplo:
    def __init__(self, master):
        self.master = master
        
        # titulo del programa
        master.title("Convertidor de CSV a JSON")
        
        # Muestra una etiqueta
        self.etiqueta = Label(master, text="la primera ventana!")
        self.etiqueta.pack()
        
        # boton para mostrar un texto
        self.botonSaludo = Button(master, text="Saludar", command=self.saludar)
        self.botonSaludo.pack()
        
        # boton para leer un CSV las primeras 5 lineas
        self.botonFiles = Button(master, text="Archivos", command=self.archivos)
        self.botonFiles.pack()
        
        # boton que convierte un CSV a Json
        self.botonFiles = Button(master, text="CSV a Json", command=self.tojson)
        self.botonFiles.pack()
        
        # obtener la ruta donde se guarda el json
        self.etiqueta = Label(master, text= "")
        self.etiqueta.pack()
        
        # boton de cerrar el programa
        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()
        
# boton para saludar :D
    def saludar(self):
        print("Hola bon dia =D")

# function de abrir un archivo
    def archivos(self):
        root = Tk()
        root.filename = filedialog.askopenfilename(initialdir="/", title="Selecciona un archivo", defaultextension="*.*")
        archivo = root.filename

        df = pd.read_csv(archivo)
        # Establecer los nombres de las columnas
        if archivo == "iris.csv":
            nombres = ['longitud_sepalo', 'ancho_sepalo', 'longitud_petalo', 'ancho_petalo', 'clase']
            df.columns = nombres

        print(df.head())


    # function para convertir CSV a Json
    def tojson(self):
        roota = Tk()
        roota.filename = filedialog.askopenfilename(initialdir="/", title="Selecciona un archivo", defaultextension="*.*")
        archivocsv = roota.filename
        
        # guardar los datos del csv
        csv_data = pd.read_csv(archivocsv, sep=",")
        # Aquí se obriene la ruta del usuario donde quiera guardarlo
        archivo_guardado = filedialog.asksaveasfilename(initialdir="/", title="Seleciona donde guardar", defaultextension="*.*")
        ruta_usuario= open(archivo_guardado,"w")
        # convertimos el csv a json y usamos la ruta de antes para guardar los datos
        csv_data.to_json(ruta_usuario, orient="records")

        # prueba ruta manual
        # csv_data.to_json("C:\\Users\\dchirinos\\Documents\\Python proyects\\data\\sida1.json", orient="records")
        print("se ha creado el archivo JSON en: ", archivo_guardado)
        texto_variable = archivo_guardado
        self.etiqueta.configure(text="se ha guardado en: " + texto_variable)   
    
root = Tk()
root.geometry("500x300+560+240")
miVentana = VentanaEjemplo(root)
root.mainloop()