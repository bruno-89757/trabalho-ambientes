"""


Implementa as operações CRUD para os instrutores:
- criar_instrutor
- listar_instrutores
"""

from models import Instrutor

instrutores = []  # Lista global de instrutores

def criar_instrutor(nome, categorias):
    """
    Adiciona um novo instrutor à lista de instrutores.

    Args:
        nome (str): Nome do instrutor
        categorias (list): Lista de categorias que o instrutor pode ensinar

    Returns:
        None
    """
    instrutor = Instrutor(nome, categorias)
    instrutores.append(instrutor)
    print(f"Instrutor {nome} adicionado com sucesso!")

def listar_instrutores():
    """
    Lista todos os instrutores cadastrados.

    Returns:
        None
    """
    if not instrutores:
        print("Nenhum instrutor cadastrado.")
    for i, instrutor in enumerate(instrutores):
        print(f"{i+1}. {instrutor}")
