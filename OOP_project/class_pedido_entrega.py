from class_pedido import Pedido

class Pedido_Entrega(Pedido):
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor
    def __init__(self, codido_pedido, cliente):
        super().__init__(codido_pedido, cliente)
        self.__endereco_entrega = super()._cliente._enderecos[0]  # Endereço de entrega padrão

    @property
    def _endereco_entrega(self):
        return self.__endereco_entrega

    @_endereco_entrega.setter
    def _endereco_entrega(self, value):
        self.__endereco_entrega = value

    def toString(self):
        str_line = "** INÍCIO DAS INFORMAÇÕES DO PEDIDO **"
        print(str_line, end='\n')
        str_line = "CÓDIGO DO PEDIDO:" + str(self._codigo_pedido)
        print(str_line, end='\t')
        str_line = "STATUS DO PEDIDO:" + \
            str(self._status)  # (0-aberto | 1-finalizado)
        print(str_line, end='\n')
        str_line = "CEP ENDEREÇO PARA ENTREGA:" + \
            str(self._endereco_entrega._cep)
        print(str_line, end='\t')
        str_line = "RUA:" + str(self._endereco_entrega._rua)
        print(str_line, end='\t')
        str_line = "BAIRRO/CIDADE PARA ENTREGA:" + \
            str(self._endereco_entrega._bairro) + "/" + \
            str(self._endereco_entrega._cidade)
        print(str_line, end='\n')
        str_line = "QUANTIDADE DE ITENS DO PEDIDO:" + \
            str(self.quantidade_itens_pedido())
        print(str_line, end='\n')
        dbl_preco_total = 0.0
        for i, item in enumerate(self._itens_pedidos):
            str_line = "\t #ITEM:" + str(i)
            print(str_line, end='\t')
            str_line = "PRODUTO:" + str(item._produto._descricao)
            print(str_line, end='\t')
            str_line = "QTD (#):" + str(item._quantidade)
            print(str_line, end='\t')
            str_line = "SUBTOTAL (R$):" + str(item._preco_item)
            dbl_preco_total += item._preco_item
            print(str_line, end='\n')
        str_line = "PREÇO TOTAL DO PEDIDO:" + str(dbl_preco_total)
        print(str_line, end='\n')
        str_line = "** FIM DAS INFORMAÇÕES DO PEDIDO **"
        print(str_line, end='\n')
