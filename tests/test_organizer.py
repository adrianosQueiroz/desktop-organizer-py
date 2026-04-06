import unittest
import os
import shutil
import tempfile
from src.main import organizar_area_de_trabalho

class TestOrganizador(unittest.TestCase):

    def setUp(self):
        # Cria um diretório temporário para simular a Área de Trabalho
        self.test_dir = tempfile.mkdtemp()
        
        # Cria alguns arquivos de teste
        self.arquivos_teste = [
            'relatorio.pdf',
            'query_vendas.sql',
            'dashboard_final.pbix',
            'script_analise.py',
            'foto_perfil.png'
        ]
        
        for nome in self.arquivos_teste:
            with open(os.path.join(self.test_dir, nome), 'w') as f:
                f.write('conteudo de teste')

    def tearDown(self):
        # Remove o diretório temporário após o teste
        shutil.rmtree(self.test_dir)

    def test_organizacao_pastas(self):
        """Verifica se as pastas corretas foram criadas e arquivos movidos"""
        organizar_area_de_trabalho(self.test_dir)
        
        # Verifica se as pastas esperadas existem
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Documentos')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'SQL')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Power BI')))
        
        # Verifica se o arquivo SQL foi movido corretamente
        caminho_sql = os.path.join(self.test_dir, 'SQL', 'query_vendas.sql')
        self.assertTrue(os.path.isfile(caminho_sql))

if __name__ == '__main__':
    unittest.main()