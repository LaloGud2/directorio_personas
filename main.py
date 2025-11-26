import tkinter as tk 
from tkinter import messagebox
from directorio import inicializar_csv, guardar_persona

ventana = None
entrada_nombre = None
entrada_numero = None
entrada_estado = None
etiqueta_estado = None
def limpiar_campos():
    entrada_nombre.delete(0, tk.END)
    entrada_numero.delete(0, tk.END)
    etiqueta_estado.config(text="")
    entrada_nombre.focus()

def agregar_persona():
    print("entra a la funcion agregar persona")
    nombre = entrada_nombre.get()
    numero = entrada_numero.get()
    print(nombre,numero)
    
    if not nombre or not numero:
        messagebox.showwarning("Error, debe llenar ambos campos")
        
        if guardar_persona(nombre,numero):
            etiqueta_estado.config(text=f"agregado: {nombre}")
            entrada_nombre.delete(0, tk.END)
            entrada_numero.delete(0, tk.END)
            ventana.after(5000,lambda: etiqueta_estado.config(text=""))
        else:
            messagebox.showerror("error","no se pudo guardar")
def limpiar_campos():
    print("entra a la funcion de limpiar campos")
          
def construir_interfaz():
    global ventana, entrada_nombre, entrada_numero, etiqueta_estado
    ventana = tk.Tk()
    ventana.title("directorio")
    
    etiqueta_nombre = tk.Label(ventana,text="")
    etiqueta_nombre.pack()
    etiqueta_nombre = tk.Label(ventana,text="nombre")
    etiqueta_nombre.pack()
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.pack()
    
    etiqueta_numero = tk.Label(ventana, text="Numero:")
    etiqueta_numero.pack()
    entrada_numero = tk.Entry(ventana)
    entrada_numero.pack()
    boton_agregar = tk.Button(ventana, text="agregar persona",command=agregar_persona)
    boton_agregar.pack()
    
    boton_limpiar = tk.Button(ventana, text="limpiar campos",command=limpiar_campos)
    boton_limpiar.pack()
    

    
def main():
    inicializar_csv()
    construir_interfaz()
    ventana.mainloop()
    
if __name__ =="__main__":
    main()
