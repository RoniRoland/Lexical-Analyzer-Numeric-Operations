import tkinter as tk
from tkinter import filedialog
from analizador import Analizador
import math
from tkinter import messagebox


class App:
    ANCHO = 710
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

        self.boton_reporte = tk.Button(
            self.marco_archivo,
            text="Reporte",
            font=("Roboto Medium", 11),
            bg="#0059b3",
            activebackground="#0059b3",
            foreground="white",
            activeforeground="white",
            width=15,
            height=1,
            command=self.reporte,
        )
        self.boton_reporte.pack(side="top", pady=25)

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
            self.text_area.delete("1.0", tk.END)  # limpia el area de texto
            self.text_area.insert(tk.END, lineas)

            # Muestra el mensaje de archivo cargado exitosamente
            messagebox.showinfo(
                "Archivo Cargado", "El archivo se ha cargado exitosamente."
            )

    def guardar(self):
        if self.file_path:
            with open(self.file_path, "w") as file:
                # obtiene el texto nuevo que se añade
                updated_text_data = self.text_area.get("1.0", tk.END)
                # escribe el nuevo texto en el archivo
                file.write(updated_text_data)

            # Muestra el mensaje de guardado exitoso
            messagebox.showinfo(
                "Guardado Correctamente", "El archivo se ha guardado correctamente."
            )
        else:
            # Muestra un mensaje de advertencia si no hay archivo abierto
            messagebox.showwarning(
                "Archivo no seleccionado",
                "Por favor, abra un archivo antes de guardar.",
            )

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

    def reconocerOperacion(self, lista):
        resultado = 0
        tipoOperacion = lista[3].lexema
        (numero1, lista) = self.obtenerValor(lista[7:])

        if lista[0].lexema == ",":  # Viene otro valor
            (numero2, lista) = self.obtenerValor(lista[3:])

            if tipoOperacion == '"suma"':
                resultado = numero1 + numero2
                print(numero1, "+", numero2, "=", resultado)
            elif tipoOperacion == '"resta"':
                resultado = numero1 - numero2
                # print(numero1, "-", numero2, "=", resultado)
            elif tipoOperacion == '"multiplicacion"':
                resultado = numero1 * numero2
            elif tipoOperacion == '"division"':
                resultado = numero1 / numero2
            elif tipoOperacion == '"potencia"':
                resultado = numero1**numero2

            elif tipoOperacion == '"mod"':
                resultado = numero1 % numero2

        else:  # Viene solo 1 valor
            if tipoOperacion == '"raiz"':
                resultado = math.sqrt(numero1)
            elif tipoOperacion == '"inverso"':
                resultado = 1 / numero1
            elif tipoOperacion == '"seno"':
                radianes = math.radians(numero1)
                resultado = math.sin(radianes)
            elif tipoOperacion == '"coseno"':
                radianes = math.radians(numero1)
                resultado = math.cos(radianes)
            elif tipoOperacion == '"tangente"':
                radianes = math.radians(numero1)
                resultado = math.tan(radianes)

        # En la lista se retira la llave que cierra la operación
        return (resultado, lista[1:])

    def obtenerValor(self, lista):
        numeroFinal = 0
        listaNueva = []
        try:  # si guardaron el tipo de token no es necesario el try except, sería solo un IF
            numeroFinal = float(lista[0].lexema)
            listaNueva = lista[1:]
        except:  # Operacion anidada
            # Estructura de una anidada: [ { operacion, valor1, valor2 } ]
            # Para enviarlo como operación primero se quita el corchete de apertura
            (numeroFinal, lista) = self.reconocerOperacion(lista[1:])
            # Luego se quita el corchete de cierre
            listaNueva = lista[1:]

        return (numeroFinal, listaNueva)

    def analizar(self):
        global lineas
        lineas = ""
        if self.file_path:
            with open(self.file_path, "r") as archivo:
                for i in archivo.readlines():
                    lineas += i
            self.text_area.delete("1.0", tk.END)  # limpia el área de texto
            self.text_area.insert(tk.END, lineas)

            # Ahora, puedes crear una instancia de Analizador con el contenido del archivo
            lexer = Analizador(lineas)
            lexer.analizar()
            lista = lexer.tokens_reconocidos[4:]
            estado = "operaciones"
            contador = 0

            # Limpia el área de texto antes de mostrar los resultados
            self.text_area.delete("1.0", tk.END)

            # Muestra los tokens en el área de texto
            self.text_area.insert(
                tk.END,
                "--------------------------- Tokens ---------------------------\n",
            )
            for token in lexer.tokens_reconocidos:
                self.text_area.insert(tk.END, str(token) + "\n")
            # Muestra el mensaje de análisis completado correctamente
            messagebox.showinfo(
                "Análisis Completado", "El análisis se ha completado correctamente."
            )
        else:
            messagebox.showwarning(
                "Archivo no cargado",
                "Por favor, cargue un archivo antes de realizar el análisis.",
            )
            return  # Salir de la función si no hay archivo cargado

            self.text_area.insert(
                tk.END,
                "--------------------------- OPERACIONES ---------------------------\n",
            )

            while True:
                if len(lista) == 0:
                    break

                if estado == "operaciones":
                    (resultado, lista) = self.reconocerOperacion(lista)

                    contador += 1
                    # print("Resultado operación", contador, ":", resultado)
                    resultado_str = f"Resultado operación {contador}: {resultado}\n"
                    self.text_area.insert(tk.END, resultado_str)  # Mostrar resultado

                    if lista[0].lexema == "]":  # Terminan las operaciones
                        estado = "configuraciones"
                        lista = lista[
                            2:
                        ]  # Se quita el token con el corchete de cierre la lista de operaciones y la coma
                    else:  # Viene otra operación
                        lista = lista[
                            1:
                        ]  # Se quita el token coma que separa la sig operación
                elif estado == "configuraciones":
                    break  # Termina porque configuraciones es lo último

            self.text_area.insert(
                tk.END,
                "--------------------------- OPERACIONES ---------------------------\n",
            )

            while True:
                if len(lista) == 0:
                    break

                if estado == "operaciones":
                    (resultado, lista) = self.reconocerOperacion(lista)

                    contador += 1
                    # print("Resultado operación", contador, ":", resultado)
                    resultado_str = f"Resultado operación {contador}: {resultado}\n"
                    self.text_area.insert(tk.END, resultado_str)  # Mostrar resultado

                    if lista[0].lexema == "]":  # Terminan las operaciones
                        estado = "configuraciones"
                        lista = lista[
                            2:
                        ]  # Se quita el token con el corchete de cierre la lista de operaciones y la coma
                    else:  # Viene otra operación
                        lista = lista[
                            1:
                        ]  # Se quita el token coma que separa la sig operación
                elif estado == "configuraciones":
                    break  # Termina porque configuraciones es lo último

    def errores(self):
        global lineas
        lineas = ""
        if self.file_path:
            with open(self.file_path, "r") as archivo:
                for i in archivo.readlines():
                    lineas += i
            self.text_area.delete("1.0", tk.END)  # limpia el área de texto
            self.text_area.insert(tk.END, lineas)

            # Ahora, puedes crear una instancia de Analizador con el contenido del archivo
            lexer = Analizador(lineas)
            lexer.analizar()

            # Limpia el área de texto antes de mostrar los resultados
            self.text_area.delete("1.0", tk.END)

            # Muestra los errores en el área de texto
            self.text_area.insert(
                tk.END,
                "--------------------------- Errores ---------------------------\n",
            )
            for error in lexer.errores:
                self.text_area.insert(tk.END, str(error) + "\n")

            if not lexer.errores:
                # Si no hay errores, mostrar un mensaje
                messagebox.showinfo(
                    "Sin Errores", "No se encontraron errores en el código."
                )
                return  # Salir de la función si no hay errores

            # Construye la estructura de errores como un diccionario
            errores_dict = {
                "errores": [
                    {
                        "No": idx + 1,
                        "descripcion": {
                            "lexema": error.lexema,
                            "tipo": error.tipo,
                            "columna": error.columna,
                            "fila": error.fila,
                        },
                    }
                    for idx, error in enumerate(lexer.errores)
                ]
            }

            # Convierte la estructura de errores a una cadena JSON manualmente
            errores_json_str = "{\n"
            errores_json_str += '    "errores": [\n'
            for i, error in enumerate(errores_dict["errores"]):
                errores_json_str += "        {\n"
                errores_json_str += f'            "No": {error["No"]},\n'
                errores_json_str += '            "descripcion": {\n'
                errores_json_str += (
                    f'                "lexema": "{error["descripcion"]["lexema"]}",\n'
                )
                errores_json_str += (
                    f'                "tipo": "{error["descripcion"]["tipo"]}",\n'
                )
                errores_json_str += (
                    f'                "columna": {error["descripcion"]["columna"]},\n'
                )
                errores_json_str += (
                    f'                "fila": {error["descripcion"]["fila"]}\n'
                )
                errores_json_str += "            }\n"
                errores_json_str += (
                    "        }"
                    if i == len(errores_dict["errores"]) - 1
                    else "        },\n"
                )
            errores_json_str += "\n    ]\n}\n"

            # Reemplaza las comillas simples por comillas dobles y ajusta el formato
            errores_json_str = errores_json_str.replace("'", '"').replace(
                "},", "},\n    "
            )

            # Crea un archivo llamado RESULTADOS.json y escribe los errores en él
            with open("RESULTADOS.json", "w") as resultados_file:
                resultados_file.write(errores_json_str)

            # Muestra el contenido de RESULTADOS.json en el área de texto
            self.text_area.insert(
                tk.END,
                "------------------------ RESULTADOS.JSON -----------------------\n",
            )
            with open("RESULTADOS.json", "r") as resultados_json_file:
                resultados_json = resultados_json_file.read()
            self.text_area.insert(tk.END, resultados_json)

        else:
            messagebox.showwarning(
                "Archivo no seleccionado",
                "Por favor, seleccione un archivo antes de continuar.",
            )

    def reporte(self):
        # Aquí iría el código para la opción "reportes"
        pass

    def salir(self):
        # Cierra la ventana principal
        self.ventana_principal.destroy()


if __name__ == "__main__":
    app = App()
    app.ventana_principal.mainloop()
