# Armazenamento dos cadastros
Primeiro_nome = []
sobrenome = []
cpfs = []
nascimento = []
ID = []
sobren = ""
CP = 0
data = ""
cadastro = 0

#Entrada para usuário
Primeiro = input("Digite seu nome ou se quiser encerrar o programa digite (terminou): ")

#Primeira condição para condicionar o programa
if Primeiro.strip() != "terminou": 

  #Aceitando a condição, o programa da sequencia para coletar os dados do usuário.
  sobren = str(input("Digite seu sobrenome: "))
  CP = input("Digite seu CPF: ")
  data = str(input("Digite sua data de nascimento: "))
  cadastro = int(input("Digite seu ID: "))

#Check
#print(f"cadastro 1 : {cadastro}")
i = 0

#Entrada de loop para executar ação caso o ID já exista:
while Primeiro.strip() != "terminou": 
  
  if cadastro in ID: 
    ID.insert(int(cadastro), cadastro)
    Primeiro_nome.insert(int(cadastro), Primeiro)
    sobrenome.insert(int(cadastro), sobren)
    cpfs.insert(int(cadastro), CP)
    nascimento.insert(int(cadastro), data)
    
#Segunda condição caso o ID seja inexistente
  else:
    Primeiro_nome.append(Primeiro)
    sobrenome.append(sobren)
    cpfs.append(CP)
    nascimento.append(data)
    ID.append(cadastro)
   

#Fim do loop, enquanto a condição não for satisfeita novos registros acontecem. 
  Primeiro = input("Digite seu nome: ")
  
  if Primeiro.strip() != "terminou":
    sobren = input("Digite seu sobrenome: ")
    CP = input("Digite seu CPF: ")
    data = input("Digite sua data de nascimento: ")
    cadastro = input("Digite seu ID: ")
  
  #print(f"cadastro :{i} {cadastro}")
  
  i = i + 1

if i != 0 : 
  print(f"Nomes : {Primeiro_nome}, Sobrenomes: {sobrenome} CPFs : {cpfs}, Datas de nascimento : {nascimento}, IDs : {cadastro}")
else: 
  print("Não há cadastros")
      




  

      

  
  

  
  
  



             