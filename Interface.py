import os
import tkinter as tk
from tkinter import Frame, filedialog ,messagebox, ttk
import customtkinter as ctk
from customtkinter import CTkButton, CTkFrame, CTk, CTkLabel, CTkImage, CTkEntry, CTkRadioButton, CTkProgressBar
import pandas as pd
import shutil


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("650x400")
        self.title ("Organizador de documentos Excel")
        self.container = CTkFrame(self, fg_color="#F5F4F4")
        self.container.pack(fill="both", expand=True)
        # self.container.rowconfigure(0, weight=1)
        # self.container.columnconfigure(0, weight=1)
        self.resizable(False, False)
        self.titulo = CTkLabel(self.container, text= "Organize suas Planilhas", font= ('Arial', 18, 'bold'), text_color="#171127" )
        self.titulo.pack(pady=(50,30))

        self.frame_origem = CTkFrame(self.container, fg_color="transparent", corner_radius=8)
        self.frame_origem.pack(fill="x", padx=10, pady=5)
        self.titulo_origem = CTkLabel(self.frame_origem, text= "Selecione a pasta de origem das planilhas", font= ('Arial', 12, 'bold'), text_color="#121213")
        self.titulo_origem.pack(anchor="w",padx=(5,0))
        self.botao_origem = CTkButton(self.frame_origem, text="Origem das planilhas", fg_color="#0fabb1", font=('Arial', 14, 'bold'),width= 40, height= 25, command=self.buscar_origem)
        self.botao_origem.pack(side='left', padx=(15, 5), pady=(10,30))
        self.caminho_origem = CTkEntry(self.frame_origem, font=('Arial', 14, 'bold'), text_color="black", fg_color="#FFFFFF", width= 450, justify="center", state="disabled")
        self.caminho_origem.pack(side='left',pady=(10,20))

        self.frame_destino = CTkFrame(self.container, fg_color="transparent", corner_radius=8)
        self.frame_destino.pack(fill="x", padx=10, pady=5)
        self.titulo_destino = CTkLabel(self.frame_destino, text="Selecione a pasta de destino das planilhas", font=('Arial', 12, 'bold'), text_color="#121213")
        self.titulo_destino.pack(anchor= 'w', padx=(5,0))
        self.botao_destino = CTkButton(self.frame_destino, text="Destino das planilhas", fg_color="#0fabb1", font=('Arial', 14, 'bold'),width= 40, height= 25, command=self.buscar_destino)
        self.botao_destino.pack(side='left', padx=(15, 5), pady=(5,10))
        self.caminho_destino = CTkEntry(self.frame_destino, font=('Arial', 14, 'bold'), text_color="black", fg_color="#FFFFFF", width= 450, justify="center", state="disabled")
        self.caminho_destino.pack(side='left')

        self.botao_processar = CTkButton(self.container, text="Processar Planilhas", fg_color="#27b8bd",  hover_color="#282188", font=('Arial', 15, 'bold'), width=250, height=40,
        command=self.executar_leitura)
        self.botao_processar.pack(pady=(30, 10))

        
    def buscar_origem(self):
        caminho = filedialog.askdirectory(title="Selecione a pasta de origem das planilhas", initialdir=os.path.join(os.path.expanduser("~")))
        if caminho:
            self.caminho_origem.configure(state="normal")
            self.caminho_origem.delete(0, "end")
            self.caminho_origem.insert(0, caminho) 
            self.caminho_origem.configure(state="disabled")


    def buscar_destino(self):
        caminho = filedialog.askdirectory(title="Selecione a pasta o destino das planilhas", initialdir=os.path.join(os.path.expanduser("~")))
        if caminho:
            self.caminho_destino.configure(state="normal")
            self.caminho_destino.delete(0, "end")
            self.caminho_destino.insert(0, caminho) 
            self.caminho_destino.configure(state="disabled")


    def executar_leitura(self):
        self.caminho_origem.configure(state="normal")
        origem = self.caminho_origem.get()
        self.caminho_origem.configure(state="disabled")

        self.caminho_destino.configure(state="normal")
        destino = self.caminho_destino.get()
        self.caminho_destino.configure(state="disabled")

        if not os.path.isdir(origem) or not os.path.isdir(destino):
            messagebox.showerror("ERRO!","Origem ou destino dos arquivos não foi selecionado.")
            return

        arquivos = os.listdir(origem)
        planilhas = [f for f in arquivos if f.lower().endswith(('.xlsx', '.xls', 'xlsm'))]

        if not planilhas:
                messagebox.showwarning("Aviso", "Nenhum arquivo do Excel (.xlsx ou .xls) foi encontrado na pasta de origem!")
                return

        try:
            contador = 0
            for arquivo in planilhas:
                caminho_origem_arquivo = os.path.join(origem, arquivo)
                caminho_destino_arquivo = os.path.join(destino, f"organizado_{arquivo}")
                shutil.copy(caminho_origem_arquivo, caminho_destino_arquivo)
                contador += 1

            messagebox.showinfo("Sucesso!",
            f"Processo concluído!\n\n{contador} planilha(s) organizada(s) com sucesso.")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao processar os arquivos:\n{e}")


if __name__ == "__main__":
    app = App()
    app.mainloop()