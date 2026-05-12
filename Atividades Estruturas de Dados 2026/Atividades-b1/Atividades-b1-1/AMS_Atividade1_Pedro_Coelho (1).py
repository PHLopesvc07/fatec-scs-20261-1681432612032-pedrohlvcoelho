'''
*---------------------------------------------------------------*
*       Fatec São Caetano do Sul                                *
*       Atividade B1-1                                          *
*       Autor: Pedro Henrique Lopes Vilela Coelho               *
*        Objetivo: Reimplementar as opera¸cões fundamentais     *
*       de um sistema de cadastro utilizando a estrutura de     * 
*       dados Dicionário em Python, aplicando conceitos de      *
*       abstração e persistência em memória.                    *
*                                                               *  
*       data: 24/02/2026                                        *
*---------------------------------------------------------------*
'''

catalogo = {}

def adicionar_filme(id_filme, titulo, diretor):
    if id_filme not in catalogo:
        catalogo[id_filme] = {"titulo": titulo, "diretor": diretor}
        print("Filme adicionado com sucesso!")
    else: 
        print("Erro: filme já existe no catalogo")
        return

def buscar_filme(id_filme):
    if id_filme in catalogo:
        return catalogo.get(id_filme)
    else:
        print("Erro: filme não encontrado")
        return None

def remover_filme(id_filme):
    if catalogo.pop(id_filme, None):
        print("Filme removido com sucesso.")
    else:
        print("Erro: filme não encontrado")

def listar_todos():
    if not catalogo:
        print("\nO catalogo está vazio.")
    else:
        print("\n--- Listagem de Filmes ---")
        for id_f, dados in catalogo.items():
            print(f"ID: {id_f} | Titulo: {dados['titulo']} | Diretor: {dados['diretor']}")

# --- Testes de Funcionamento ---

# Teste com ID duplicado
print(">>> TESTE 1: Adicionando filmes")
adicionar_filme(101, "Django", "Quentin Tarantino")
adicionar_filme(102, "Full Metal Jacket", "Stanley Kubrick")
adicionar_filme(101, "O Cavaleiro das Trevas", "Christopher Nolan") 


print("\n>>> TESTE 2: Buscando filmes")
busca1 = buscar_filme(101)
print(f"Resultado ID 101: {busca1}")
busca2 = buscar_filme(999)
print(f"Resultado ID 999: {busca2}") #Teste ID inexiste

#teste listagem
print("\n>>> TESTE 3: Listagem atual")
listar_todos()
