# 📂 Desktop Organizer Python

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Script automatizado para organizar arquivos da Área de Trabalho (Desktop) em pastas categorizadas por extensão. Ideal para manter o fluxo de trabalho limpo e otimizar a busca por documentos e códigos.

## 🚀 Funcionalidades
- Categorização automática de arquivos (**BI**, **SQL**, **Código**, **Documentos**, etc).
- Criação dinâmica de pastas caso não existam.
- Tratamento de exceções para evitar erros durante a movimentação de arquivos.
- Suporte para extensões específicas de análise de dados como `.pbix`, `.sql`, `.rdl` e `.ipynb`.

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- Biblioteca `os` e `shutil` (Nativas do Python)

## 📋 Como usar
1.## 🚀 Como Utilizar

Siga os passos abaixo para configurar e executar o organizador em sua máquina.

### 1.1 Pré-requisitos
Certifique-se de ter o **Python 3.x** instalado. Você pode verificar digitando no terminal:

python --version


2. Clonando o Repositório
Abra o seu terminal (ou Git Bash) e execute: Clone este repositório:

   git clone [https://github.com/adrianosQueiroz/desktop-organizer-py.git](https://github.com/adrianosQueiroz/desktop-organizer-py.git)


3. Execução
Para organizar sua Área de Trabalho agora mesmo, rode o comando:

Bash
python src/main.py
4. Customização (Opcional)
Se você deseja adicionar novas extensões ou mudar o nome das pastas:

Abra o arquivo src/main.py.

Localize o dicionário MAPA_EXTENSOES.

Adicione a categoria desejada seguindo o padrão:

Python
'Minha Nova Pasta': ['.ext1', '.ext2']
🧪 Rodando os Testes
Para garantir que o ambiente está configurado corretamente e a lógica de movimentação está íntegra, execute:

Bash
python -m unittest tests/test_main.py

---