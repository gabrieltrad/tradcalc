import customtkinter
import tkinter
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.geometry("400x400")
        self.tab = customtkinter.CTkTabview(self)
        self.tab.grid(row=1, column=1, padx=40, pady=20, sticky="nw")
        self.tab.add("Lauda")
        self.tab.add("Palavras")
        self.tab.tab("Lauda").grid_columnconfigure(0, weight=1)
        self.tab.tab("Palavras").grid_columnconfigure(0, weight=1)
        correct = tkinter.DoubleVar(value=1500)

        def calc():
            try:
                print(self.char.get())
                print(self.tam.get())
                print(self.preco.get())
                div = float(self.char.get()) / float(self.tam.get())
                print(f'O documento possui {round(div, 2)} laudas')
                total = float(self.preco.get().replace(",", ".")) * div
                print(f'Preço total: R${round(total, 2)}')
                self.result.configure(text=f'Valor total: {self.currency.get()} {round(total, 2)}')

            except ValueError:
                print("Valor inválido!!!")

        def presets(x):
            if x == "PRESET1":
                print('ta')
                self.tam.configure(textvariable=correct, state="disabled", text_color="grey")
        # ---------- Calculo por laudas ----------
        # --- caracteres
        self.charlabel = customtkinter.CTkLabel(self.tab.tab("Lauda"), text="Quantidade de caracteres")
        self.charlabel.grid()
        self.char = customtkinter.CTkEntry(self.tab.tab("Lauda"))
        self.char.grid()
        # ---
        self.tamlabel = customtkinter.CTkLabel(self.tab.tab("Lauda"), text="Tamanho da lauda")
        self.tamlabel.grid()
        self.tam = customtkinter.CTkEntry(self.tab.tab("Lauda"))
        self.tam.grid()
        self.precolabel = customtkinter.CTkLabel(self.tab.tab("Lauda"), text="Preço por lauda")
        self.precolabel.grid()
        self.preco = customtkinter.CTkEntry(self.tab.tab("Lauda"), placeholder_text="Valor")
        self.preco.grid()
        self.calcbutton = customtkinter.CTkButton(master=self.tab.tab("Lauda"), text="Calcular!", command=calc)
        self.calcbutton.grid(pady=5)
        self.result = customtkinter.CTkLabel(self.tab.tab("Lauda"), text="")
        self.result.grid()

        self.options = customtkinter.CTkFrame(self, width=240)
        self.options.grid(row=2, column=1, padx=40, pady=20, sticky="nw")
        self.curlabel = customtkinter.CTkLabel(self.options, text="Moeda")
        self.curlabel.grid(column=0, row=0)
        self.currency = customtkinter.CTkOptionMenu(self.options, dynamic_resizing=False,
                                                    values=["BRL", "USD", "EUR"], )
        self.currency.grid(padx=5, pady=5)
        self.presetlab = customtkinter.CTkLabel(self.options, text="Presets")
        self.presetlab.grid(column=2, row=0)
        self.preset = customtkinter.CTkOptionMenu(self.options, dynamic_resizing=True,
                                                  values=["PRESET1", "PRESET 2"], command=presets)
        self.preset.grid(row=1, column=2, padx=5, pady=5)




if __name__ == "__main__":
    app = App()
    app.mainloop()
