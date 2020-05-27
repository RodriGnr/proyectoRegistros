from tkinter import*
from tkinter import messagebox
from tkinter import ttk

#Inicio Interfaz
registro = Tk()
registro.title('Registro De Usuario')
registro.geometry('430x500')
registro.resizable(0,0)
Canvas(registro, width=423, height=493, relief="groove", borderwidth=2).place(x=0, y=0)

#Labels fijos(NO TOCAR)
Label(registro, text="--------------------------------- DATOS PERSONALES ---------------------------------", font=("Arial", 10)).place(x=10, y=10)

Label(registro, text="Nombres", borderwidth=2, width=18, font=("Arial", 12), relief="groove").place(x=10, y=40)
Label(registro, text="Apellidos", borderwidth=2, width=18, font=("Arial", 12), relief="groove").place(x=10, y=70)
Label(registro, text="DNI", borderwidth=2, width=18, font=("Arial", 12), relief="groove").place(x=10, y=100)
Label(registro, text="Fecha De Nacimiento", borderwidth=2, width=18, font=("Arial", 12), relief="groove").place(x=10, y=130)
Label(registro, text="Domicilio", borderwidth=2, width=18, font=("Arial", 12), relief="groove").place(x=10, y=160)
Label(registro, text="Nro. Telefono", borderwidth=2, width=18, font=("Arial", 12), relief="groove").place(x=10, y=190)

Label(registro, text="----------------------------------- DATOS DE CUENTA -----------------------------------", font=("Arial", 10)).place(x=10, y=220)

Label(registro, text="Correo Electronico", borderwidth=2, width=18, font=("Arial", 12), relief="groove").place(x=10, y=250)
Label(registro, text="Contraseña", borderwidth=2, width=18, font=("Arial", 12), relief="groove").place(x=10, y=280)
Label(registro, text="Repita La Contraseña", borderwidth=2, width=18, font=("Arial", 12), relief="groove").place(x=10, y=310)

Label(registro, text="Dia:", font=("Arial", 10)).place(x=185, y=130)
Label(registro, text="Mes:", font=("Arial", 10)).place(x=260, y=130)
Label(registro, text="Año:", font=("Arial", 10)).place(x=337, y=130)

Label(registro, text="Ya Tiene Cuenta? -------->", font=("Arial", 12)).place(x=10, y=430)

#Entrys
    #------------------DATOS PERSONALES---------------------
ent_nombre = Entry(registro, width=39, borderwidth=2)
ent_nombre.place(x=180, y=41)
ent_apellidos = Entry(registro, width=39, borderwidth=2)
ent_apellidos.place(x=180, y=71)
ent_dni = Entry(registro, width=39, borderwidth=2)
ent_dni.place(x=180, y=101)
ent_domicilio = Entry(registro, width=39, borderwidth=2)
ent_domicilio.place(x=180, y=161)
ent_telefono = Entry(registro, width=39, borderwidth=2)
ent_telefono.place(x=180, y=191)
    #Combobox Fecha Nacimiento
cmb_dia = ttk.Combobox(registro,width=3)
cmb_dia.place(x=215, y=131)
cmb_mes = ttk.Combobox(registro,width=3)
cmb_mes.place(x=295, y=131)
cmb_año = ttk.Combobox(registro,width=5)
cmb_año.place(x=368, y=131)

    #------------------DATOS DE CUENTA------------------
ent_correo = Entry(registro, width=39, borderwidth=2)
ent_correo.place(x=180, y=251)
ent_contraseña = Entry(registro, width=39, borderwidth=2)
ent_contraseña.place(x=180, y=281)
ent_repContra = Entry(registro, width=39, borderwidth=2)
ent_repContra.place(x=180, y=311)

#Botones

btn_registrar = Button(registro, text="Registrar Usuario", font="Arial", cursor="hand2", borderwidth=5, relief="ridge", width=43)
btn_registrar.place(x=12, y=360)
btn_incioSesion = Button(registro, text="Iniciar Sesion", font="Arial", cursor="hand2", borderwidth=5, relief="ridge", width=21)
btn_incioSesion.place(x=202, y=423)

registro.mainloop()