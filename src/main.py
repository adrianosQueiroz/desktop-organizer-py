import os
import shutil
import logging

# Configuração de Logging para parecer um software profissional
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Dicionário de Categorias (Fácil de dar manutenção)
MAPA_EXTENSOES = {
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.rtf', '.csv'],
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Vídeos': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
    'Áudios': ['.mp3', '.wav', '.aac', '.flac'],
    'Compactados': ['.zip', '.rar', '.7z'],
    'Executáveis': ['.exe', '.msi'],
    'Código': ['.py', '.js', '.html', '.css', '.c', '.cpp', '.java', '.ipynb', '.json', '.rdl'],
    'SQL': ['.sql'],
    'Power BI': ['.pbix']
}

def obter_pasta_destino(extensao):
    """Retorna o nome da pasta com base na extensão do arquivo."""
    for pasta, extensoes in MAPA_EXTENSOES.items():
        if extensao.lower() in extensoes:
            return pasta
    return 'Outros'

def organizar_area_de_trabalho(caminho_desktop):
    """Executa a lógica de organização dos arquivos."""
    if not os.path.exists(caminho_desktop):
        logging.error(f"Caminho não encontrado: {caminho_desktop}")
        return

    itens = os.listdir(caminho_desktop)
    
    for item in itens:
        caminho_origem = os.path.join(caminho_desktop, item)
        
        # Pula diretórios e o próprio script para evitar loops
        if os.path.isdir(caminho_origem) or item in ['main.py', 'organizador.py']:
            continue

        _, extensao = os.path.splitext(item)
        pasta_nome = obter_pasta_destino(extensao)
        caminho_destino_pasta = os.path.join(caminho_desktop, pasta_nome)

        # Cria a pasta se não existir
        if not os.path.exists(caminho_destino_pasta):
            os.makedirs(caminho_destino_pasta)
            logging.info(f"Nova categoria criada: {pasta_nome}")

        # Move o arquivo com tratamento de erro
        try:
            shutil.move(caminho_origem, os.path.join(caminho_destino_pasta, item))
            logging.info(f"Movido: {item} -> {pasta_nome}")
        except Exception as e:
            logging.error(f"Erro ao mover {item}: {e}")

if __name__ == "__main__":
    # Detecta o Desktop automaticamente (Windows/Linux/Mac)
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    
    print("--- Iniciando Automação de Limpeza ---")
    organizar_area_de_trabalho(desktop)
    print("--- Organização Concluída com Sucesso ---")