# Uma possível solução
```python
# Armazenamento dos cadastros
nomes = []
cpfs = []
nascimentos = []

# Lê o ID
uid = input('ID (opcional): ')

# Lê o primeiro nome
nome = input('Primeiro nome: ')

# Lê o sobrenome
sobrenome = input('Sobrenome (apenas o último): ')

# Adiciona o sobrenome ao nome
nome += ' ' + sobrenome

# Lê o CPF
cpf = input('CPF (apenas dígitos): ')
  
# Lê a data de nascimento
data_nasc = input('Data de nascimento (dd/mm/aaaa): ')

if uid == '':  # ID não preenchido
  # Insere cadastro no final
  nomes.append(nome)
  cpfs.append(cpf)
  nascimentos.append(data_nasc)
else:  # ID preenchido
  # Insere cadastro na posição correspondente ao ID
  nomes.insert(int(uid) - 1, nome)
  cpfs.insert(int(uid) - 1, cpf)
  nascimentos.insert(int(uid) - 1, data_nasc)
```