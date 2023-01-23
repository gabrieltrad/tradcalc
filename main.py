import customtkinter
import tkinter
import pyperclip
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


class App(customtkinter.CTk):
    """TODO: mover os presets pra cada aba, pra ficar individual"""
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.geometry("380x500")
        self.resizable(False, False)
        self.tab = customtkinter.CTkTabview(self)
        self.tab.grid(row=1, column=1, padx=40, pady=20, sticky="nw")
        self.tab.add("Lauda")
        self.tab.add("Palavras")
        self.tab.tab("Lauda").grid_columnconfigure(0, weight=1)
        self.tab.tab("Palavras").grid_columnconfigure(0, weight=1)

        def calc():
            """calculo de laudas usando regra de três."""
            try:
                # limpando os campos em vermelho (não vou por um if, ocupa linhas a toa)
                self.char.configure(border_color="grey")
                self.tam.configure(border_color="grey")
                self.preco.configure(border_color="grey")
                div = float(self.char.get()) / float(self.tam.get())
                # print(f'O documento possui {round(div, 2)} laudas')
                total = float(self.preco.get().replace(",", ".")) * div
                # print(f'Preço total: R${round(total, 2)}')
                self.result.configure(text=f'Valor total: {self.currency.get()} '
                                           f'{round(total, 2)} ({round(div, 2)} laudas)')
                if self.copy.get() is 1:
                    pyperclip.copy(round(total, 2))

            except ValueError:
                # verificando se todos os campos estão preenchidos
                if self.char.get() is None:
                    self.char.configure(border_color="red")
                if self.tam.get() is None:
                    self.tam.configure(border_color="red")
                if self.preco.get() is None:
                    self.preco.configure(border_color="red")
                if not self.char.get().isnumeric():
                    self.char.configure(border_color="red")
                if not self.tam.get().isnumeric():
                    self.tam.configure(border_color="red")
                if not self.preco.get().isnumeric():
                    self.preco.configure(border_color="red")
                self.result.configure(text="Valores inválidos!")

        def calcword():
            total = float(self.words.get()) * float(self.prpa.get().replace(",", "."))
            self.result2 = customtkinter.CTkEntry(self.tab.tab("Palavras"), state="readonly",
                                                  textvariable=customtkinter.StringVar(value=f"{self.currency.get()} {round(total, 3)}"))
            self.result2.grid()
        # teste do preset, remover quando tiver db
        correct = tkinter.DoubleVar(value=1500)

        def presets(x):
            if x == "PRESET1":
                self.tam.configure(textvariable=correct, state="readonly", text_color="grey")
        # -------------------- Calculo por laudas ------------------------
        # -------------- caracteres    ------------------
        self.charlabel = customtkinter.CTkLabel(self.tab.tab("Lauda"), text="Quantidade de caracteres")
        self.charlabel.grid()
        self.char = customtkinter.CTkEntry(self.tab.tab("Lauda"), placeholder_text="Valor")
        self.char.grid()
        # ----------------- laudas     -----------------
        self.tamlabel = customtkinter.CTkLabel(self.tab.tab("Lauda"), text="Tamanho da lauda")
        self.tamlabel.grid()
        self.tam = customtkinter.CTkEntry(self.tab.tab("Lauda"), placeholder_text="Valor")
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
        self.copy = customtkinter.CTkCheckBox(self.options, text="Copiar total")
        self.copy.grid(row=2, column=0, padx=5, pady=5)
        # ------------------------- Calculo por palavras ----------------------
        self.wordslabel = customtkinter.CTkLabel(self.tab.tab("Palavras"), text="Quantidade de palavras")
        self.wordslabel.grid()
        self.words = customtkinter.CTkEntry(self.tab.tab("Palavras"), placeholder_text="Valor")
        self.words.grid()
        self.prpalabel = customtkinter.CTkLabel(self.tab.tab("Palavras"), text="Preço por palavra")
        self.prpalabel.grid()
        self.prpa = customtkinter.CTkEntry(self.tab.tab("Palavras"), placeholder_text="Valor")
        self.prpa.grid()
        self.prpabutton = customtkinter.CTkButton(self.tab.tab("Palavras"), text="Calcular!", command=calcword)
        self.prpabutton.grid(pady=5)
        """self.result2 = customtkinter.CTkEntry(self.tab.tab("Palavras"), state="readonly", placeholder_text="Total")
        self.result2.grid()"""


if __name__ == "__main__":
    app = App()
    app.mainloop()
