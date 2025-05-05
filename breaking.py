import pyzipper

# Nome do arquivo ZIP
nome_arquivo_zip = 'arquivo.zip'

# Tenta abrir o ZIP com suporte a AES
try:
    with pyzipper.AESZipFile(nome_arquivo_zip) as arquivo_zip:
        for i in range(10000):  # de 0000 até 9999
            senha = f"{i:04}"  # Garante que são 4 dígitos, ex: '0073'
            try:
                arquivo_zip.pwd = senha.encode('utf-8')
                arquivo_zip.extractall()
                print(f"✅ Senha encontrada: {senha}")
                break
            except RuntimeError:
                continue
except FileNotFoundError:
    print("Arquivo não encontrado.")
except Exception as e:
    print(f"Erro: {e}")