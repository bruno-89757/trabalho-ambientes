"""


Define as classes principais do sistema da escola de condução:
- Aluno
- Instrutor
- Veículo
- Aula

Cada classe contém atributos relevantes e método __str__ para representação legível.
"""

class Aluno:
    """
    Representa um aluno da escola de condução.

    Atributos:
        nome (str): Nome completo do aluno
        idade (int): Idade do aluno
        categoria_carta (str): Categoria da carta de condução

    Métodos:
        __str__(): Retorna uma representação textual do aluno
    """
    def __init__(self, nome, idade, categoria_carta):
        self.nome = nome
        self.idade = idade
        self.categoria_carta = categoria_carta

    def __str__(self):
        return f"{self.nome}, {self.idade} anos, Carta: {self.categoria_carta}"

class Instrutor:
    """
    Representa um instrutor da escola de condução.

    Atributos:
        nome (str): Nome do instrutor
        categorias (list): Lista de categorias que o instrutor pode ensinar

    Métodos:
        __str__(): Retorna uma representação textual do instrutor
    """
    def __init__(self, nome, categorias):
        self.nome = nome
        self.categorias = categorias

    def __str__(self):
        return f"{self.nome}, Categorias: {', '.join(self.categorias)}"

class Veiculo:
    """
    Representa um veículo da frota da escola.

    Atributos:
        modelo (str): Modelo do veículo
        matricula (str): Matrícula do veículo

    Métodos:
        __str__(): Retorna uma representação textual do veículo
    """
    def __init__(self, modelo, matricula):
        self.modelo = modelo
        self.matricula = matricula

    def __str__(self):
        return f"{self.modelo} - {self.matricula}"

class Aula:
    """
    Representa uma aula agendada na escola de condução.

    Atributos:
        aluno (Aluno): Aluno associado à aula
        instrutor (Instrutor): Instrutor associado à aula
        veiculo (Veiculo): Veículo utilizado
        estado (str): Estado da aula (agendada, concluída, cancelada)

    Métodos:
        __str__(): Retorna uma representação textual da aula
    """
    def __init__(self, aluno, instrutor, veiculo, estado="agendada"):
        self.aluno = aluno
        self.instrutor = instrutor
        self.veiculo = veiculo
        self.estado = estado

    def __str__(self):
        return f"Aula: {self.aluno.nome} com {self.instrutor.nome}, Veículo: {self.veiculo.modelo}, Estado: {self.estado}"
