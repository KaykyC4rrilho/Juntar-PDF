import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

def unir_pdfs_da_pasta(caminho_da_pasta, caminho_saida):
    try:
        # Lista todos os arquivos na pasta e filtra apenas os PDFs
        arquivos_pdfs = [os.path.join(caminho_da_pasta, f) for f in os.listdir(caminho_da_pasta) if f.endswith('.pdf')]
        arquivos_pdfs.sort()  # Ordena os arquivos em ordem alfabética

        if not arquivos_pdfs:
            messagebox.showinfo("Aviso", "Nenhum arquivo PDF encontrado na pasta selecionada.")
            return

        mesclador = PyPDF2.PdfMerger()

        # Adiciona cada PDF ao mesclador
        for pdf in arquivos_pdfs:
            mesclador.append(pdf)

        # Cria o PDF unido
        with open(caminho_saida, 'wb') as arquivo_final:
            mesclador.write(arquivo_final)

        messagebox.showinfo("Sucesso", f"PDFs unidos com sucesso! Arquivo salvo como:\n{caminho_saida}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def selecionar_pasta():
    caminho_da_pasta = filedialog.askdirectory(title="Selecione a pasta com os PDFs")
    if caminho_da_pasta:
        # Nome do arquivo de saída será o nome da pasta
        nome_pasta = os.path.basename(caminho_da_pasta)
        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar arquivo como",
            defaultextension=".pdf",
            filetypes=[("Arquivos PDF", "*.pdf")],
            initialfile=f"{nome_pasta}.pdf"
        )
        if caminho_saida:
            unir_pdfs_da_pasta(caminho_da_pasta, caminho_saida)

# Configurar interface Tkinter
def criar_interface():
    janela = tk.Tk()
    janela.title("Unir PDFs")
    janela.geometry("400x200")
    janela.resizable(False, False)

    label_instrucoes = tk.Label(
        janela,
        text="Clique no botão abaixo para selecionar a pasta com os PDFs.",
        wraplength=350,
        justify="center"
    )
    label_instrucoes.pack(pady=20)

    botao_selecionar = tk.Button(
        janela,
        text="Selecionar Pasta",
        command=selecionar_pasta,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold")
    )
    botao_selecionar.pack(pady=20)

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()
