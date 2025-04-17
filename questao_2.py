#****************************************************************************************
# QUESTÃO 2 de 4 - Conteúdo até aula 04
# Enunciado: Você e sua equipe de programadores foram contratados para 
# desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu. 
# Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
# A Loja possui seguinte relação:
# · Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
# · Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
# · Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;
#***************************************************************************************** 

# Cabeçalho do programa
print("Bem vindo a Loja de Gelados do Igor da Mota Rabelo")
print("-"*21+"Cardápio"+"-"*21)
print("-"*50)
print("---| ","Tamanho"," | ","Cupuaçu (CP)"," | ","Açaí (AC)"," |---" )
print("---| ","   P   "," | ","   R$  9.00 "," | ","R$ 11.00 "," |---" )
print("---| ","   M   "," | ","   R$ 14.00 "," | ","R$ 16.00 "," |---" )
print("---| ","   G   "," | ","   R$ 18.00 "," | ","R$ 20.00 "," |---" )
print("-"*50)

# Para evitar duplicidade de código, foi criado print_order
# Receberá os parametros e mostrará ao usuário o que ele pediu
def print_order(sabor, tamanho, valor):
	print(f"Você pediu um {sabor} no tamanho {tamanho}: R$ {valor:.2f}")	

# Criado Dicionarios necessários para opções de sabores
# existentes na loja. Facilita a adição de novos sabores
# e novos tamanhos se necessário mas seria necessário adaptar o restante do codigo melhor
options = {"CP":"Cupuaçu","AC":"Açaí"}
cupuacu = {"P": 9, "M": 14, "G": 18} 
acai = {"P": 11, "M": 16, "G":20}

total = 0 # Total a ser pago pelo usuário quando a ordem for encerrada.

while True:
	sabor = input("Entre com o sabor desejado (CP/AC): ").upper()
	
	# Se o sabor não existir entre as opções, o usurário saberá que precisará selecionar um sabor valido
	if options.get(sabor) == None:
		print("Sabor inválido. Tente novamente")
		print()

	else:		
		tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()
		
		# Se o tamanho não existir entre as opções do sabor selecionado, o usurário saberá que precisará selecionar um tamanho valido
		if acai.get(tamanho) == None and cupuacu.get(tamanho) == None:
			print("Tamanho inválido. Tente novamente.")
			print()
		else:

			# Bloco para fazer o calculo de valor baseado no sabor e tamanho escolhido pelo usuário
			if sabor == "CP":
				if tamanho == 'P':
					print_order(options["CP"],tamanho,cupuacu[tamanho])
					total += cupuacu[tamanho]
				elif tamanho == 'M':
					print_order(options["CP"],tamanho,cupuacu[tamanho])
					total += cupuacu[tamanho]
				else:
					print_order(options["CP"],tamanho,cupuacu[tamanho])
					total += cupuacu[tamanho]
			else:
				if tamanho == 'P':
					print_order(options["AC"],tamanho,acai[tamanho])
					total += acai[tamanho]
				elif tamanho == 'M':
					print_order(options["AC"],tamanho,acai[tamanho])
					total += acai[tamanho]
				else:
					print_order(options["AC"],tamanho,acai[tamanho])
					total += acai[tamanho]
			print()
			
			# Bloco criado para o usurário escolher sair ou fazer novo pedido
			while True:
				novo_pedido =  input("Deseja pedir mais alguma coisa? (S/N): ").upper()
				if novo_pedido == 'S' or novo_pedido == 'N':
					break
				else:
					print("Opção inválida.")
				
			if novo_pedido == 'S':
				continue
			else:
				print()
				print('-'*50)
				print(f"O valor total a ser pago: R$ {total:.2f}")
				print('-'*50)
				break

