# Questão 4

#Variaveis globais
lista_livro = []
id_global = 0

# Função deve fazer o cadastro de livros para o cliente.
# O cadastro deve levar em conta o autor, o nome do livro, a editora digitado pelo cliente e o ID que é gerado automaticamente
# A função checará se o autor já está cadastrado no sistema. Se sim, apenas acrescentará o novo livro ao
# repositorio do referido autor. Se não, deverá criar um novo item no sistema e cadastrar todos os dados passados
def cadastrar_livro(id):
	print('-'*44)
	print('-'*11,"MENU CADASTRAR LIVRO",'-'*11)
	print(f"ID do livro: {id}")
	nome = input("Por favor, entre com o nome do livro: ")
	autor = input("Por favor, entre com o autor do livro: ")
	editora = input("Por favor, entre com a editora do livro: ")
	# Check para saber se a lista de livro está vazia. Se estiver já faz o primeiro cadastro
	if len(lista_livro) == 0:
		lista_livro.append({"autor":autor,"livro":[{"nome":nome, "editora": editora, "id":id}]})
		print('-'*44)
		print()
	else:
		# Verificará os items dentro da lista para encontrar autores já cadastrados
		for item in lista_livro:
			if autor in item.values():
				# Se o autor já está cadastrado, a lista de livros pertencente a este autor será atualizado
				item["livro"].append({"nome":nome, "editora": editora ,"id":id})
				print('-'*44)
				print()
				break
			
			# Se o autor não foi encontrado após verificar toda a lista, então será cadastrado um novo autor
			elif lista_livro[len(lista_livro)-1] == item:
				lista_livro.append({"autor":autor,"livro":[{"nome":nome, "editora": editora, "id":id}]})
				print('-'*44)
				print()
				break

# Função para fazer uma busca no sistema pelos livros cadastrados:
# Fará um loop em cada item do sistema buscando o item ou os items requisitados pelo cliente
# A função retornará ao menu principal caso seja passado a opção de retornar
def consultar_livro():
	while True:
		print()
		print('-'*44)
		print('-'*11,"MENU CONSULTAR LIVRO",'-'*11)
		print("Escolha a opção desejada:")
		print("1 - Consultar Todos os Livros\n2 - Consultar Livro por id\n3 - Consultar Livro(s) por autor\n4 - Retornar")
		option = input()

		match option:
			case '4': 
				# Retornar ao menu principal
				return 0
			case '1': # Consultar Todos os Livros
				# Verificação de a lista de livro está vazia
				if len(lista_livro) == 0:
					print("Não há livros cadastrados.")
				else:
					# Caso não esteja, faz a consulta dentro da lista item por item do dicionario
					for items in lista_livro:
						for livro in items["livro"]:
							print(f"\nid: {livro['id']}\nnome: {livro['nome']}\nautor: {items['autor']}\neditora: {livro['editora']}")

			case '2': # Consultar Livro por id
				while True:
					con_id = input("Digite o id do livro: ")
					# Checar se o número de ID digitado é valido
					if not con_id.isnumeric() or int(con_id) <= 0 or int(con_id) > id_global:
						print(f"ID inválido. Digite um ID válido por favor (1 - {id_global})")
					else:
						control = False # Criado para sair do loop duplo for quando o item for encontrado pois não é necessário retornar mais de um item
						for items in lista_livro:
							for livro in items["livro"]:
								if livro["id"] == int(con_id):
									print(f"\nid: {livro['id']}\nnome: {livro['nome']}\nautor: {items['autor']}\neditora: {livro['editora']}")
									control = True # Encerrar o loop após encontrar o ID inserido
									break
							if control: # Quebra o loop somente após encontrar o item requisitado
								break
						break

			case '3': # Consultar Livro(s) por autor
				con_autor = input("Digite o autor do(s) livro(s): ")
				control = False # Criado controle para não haver repetição de loop desnecessário pois cada autor deverá ser cadastrado apenas uma vez no sistema
				for items in lista_livro:
					if items["autor"] == con_autor:
						control = True # Se o autor foi encontrado não há necessidade de continuar o loop
						for livro in items["livro"]:
							print(f"\nid: {livro['id']}\nnome: {livro['nome']}\nautor: {items['autor']}\neditora: {livro['editora']}")
					if control: # Quebra o loop após mostrar na tela as informações requisitadas
						break

			case _: # Caso nenhuma opção valida por selecionada, informar o cliente e motrar o menu novamente
				print("Opção invalida\n")



# Função criada para remover um livro do sistema
# Cada livro tem um ID próprio e este é usado por esta função para encontra-lo e remove-lo
def remover_livro():
	print()
	print('-'*44)
	print('-'*12,"MENU REMOVER LIVRO",'-'*12)
	con_id = input("Digite o id do livro a ser removido: ")
	while True:
		# Checar se o numero de ID digitado é valido
		if not con_id.isnumeric() or int(con_id) <= 0 or int(con_id) > id_global:
			print(f"ID inválido. Digite um ID válido por favor (1 - {id_global})")
		else:
			control = False # Controle criado para evitar loop desnecessário pois cada ID só pode estar atribuido a um unico livro
			for items in lista_livro:
				for livro in items["livro"]:
					if livro["id"] == int(con_id):
						print("Livro removido com sucesso!\n")
						
						# Para remover o livro é necessário passar todas as informações do livro com o ID pedido
						items["livro"].remove({"nome":livro["nome"],"editora":livro["editora"], "id":livro["id"]})
						control = True
						break
				if control: # Se o ID foi encontrado, o livro foi removido portanto o loop deve ser encerrado
					break
		break





# Programa principal
def main():
	print("Bem vindo a livraria do Igor da Mota Rabelo")
	
	global id_global # Variavel necessita ser global para ser acessada pelas funções do sistema

	while True:
		print('-'*44)
		print('-'*14,"MENU PRINCIPAL",'-'*14)
		print("Escolha a opção desejada:")
		print("1 - Cadastrar Livro\n2 - Consultar Livro(s)\n3 - Remover Livro\n4 - Sair")
		option = input()
		
		# Com base na opção escolhida pelo usuário:
		match option:
			case '4': # Encerrar Programa
				break

			case '1': # Cadastrar Livro
				id_global += 1 # Cada livro deve ter um ID único
				cadastrar_livro(id_global)

			case '2': # Consultar livro
				consultar_livro()

			case '3': # Remover livro
				remover_livro()
			
			case _: # Se não foi escolhida opção válida, informar o cliente e mostrar novamente o menu
				print("Opção inválida. Digite uma opção válida por favor (1 - 4)")






if __name__ == "__main__":
	main()
