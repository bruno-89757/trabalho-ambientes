"""

Implementa um login simples para diferenciar tipos de utilizador:
- admin
- instrutor
- aluno

Usuários e senhas são armazenados em memória (dicionário).
"""

usuarios = {
    "admin": "1234",
    "instrutor": "abcd",
    "aluno": "pass"
}

def login():
    """
    Realiza o login do utilizador.

    Returns:
        str | None: Tipo de utilizador se login bem-sucedido, None caso contrário
    """
    username = input("Nome do Utilizador: ")
    senha = input("Palavra-passe: ")
    if username in usuarios and usuarios[username] == senha:
        print(f"Login bem-sucedido como {username}")
        return username
    else:
        print("Nome de utilizador ou senha inválidos.")
        return None
