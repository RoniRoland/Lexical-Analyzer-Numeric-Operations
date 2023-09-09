import tkinter as tk
from tkinter import filedialog
from analizador import Analizador


class App:
    ANCHO = 589
    ALTO = 1189

    def __init__(self):
        # Crear la ventana principal
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Proyecto 1 - Analizador Lexico")
        self.ventana_principal.geometry(f"{App.ALTO}x{App.ANCHO}")
        self.ventana_principal.configure(bg="#212325")

        self.text_area = tk.Text(self.ventana_principal)
        self.text_area.pack(fill=tk.BOTH, expand=True, side="right")
        self.text_area.configure(background="#23262e", foreground="white")
        self.file_path = None

        # Crear el marco para los botones de "Archivo"
        self.marco_archivo = tk.LabelFrame(
            self.ventana_principal,
            text="Archivo",
            font=("Roboto Medium", 20),
            background="#263238",
            foreground="white",
        )
        self.marco_archivo.pack(
            side="left", fill="both", expand="yes", padx=30, pady=30
        )
        self.marco_archivo.configure(bg="#263238")

        # Crear los botones de "Archivo"
        self.boton_abrir = tk.Button(
            master=self.marco_archivo,
            text="Abrir",
            font=("Roboto Medium", 11),
            bg="#1BDBD1",
            activebackground="#0059b3",
            foreground="white",
            activeforeground="white",
            width=15,
            height=1,
            command=self.abrir,
        )
        self.boton_abrir.pack(side="top", pady=25)

        self.boton_guardar = tk.Button(
            self.marco_archivo,
            text="Guardar",
            font=("Roboto Medium", 11),
            bg="#6F16FD",
            activebackground="#0059b3",
            foreground="white",
            activeforeground="white",
            width=15,
            height=1,
            command=self.guardar,
        )
        self.boton_guardar.pack(side="top", pady=25)

        self.boton_guardar_como = tk.Button(
            self.marco_archivo,
            text="Guardar Como",
            font=("Roboto Medium", 11),
            bg="#0059b3",
            activebackground="#0059b3",
            foreground="white",
            activeforeground="white",
            width=15,
            height=1,
            command=self.guardar_como,
        )
        self.boton_guardar_como.pack(side="top", pady=25)

        self.boton_analizar = tk.Button(
            self.marco_archivo,
            text="Analizar",
            font=("Roboto Medium", 11),
            bg="#0059b3",
            activebackground="#0059b3",
            foreground="white",
            activeforeground="white",
            width=15,
            height=1,
            command=self.analizar,
        )
        self.boton_analizar.pack(side="top", pady=25)

        self.boton_errores = tk.Button(
            self.marco_archivo,
            text="Errores",
            font=("Roboto Medium", 11),
            bg="#0059b3",
            activebackground="#0059b3",
            foreground="white",
            activeforeground="white",
            width=15,
            height=1,
            command=self.errores,
        )
        self.boton_errores.pack(side="top", pady=25)

        self.boton_salir = tk.Button(
            self.marco_archivo,
            text="Salir",
            font=("Roboto Medium", 11),
            bg="#D35B58",
            activebackground="#D35B58",
            foreground="white",
            activeforeground="white",
            width=15,
            height=1,
            command=self.salir,
        )
        self.boton_salir.pack(side="top", pady=25)

    def abrir(self):
        global lineas
        lineas = ""
        formatos = (
            ("form files", ".json"),
            ("form files", ".txt"),
        )
        self.file_path = None
        self.file_path = filedialog.askopenfilename(
            defaultextension=".txt", filetypes=formatos
        )
        if self.file_path:
            archivo = open(self.file_path, "r")

            # Abre el archivo y pega el texto en el area de texto
            for i in archivo.readlines():
                lineas += i
            print(lineas)
            self.text_area.delete("1.0", tk.END)  # limpia el area de texto
            self.text_area.insert(tk.END, lineas)

    def guardar(self):
        if self.file_path:
            with open(self.file_path, "w") as file:
                # obtiene el texto nuevo que se añade
                updated_text_data = self.text_area.get("1.0", tk.END)
                # escribe el nuevo texto en el archivo
                file.write(updated_text_data)

    def guardar_como(self):
        formatos = (
            ("form files", ".json"),
            ("form files", ".txt"),
        )
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=formatos
        )
        if file_path:
            self.file_path = file_path
            self.ventana_principal.title(self.file_path)
            self.guardar()

    def analizar(self):
        pass

    def errores(self):
        # Aquí iría el código para la opción "Errores"
        pass

    def salir(self):
        # Cierra la ventana principal
        self.ventana_principal.destroy()


if __name__ == "__main__":
    app = App()
    app.ventana_principal.mainloop()
