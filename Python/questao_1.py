# ********************************************************************************
#* Se total for menor que 2500 o desconto será de 0%;                            *
#* Se total for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;  *
#* Se total for igual ou maior que 6000 e menor que 10000 o desconto será de 7%; *
#* Se total for igual ou maior que 10000 o desconto será de 11%;                 * 
# ********************************************************************************

# O print dos valores aparecerão na tela varias vezes.
# Foi criada a função total_value para reduzir a duplicidade do código
def total_value(total_value,total_discount):
		print(f"O valor SEM desconto: R${total_value:.2f}")
		print(f"O valor COM desconto: R${total_discount:.2f}")

print("Bem-vindo a Loja do Igor da Mota Rabelo")

# Primeiro while True para garantir que seja digitado valor
# de produto valido sem que seja encerrado o programa
while True:
	value = input("Entre com o valor do produto: ").replace(",",".")
	if not value.replace(".","").isnumeric() or float(value) <= 0 if len(value.rsplit(".")) <= 2 else True :
		print("Valor invalido. Entre com valor valido por favor.")
	
	else:
		# Segundo while True para garantir que seja digital um valor 
		# de quantidade valida sem que seja encerrado o programa
		while True:
			quantity = input("Entre com a quantidade do produto: ")
			if not quantity.isnumeric() or int(quantity) <= 0:
				print("Quantidade invalida. Entre com uma quantidade valida por favor.")
			
			else:

				# Bloco definirá se o usuário receberá desconto ou não a partir
				# do valor final da ordem e baseado nos requisitos definidos pelo cliente
				total = float(value) * int(quantity) # Calculo do valor final do pedido do usuário
				if total < 2500:
					print("Não há desconto para valor inferior a R$2500.00")
					print(f"O valor total SEM desconto: R${total:.2f}")
				elif total >= 2500 and total < 6000:
					total_value(total,(total-(total*0.04)))
				elif total >= 6000 and total < 10000:
					total_value(total,(total-(total*0.07)))
				else:
					total_value(total,(total-(total*0.11)))
				break		
		break

