# Projeto_Framework_Testes_C114_Eng_de_Software

O projeto visa apresentar a utilização do framework Unittest, o qual é uma ferramenta para teste de unidade em Python, para se testar uma Classe dessa linguagem de programação.

### 📋 Pré-requisitos

- Ter instalada alguma versão do Python para execução do projeto. Essa execução poderá ser feita utilizando tanto o terminal quanto alguma IDE.

## 🚀 Executando os testes

- Basta executar o arquivo test.py, o qual contém a classe de teste e alguns métodos já implementados.
- Para execução no terminal: </br>
1°) Garanta que o terminal esteja aberto na pasta do projeto; </br>
2°) Execute o comando: *

```
python -m unittest test/test.py
```

*Se a versão do Python que estiver instalada em sua máquina for a partir do Python 3, executar o comando: 
```
python3 -m unittest test/test.py
```

### ⚙️ Testes

**test_cafeicultor:** verifica se um objeto cafeicultor é instanciado corretamente, analisando o atributo nome.

**test_arrayVazio:** verifica se o array é inicializado vazio, ou seja, com comprimento igual a 0.

**test_arrayAppend:** verifica se um elemento é adicionado corretamente no array de clientes, ou seja, se o comprimento após a adição é 1 e se a lista contém o cliente.

**test_arrayPop:** verifica se o clinete é corretamente removido do array, ou seja, se o comprimento após a remoção é 0 e se a lista não contém o cliente. Além disso, verifica se o retorno do pop é igual ao elemento adicionado anteriormente.

**test_arrayException:** verifica se uma exceção do tipo IndexError é lançada ao tentar remover um elemento da lista vazia.

## 🛠️ Construído com

* [Unittest](https://docs.python.org/3/library/unittest.html) - O framework de teste usado.

## ✒️ Autores


* **Mariana Helena Inês Moreira** - [Mariana](https://github.com/Mariana-Helena)
* **Sinara Pimenta Medeiros** - [Sinara](https://github.com/SinaraPimenta)

---
⌨️ com ❤️ 
