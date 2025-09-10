from class_pessoa import Pessoa
from class_endereco import Endereco

class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, endereco: Endereco):
        super().__init__(nome, idade, cpf)
        self.__enderecos = [endereco]
    
    @property
    def _enderecos(self):
        return self.__enderecos
    
    def adicionar_endereco(self, endereco: Endereco):
        self.__enderecos.append(endereco)

    def remover_endereco(self, endereco: Endereco):
        if endereco in self.__enderecos:
            self.__enderecos.remove(endereco)
        else:
            raise ValueError("Endereço não encontrado na lista de endereços do cliente.")
    
    def toString(self):
        return f"Cliente: {self._nome}, Idade: {self._idade}, CPF: {self._cpf}, Endereço primário: [{self.__enderecos[0].toString()}]"