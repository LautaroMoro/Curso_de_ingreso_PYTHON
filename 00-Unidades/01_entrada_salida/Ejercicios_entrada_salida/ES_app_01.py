import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Lautaro
apellido:Moro
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        dolar_oficial = prompt("Dolar oficial", "INGRESE EL VALOR ACTUAL DEL DOLAR OFICIAL")

        dolar_blue = prompt("Dolar blue", "INGRESE EL VALOR ACTUAL DEL DOLAR BLUE")

        dolar_oficial = float(dolar_oficial)

        dolar_blue = float(dolar_blue)

        diferencia_de_cotizaciones = (dolar_blue - dolar_oficial)

        porcentaje = (diferencia_de_cotizaciones / dolar_oficial)
        
        porcentaje = (porcentaje * 100)

        alert("Cotizaciones", f"La diferencia de cotizaciones entre el dolar blue y el oficial es del : {porcentaje}%")

        

        



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
