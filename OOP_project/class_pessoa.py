class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__telefone = None

    @property
    def _nome(self):
        return self.__nome
    
    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _idade(self):
        return self.__idade
    
    @_idade.setter
    def _idade(self, value):
        self.__idade = value

    @property
    def _cpf(self):
        return self.__cpf
    
    @_cpf.setter
    def _cpf(self, value):
        self.__cpf = value

    @property
    def _telefone(self):
        return self.__telefone
    
    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

    

    