<p align="center">
    <img src="assets/logo_infnet.png" width="70" height="70" />
</p>

# *Assessment*

## Exercício 2

**Atenção:**
- É importante que você desenvolva o programa totalmente, do início ao fim, na IDE do Replit (**AQUI MESMO!!**⚠️**NÃO crie um repl no seu perfil do Replit para fazer o Assessment**⚠️). Você **NÃO** deve escrever o código em outra IDE e depois copiá-lo para cá.
- **NÃO** é permitido usar nenhum recurso que não faça parte do conteúdo desta disciplina, a menos que explicitamente autorizado no enunciado.
- Use comentários para explicar o que cada parte do código faz.
- Após concluir as tarefas, submeta suas soluções aqui e no Moodle (postando lá os links para seus projetos do Replit).

Neste exercício, você deverá criar um programa que implementa a funcionalidade "Inserir novo cadastro" de um sistema de cadastro de dados pessoais conforme a descrição a seguir.

## Armazenamento dos cadastros

Cada cadastro é composto pelos seguintes dados de uma pessoa:

- **ID**: Nº inteiro positivo que identifica cada cadastro. Esse nº corresponderá à posição de cada cadastro na estrutura de armazenamento. Ou seja, o ID do 1º cadastro será 1, o do 2º será 2 e assim sucessivamente.
- **Nome**: Composto por primeiro nome e um único sobrenome (ex: José Silva).
- **CPF**: Composto por 11 dígitos quaisquer (ex: 99999999999).
- **Data de nascimento**: No formato dd/mm/aaaa (ex: 01/02/1999).

Os dados dos cadastros devem ser armazenados em listas.

## Descrição das funcionalidades

### Inserir novo cadastro

O programa deverá solicitar que o usuário preencha os dados referentes ao novo cadastro (ID, primeiro nome, sobrenome, CPF e data de nascimento).

O único campo opcional é o ID, que pode ser deixado em branco pelo usuário.

Se o usuário informar o ID, o cadastro deverá ser inserido com o ID informado (na posição correspondente). Caso haja cadastros com ID maior ou igual ao inserido, seus IDs serão atualizados para corresponderem às novas posições ocupadas, conforme o exemplo abaixo.

Suponha que os cadastros abaixo já existem:
- ID 1 (Pessoa A)
- ID 2 (Pessoa B)
- ID 3 (Pessoa C)

No cenário acima, se o usuário solicitar a inserção de um cadastro da Pessoa D com ID 2, o resultado deverá ser o seguinte:
- ID 1 (Pessoa A)
- ID 2 (Pessoa D)
- ID 3 (Pessoa B)
- ID 4 (Pessoa C)

Já se o usuário deixar o ID em branco, o novo cadastro deve ser criado com o próximo ID que ainda não estiver em uso.

*Observações:*

- O arquivo main.py já contém definições de listas que podem ser usadas para o armazenamento dos dados dos cadastros, mas você pode alterá-las como julgar apropriado.
- Você pode alterar o conteúdo das listas manualmente, inserindo alguns dados previamente para facilitar os testes, mas o programa deve funcionar mesmo que as listas estejam vazias.