import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Lautaro
apellido:Moro
---
TP: ES_Pinturas
---
Enunciado:

2.	Para el departamento de Pinturas:
	A.	Al ingresar una temperatura en Fahrenheit debemos mostrar la temperatura en Centígrados con un mensaje concatenado 
        (0 °F − 32) × 5/9 = -17,78 °C

    B.	Al ingresar una temperatura en Centígrados debemos mostrar la temperatura en Fahrenheit 
        (0 °C × 9/5) + 32 = 32 °F

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Temperatura °C")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_temperatura_c = customtkinter.CTkEntry(master=self)
        self.txt_temperatura_c.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Temperatura °F")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_temperatura_f = customtkinter.CTkEntry(master=self)
        self.txt_temperatura_f.grid(row=1, column=1)
       
        self.btn_convertir_c_f = customtkinter.CTkButton(master=self, text="Convertir °C a °F", command=self.btn_convertir_c_f_on_click)
        self.btn_convertir_c_f.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_convertir_f_c = customtkinter.CTkButton(master=self, text="Convertir °F a °C", command=self.btn_convertir_f_c_on_click)
        self.btn_convertir_f_c.grid(row=4, pady=10, columnspan=2, sticky="nsew")
    
    def btn_convertir_c_f_on_click(self):

        centigrados = self.txt_temperatura_c.get()
        centigrados = float(centigrados)

        conversion_c_f = self.btn_convertir_c_f

        conversion_c_f = (centigrados * 9 / 5) + 32
        farenheit_round = round(conversion_c_f, 1)

        alert("UTN", f"({centigrados} * 9 / 5) + 32 = {farenheit_round}")
        
    def btn_convertir_f_c_on_click(self):
        farenheit = self.txt_temperatura_f.get()
        farenheit = float(farenheit)

        conversion_f_c = self.btn_convertir_f_c

        conversion_f_c = (farenheit - 32) * 5 / 9
        centigrados_round = round(conversion_f_c, 1)

        alert("UTN", f"({farenheit} - 32) * 5 / 9  = {centigrados_round}")



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()