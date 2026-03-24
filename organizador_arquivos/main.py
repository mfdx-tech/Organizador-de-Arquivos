import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Lógica para organizar os arquivos na pasta selecionada
def organizar(pasta):
    contador = 0
    arquivos = os.listdir(pasta)

    for arquivo in arquivos:
        caminho_completo = os.path.join(pasta, arquivo)

        if os.path.isfile(caminho_completo):
            if arquivo.startswith("arquivo_"):
                continue

            caminho_completo = os.path.join(pasta, arquivo)

            if os.path.isfile(caminho_completo):
                nome, extensao = os.path.splitext(arquivo)
            if extensao:
                pasta_destino = os.path.join(pasta,f"arquivos_{extensao[1:].lower()}")

                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)
                    print(f"Pasta criada: arquivos_{extensao[1:].lower()}")

                shutil.move(caminho_completo, os.path.join(pasta_destino, arquivo))
                print(f"Arquivo movido: {arquivo} -> {pasta_destino}")
                contador += 1
    return contador
  

# Criar a interface gráfica

def escolher_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        contador = organizar(pasta)
        resultado.config(text=f"Total de arquivos organizados: {contador}")

root = tk.Tk()
root.title("Organizador de Arquivos")
root.geometry("400x150")

botao = tk.Button(
    root, 
    text="Escolher Pasta e Organizar",
    command=escolher_pasta,
    cursor="hand2",
)
botao.pack(pady=30)
resultado = tk.Label(root, text="")
resultado.pack(pady=10)
root.mainloop()