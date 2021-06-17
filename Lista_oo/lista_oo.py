"""
1 - Crie uma classe para representar uma pessoa, com os atributos privados de nome, 
idade e altura. Crie os métodos publicos necessarios para sets e gets e também um
método para imprimir os dados de uma pessoa.
"""

"""class Pessoa:
    def __init__(self: object, nome: str, idade: int, altura: float):
        self.__nome = nome 
        self.__idade = idade
        self.__altura = altura

    @property
    def nome(self: object) -> str:
        return self.__nome
    @property
    def idade(self: object) -> int:
        return self.__idade
    @property
    def altura(self: object) -> float:
        return self.__altura
    @nome.setter
    def nome(self: object, nome: str) -> None:
        self.__nome = nome
    @idade.setter
    def idade(self: object, idade: int) -> None:
        self.__idade = idade
    @altura.setter
    def altura(self: object, altura: float) -> None:
        self.__altura = altura
    def __str__(self):
        return f"Nome: {self.nome} \nIdade {self.idade} \nAltura: {self.altura}"
p1 = Pessoa("Flávio", 20, 1.70)
print(p1)"""


"""
2 - Crie uma classe Agenda que pode armazenar 10 pessoas e seja capaz de realizar
as seguintes operações:
    * void armazenarPessoa(String nome, int idade, float altura);
    * void remove Pessoa(String nome);
    * int buscarPessoa(String nome); // informa em que posição da agenda está a pessoa
    * void imprimeAgenda(); // imprime os dados de todas as pessoas da agenda
    * void imprimePessoa(int index); // imprime os dados da pessoa que está na posição "i" da agenda
"""
from typing import List
class Agenda:
    i = 10
    def __init__(self: object, nome: str, idade: int, altura: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__altura: float = altura
        Agenda.i += 1

    @property
    def nome(self: object) -> str:
        return self.__nome
    @property
    def idade(self: object) -> int:
        return self.__idade
    @property 
    def altura(self: object) -> float:
        return self.__altura
    
    @nome.setter
    def nome(self: object, nome: str) -> None:
        self.__nome = nome
    @idade.setter
    def idade(self: object, idade: int) -> None:
        self.__idade = idade
    @altura.setter
    def altura(self: object, altura: float) -> None:
        self.__altura = altura

    def __str__(self):
        return f"Nome: {self.nome} \nIdade {self.idade} \nAltura: {self.altura:.2f}"
    def armazenar_pessoa(self: object, nome: str, idade: int, altura: float):
        for index in range(i):
            self.nome = input("Digite nome do contato: ")
            self.idade: int = int(input("Digite idade do contato: "))
            self.altura: float = float(input("Digite altura do contato: "))

"""
3 - Crie uma classe denominado Elevador para armazenar as informações de um elevador
dentro de um prédio. A classe deve armazenar o andar atual (terreo = 0), 
total de andares no predio, excluindo o terreo, capacidade do elevador, e quantas pessoas estão
presentes nele.
    A classe deve também disponibilizar os seguites métodos:
    * Inicializar: que deve receber como parametros a capacidade do elevador e o
    total de andares no predio ( os elevadores sempre começão no térreo e vazio);
    * Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
    * Sai: Para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
    * Sobe: para subir um andar (não deve subir se já estiver no ultimo andar);
    * Desce: para descer um andar (não deve descer se já estiver no terro);
    * Encapsular todos os atributos da classe (criar métodos set e get);
"""

             




