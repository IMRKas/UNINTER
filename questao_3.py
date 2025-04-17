"""
# QUESTÃO 3 de 4 - Conteúdo até aula 05
# Enunciado: Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.
# A copiadora opera da seguinte maneira:
# Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;
# Serviço de Impressão Colorida (ICO) o custo por página é de um real; 
# Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos; 
# Serviço de Fotocópia (FOT) o custo por página é de vinte centavos; 

# Se número de páginas for menor que 20 retornar o número de página sem desconto;
# Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número de páginas com o desconto é de 15%;
# Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o número de páginas com o desconto é de 20%;
# Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o número de páginas com o desconto é de 25%;
# Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa quantidade de páginas;

# Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais;
# Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40 reais;
# Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;
# total = (servico * num_pagina) + extra
"""

# Dicionario identificando o tipo de serviço oferecido pelo ciente
# juntamente com o seu preço.
tipo_serv = {"DIG": 1.2, "ICO": 1, "IPB": 0.4, "FOT": 0.20}
serv_extra = {'1': 15, '2': 40, '0': 0}

# Função criada para que o funcionario do cliente possa escolher o tipo de serviço
# requisitado. Ao final retornará o preço cobrado pelo serviço requisitado
def escolha_servico():
	while True:
		servico = input("Entre com o serviço desejado\nDIG - Digitalização\nICO - Impressão Colorida\nIPB - Impressão Preto e Branco\nFOT - Fotocópia\n").upper()
		if servico not in tipo_serv.keys():
			print("Escolha inválida, entre com o tipo do serviço novamente\n")
		else:
			return tipo_serv[servico] 

# Função criada para que o funcionario do cliente possa entrar com o numero de páginas
# requisitadas. A função fará um calculo de desconto, definido pelo cliente, com base
# na quantidade de paginas inseridas e retornará o numero de paginas já com o desconto se houver algum
def num_pagina():
	while True:
		try: # Checar se o numero de paginas digitados é valido
			paginas = int(input("Entre com o numero de páginas: "))
		except:
			print("Valor de páginas inválido\nPor favor, entre com o número de paǵinas novamente")
		else:
			if paginas <= 0:
				print("Valor de páginas inválido\nPor favor, entre com o número de paǵinas novamente\n")
			elif paginas >= 20000: # Definido pelo cliente que não aceitará mais de 20000 paginas
				print("Não aceitamos tantas páginas de uma vez.\nPor favor, entre com o número de paǵinas novamente\n")
			else:
				if paginas < 20:
					return paginas 
				elif 20 <= paginas < 200:
					return int(paginas - (paginas * 0.15)) 
				elif 200 <= paginas < 2000:
					return int(paginas - (paginas * 0.20))
				else:
					return int(paginas - (paginas * 0.25))

# Função criada para o funcionario do cliente selecionar se há algum adicional
# no pedido feito e retornará o valor do serviço adicional selecionado
def servico_extra():
	while True:
		extra = input("\nDeseja adicionar algum serviço ?\n1 - Encadernação Simples - R$ 15.00\n2 - Encadernação Capa Dura - R$ 40.00\n0 - Não desejo mais nada\n") 
		# Checar se a opção escolhida é valida
		if not extra.isnumeric() or extra not in serv_extra.keys():
			print("Escolha inválida.\nSelecione uma opção válida.\n")
		else:
			return serv_extra[extra]

# Função principal
def main():
	print("Bem vindo a Copiadora do Igor da Mota Rabelo")
	servico = escolha_servico()
	paginas = num_pagina()
	extra = servico_extra()

	# Ao final, retonar o valor total do pedido e mostra-lo na tela com todas as informações utilizadas para fazer o calculo
	print(f"Total: R${paginas*servico+extra:.2f} (servicço: {servico:.2f} * páginas: {paginas} + extra: {extra:.2f})")	




if __name__ == '__main__':
	main()

