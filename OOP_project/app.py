from class_endereco import Endereco
from class_item_pedido import ItemPedido
from class_pedido import Pedido
from class_produto import Produto
from class_pedido_local import Pedido_Local
from class_pedido_entrega import Pedido_Entrega
from class_cliente import Cliente
from class_pagamento import Pagamento

from datetime import datetime

def menu_principal():  # MENU PRINCIPAL
    print('''
        MENU Principal:
        [1] - Controle de vendas
        [2] - Cadastrar novo produto
        [3] - Remover um produto
        [4] - Pesquisar um produto
        [5] - Cadastrar um cliente
        [6] - Buscar cliente
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

def menu_pedido():
    print('''
        MENU Vendas:
        [1] - Abrir novo pedido
        [2] - Adicionar item ao pedido
        [3] - Remover item do pedido
        [4] - Listar itens do pedido em detalhes
        [5] - Finalizar pedido e imprimir
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

def pedido_finalizar():
    print("Finalizar pedido:")
    int_codigo_pedido = int(input('Informe o código do pedido para finalizar: '))
    if buscar_pedido_por_codigo(int_codigo_pedido):
        # verificar se pedido existe
        pedido = pedidos[int_codigo_pedido]
        # Verifica se o pedido já foi finalizado
        if pedido._status == 1:
            print("Este pedido já foi finalizado!")
            return False
        else:
            # Cria um objeto Pagamento
            pagamento = Pagamento(pedido = pedido)
            pagamento._tipo = int(input('Informe a forma de pagamento (débito = 0/crédito = 1/dinheiro = 2/pix = 3): '))
            pagamento.realizar_pagamento()
            # Imprime a nota fiscal
            pagamento.imprimir_nota_fiscal()
            # Altera o status do pedido para finalizado
            pedido._status = 1
            print("Pedido finalizado com sucesso!")
    else:
        print("Pedido inexistente")
        return False

def cadastrar_cliente():
    print("Cadastro de cliente:")
    str_nome = str(input('Informe o nome do cliente: '))
    int_idade = int(input('Informe a idade do cliente: '))
    str_cpf = str(input('Informe o CPF do cliente: '))
    endereco_cliente = cadastrar_endereco()
    # criando objeto cliente
    cliente = Cliente(str_nome, int_idade, str_cpf, endereco_cliente)
    # adicionando cliente ao sistema
    clientes[cliente._cpf] = cliente
    return cliente

def buscar_cliente_por_cpf():
    print("Busca de cliente:")
    cpf = input('Informe o CPF do cliente: ')
    # Verifica se existe cliente cadastrado
    for chave in clientes.keys():
        if chave == cpf:
            return clientes[cpf]
    return print("Cliente não encontrado!")

def pedido_adicionar():
    print("Novo pedido:")
    tipo = str(input('Informe o tipo de pedido (entrega = 0/local = 1): '))
    if tipo == "0":
        # código pedido gerado automaticamente
        cliente = buscar_cliente_por_cpf()
        if not cliente:
            cliente = cadastrar_cliente()
        codido_pedido = int(len(pedidos)) + 1
        return Pedido_Entrega(codido_pedido, cliente)
    elif tipo == "1":
        # código pedido gerado automaticamente
        cliente = buscar_cliente_por_cpf()
        if not cliente:
            cliente = cadastrar_cliente()
        mesa = int(input('Informe o número da mesa: '))
        # a numeração do pedido começa de 1 até n
        codido_pedido = int(len(pedidos)) + 1
        return Pedido_Local(codido_pedido, cliente, mesa)
    else:
        print("Tipo de pedido inválido!")
        return False

def pedido_adicionar_item():
    print("Adicionar item ao pedido:")
    int_pedido_selecionado = int(input('Informe o código do pedido para adicionar um novo item: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_produto = int(input('Informe o código do produto para adicionar ao pedido: '))
        produto = buscar_produto_por_codigo(int_codigo_produto)
        if produto:
            int_quantidade_item = int(input('Informe a quantidade do item:'))
            novo_item_pedido = ItemPedido(produto, int_quantidade_item)
            pedido.adicionar_item_ao_pedido(novo_item_pedido)
        else:
            print("Não foi possível adicionar este produto, pois o código do produto não existe!")
        #return Pedido(codido_pedido, endereco_pedido)
    else:
        print("Pedido inexistente")
        return False
    
def pedido_remover_item():
    print("Remover item do pedido:")
    int_pedido_selecionado = int(input('Informe o código do pedido para remover um item selecionado: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_item = int(input('Informe o número do item para remover deste pedido ' + str(pedido._codigo_pedido) + ': '))
        # verifica se número intem informado existe: não faz sentido remover item 5 se ele não existe
        if int_codigo_item < 0 or int_codigo_item >= pedido.quantidade_itens_pedido():
            print("Número do item inválido!")
            return False
        #if pedido.quantidade_itens_pedido() <= int_codigo_item:
        pedido.remover_item_pedido(int_codigo_item)
    else:
        print("Pedido inexistente")
        return False
    
def pedido_listar_items():
    print("Listar itens do pedido:")
    int_pedido_selecionado = int(input('Informe o código do pedido para mais detalhes: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        pedido.toString()
    else:
        print("Pedido inexistente")
        return False
    
def cadastrar_endereco():
    print("Cadastro de endereço:")
    str_cep = str(input('Informe o cep do endereço: '))
    str_rua = str(input('Informe a rua: '))
    int_num = int(input('Informe o número: '))
    str_complemento = str(input('Informe o complemento do endereço: '))
    str_bairro = str(input('Informe o bairro: '))
    str_cidade = str(input('Informe a cidade: '))
    endereco = Endereco(str_cep, str_rua, int_num,
                        str_complemento, str_bairro, str_cidade)
    return endereco

def cadastrar_produto():
    print("Cadastro de produto:")
    int_codigo = int(input('Informe o código identificador do produto: '))
    str_nome = str(input('Qual o nome/descrição do produto? '))
    flt_preco = float(input('Informe o valor (ex. 0.00): '))
    date_validade = (input('Informe a validade do produto (formato dd/mm/aaaa): '))
    date_validade = datetime.strptime(date_validade, '%d/%m/%Y')
    return Produto(int_codigo, str_nome, flt_preco, date_validade)

def remover_produto():
    print("Remover produto:")
    int_codigo_remocao = int(input('Informe o código do produto para remoção: '))
    produto_remover = estoque_produtos[int_codigo_remocao]
    print("Produto (" + produto_remover._descricao + ") removido!") 
    del estoque_produtos[int_codigo_remocao]

def buscar_produto_por_codigo(int_codigo_produto):
    print("Busca de produto:")
    # Verifica se existe produto cadastrado
    for chave in estoque_produtos.keys():
        if chave == int_codigo_produto:
            return estoque_produtos[int_codigo_produto]
    return False

def buscar_pedido_por_codigo(int_codigo_pedido):
    print("Busca de pedido:")
    # Verifica se existe produto cadastrado
    for chave in pedidos.keys():
        if chave == int_codigo_pedido:
            return pedidos[int_codigo_pedido]
    return False

# Aplicação de exemplo disciplina POO - UFRB
# Sistema de controle de pedidos
# Professor Guilherme Braga Araújo

estoque_produtos = {}
pedidos = {}
clientes = {}

while True:
    # menu_principal
    opcao_escolhida = menu_principal()
    # verificando escolha
    # opc sair
    if (opcao_escolhida == "s"):
        break
    # opc 1
    elif (opcao_escolhida == "1"):
        while True:
            opcao_escolhida = menu_pedido()
            # opc menu vendas - novo pedido
            if (opcao_escolhida == "1"):
                pedido = pedido_adicionar()
                if (pedido):
                    # adiciona pedido ao sistema
                    pedidos[pedido._codigo_pedido] = pedido
            # opc menu vendas - adicionar item    
            elif (opcao_escolhida == "2"):
                pedido_adicionar_item()
            elif (opcao_escolhida == "3"):
                pedido_remover_item()
            elif (opcao_escolhida == "4"):
                pedido_listar_items()
            elif (opcao_escolhida == "5"):
                pedido_finalizar()
            else:
                # Volta para o menu principal
                break
               
    # opc 2
    elif (opcao_escolhida == "2"):
        produto = cadastrar_produto()
        if (produto):
            # adiciona produto ao nosso estoque
            estoque_produtos[produto._codigo_produto] = produto
    # opc 3
    elif (opcao_escolhida == "3"):
        remover_produto()
    # opc 4
    elif (opcao_escolhida == "4"):
        int_codigo_produto = int(input('Informe o código do produto para busca: '))
        produto_pesquisa = buscar_produto_por_codigo(int_codigo_produto)
        if (produto_pesquisa):
            print("Produto encontrado:")
            print(">Código=" + str(produto_pesquisa._codigo_produto))
            print(">Descricao=" + produto_pesquisa._descricao)
            print(">Valor=" + str(produto_pesquisa._preco))
            print(">Validade=" + str(produto_pesquisa._validade))
        else:
            print("Produto nâo cadastrado/encontrado.")
    # opc 5
    elif (opcao_escolhida == "5"):
        cliente = cadastrar_cliente()
    # opc 6
    elif (opcao_escolhida == "6"):
        cliente = buscar_cliente_por_cpf()
        print(cliente.toString() if cliente else print("Cliente não encontrado!"))
    else:
        print("A opção escolhida é inválida.")
