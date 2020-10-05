class Cafeicultor(object):
    nome: str
    telefone: str
    cpf: str
    cidade: str
    endereco: str
    agencia_bancaria: str
    numero_da_conta: str
    nome_do_banco: str

    def __init__(self, nome="",telefone="", cpf="", cidade="", endereco="",nome_do_banco="", agencia_bancaria="",numero_da_conta=""):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.cidade = cidade
        self.endereco = endereco
        self.agencia_bancaria = agencia_bancaria
        self.numero_da_conta = numero_da_conta
        self. nome_do_banco: nome_do_banco