from datetime import datetime
from class_pedido import Pedido

class Pagamento:
    def __init__(self, pedido: Pedido):
        self.__pedido = pedido
        self.__tipo = 0
        self.__data = datetime.now()
        self.__valor = self.__pedido._valor_total
        self.__pagamento_efetuado = False
        self.__tipos = {
        0: "Débito",
        1: "Crédito",
        2: "Dinheiro",
        3: "Pix"
    }

    @property
    def _tipo(self):
        return self.__tipo

    @_tipo.setter
    def _tipo(self, value):
        self.__tipo = value

    @property
    def _data(self):
        return self.__data

    @_data.setter
    def _data(self, value):
        self.__data = value

    @property
    def _valor(self):
        return self.__valor

    @_valor.setter
    def _valor(self, value):
        self.__valor = value

    @property
    def _pagamento_efetuado(self):
        return self.__pagamento_efetuado

    @_pagamento_efetuado.setter
    def _pagamento_efetuado(self, value):
        self.__pagamento_efetuado = value
        if not value:
            print("O pagamento não foi efetuado!!")
        else:
            print("O pagamento foi realizado com sucesso")
            print("Conte sempre com nossos serviços!!!")

    @property
    def _pedido(self):
        return self.__pedido
    
    @property
    def _tipos(self):
        return self.__tipos
    
    def realizar_pagamento(self):
        if not self.__pagamento_efetuado:

            print(f"Forma de pagamento: {self.__tipo}")
            self.__data = datetime.now()
            print(f"Data: {self.__data.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"valor total: {self.__valor:.2f} R$")
            self.__pagamento_efetuado = True
            print(f"Status: {self.__pagamento_efetuado} Pagamento efetuado com sucesso!!")
            
        else:
            print("Esse pagamento já foi realizado anteriormente!!")

    def imprimir_nota_fiscal(self):
        if self.__pagamento_efetuado == True:
            nota = open(f"nota_fiscal{self.__pedido._codigo_pedido}.txt", "w", encoding="utf-8")
            nota.write(f"Nota Fiscal - Pedido: {self.__pedido._codigo_pedido}\n")
            nota.write(f"Forma de Pagamento: {self._tipos[self._tipo]}\n")
            for item in self.__pedido._itens_pedidos:
                nota.write(f"Produto: {item._produto._descricao}, Quantidade: {item._quantidade}, Subtotal: {item._preco_item:.2f} R$\n")
            nota.write(f"Data do Pedido: {self.__data.strftime('%d/%m/%Y %H:%M:%S')}\n")
            nota.write(f"Valor Total: {self.__valor:.2f} R$\n")
            nota.write("Obrigado por comprar conosco!\n")
        else:
            print("Pagamento não efetuado. Não é possível imprimir a nota fiscal.")