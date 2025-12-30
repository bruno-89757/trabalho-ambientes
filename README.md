# TP2 – Aplicação Escola de Condução
**Unidade Curricular:** Ambientes de Desenvolvimento Colaborativo  
**Instituto:** Instituto Superior de Engenharia – Universidade do Algarve  

## 1. Descrição do Projeto
Este projeto consiste no desenvolvimento de uma aplicação em **Python**, executada em **consola**, para a gestão de uma **Escola de Condução**.  
A aplicação permite gerir **alunos, instrutores, veículos e aulas**, implementando operações **CRUD (Create, Read, Update, Delete)**, conforme o enunciado do TP2.

O desenvolvimento foi realizado de forma colaborativa, utilizando **Git** para controlo de versões e seguindo boas práticas de commits, branches e documentação.

---

## 2. Funcionalidades Implementadas

### Alunos
- Registar novos alunos  
- Listar alunos  
- Editar dados de um aluno  
- Remover alunos  

### Instrutores
- Registar instrutores  
- Listar instrutores  
- Editar dados  
- Remover instrutores  

### Veículos
- Adicionar veículos à frota  
- Listar veículos  
- Editar veículos  
- Remover veículos  

### Aulas
- Marcar aulas (aluno + instrutor + veículo)  
- Listar aulas  
- Atualizar estado da aula (marcada, cancelada, concluída)  
- Cancelar aulas  

### Autenticação
- Login por tipo de utilizador:
  - Administrador
  - Instrutor
  - Aluno

---

## 3. Estrutura do Projeto
```text
TP2-Escola-Conducao/
│
├── main.py # Menu principal e integração dos módulos
├── models.py # Classes principais (Aluno, Instrutor, Veículo, Aula)
├── crud_aluno.py # Operações CRUD de alunos
├── crud_instrutor.py # Operações CRUD de instrutores
├── crud_veiculo.py # Operações CRUD de veículos
├── crud_aula.py # Operações CRUD de aulas
├── auth.py # Login e autenticação
├── README.md # Documentação do projeto
└── .git/ # Repositório Git

```
