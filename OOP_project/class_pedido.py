from class_cliente import Cliente
from class_item_pedido import ItemPedido

# definição da classe
class Pedido:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor
    def __init__(self, codido_pedido, cliente: Cliente):
        self.__codigo_pedido = codido_pedido
        self.__status = 0 # 0 = aberto, 1 = finalizado/pago
        # criando uma estrutura map em python para armzenar itens do pedido
        self.__itens_pedidos = []
        self.__valor_total = 0.0
        self.__cliente = cliente

    @property
    def _cliente(self):
        return self.__cliente
    
    @_cliente.setter
    def _cliente(self, value):
        if not isinstance(value, Cliente):
            raise TypeError("O cliente deve ser uma instância da classe Cliente.")
        self.__cliente = value

    @property
    def _valor_total(self):
        for item in self.__itens_pedidos:
            self.__valor_total += item._preco_item
        return self.__valor_total
    
    @property
    def _status(self):
        return self.__status

    @_status.setter
    def _status(self, value):
        self.__status = value

    @property
    def _codigo_pedido(self):
        return self.__codigo_pedido

    @_codigo_pedido.setter
    def _codigo_pedido(self, value):
        self.__codigo_pedido = value

    @property
    def _itens_pedidos(self):
        return self.__itens_pedidos

    @_itens_pedidos.setter
    def _itens_pedidos(self, value):
        self.__itens_pedidos = value

    def adicionar_item_ao_pedido(self, itempedido):
        self.__itens_pedidos.append(itempedido)

    def remover_item_pedido(self, codigo_item):
        self.__itens_pedidos.pop(codigo_item)

    def quantidade_itens_pedido(self):
        return int(len(self.__itens_pedidos))
        # return self.__itens_pedidos.__sizeof__