"""


Implementa as operações CRUD para veículos:
- adicionar_veiculo
- listar_veiculos
"""

from models import Veiculo

veiculos = []  # Lista global de veículos

def adicionar_veiculo(modelo, matricula):
    """
    Adiciona um novo veículo à frota.

    Args:
        modelo (str): Modelo do veículo
        matricula (str): Matrícula do veículo

    Returns:
        None
    """
    veiculo = Veiculo(modelo, matricula)
    veiculos.append(veiculo)
    print(f"Veículo {modelo} adicionado com sucesso!")

def listar_veiculos():
    """
    Lista todos os veículos cadastrados.

    Returns:
        None
    """
    if not veiculos:
        print("Nenhum veículo cadastrado.")
    for i, v in enumerate(veiculos):
        print(f"{i+1}. {v}")
