# Unir PDFs com Python e Tkinter

Este projeto é uma ferramenta simples e eficiente para unir arquivos PDF localizados em uma pasta. Utilizando Python e a biblioteca Tkinter, a aplicação oferece uma interface gráfica amigável para selecionar a pasta de arquivos e gerar um PDF único com todos os documentos combinados.

## Funcionalidades

- **Seleção de Pasta**: Permite selecionar uma pasta contendo arquivos PDF.
- **Combinação Automática**: Une todos os PDFs da pasta em um único arquivo.
- **Ordenação Alfabética**: Os PDFs são unidos em ordem alfabética com base no nome dos arquivos.
- **Interface Intuitiva**: Interface gráfica clara e fácil de usar.
- **Escolha do Local de Salvar**: O usuário pode especificar o nome e o local do arquivo resultante.

---

## Tecnologias Utilizadas

- **Python 3.x**
- **Bibliotecas**:
  - `PyPDF2`: Manipulação de arquivos PDF.
  - `Tkinter`: Criação da interface gráfica.
  - `os`: Manipulação de diretórios e arquivos.

---

## Como Usar

### Pré-requisitos

- Ter o Python 3.x instalado no sistema.
- Instalar a biblioteca `PyPDF2`. Utilize o comando:
  ```bash
  git clone <URL-do-repositório>
  cd <nome-do-diretório>

  pip install pypdf2
  python <nome-do-script>.py

