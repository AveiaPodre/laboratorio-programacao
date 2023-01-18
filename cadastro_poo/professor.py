class professor:
    codigo = 0
    nome = ''

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
    
    def get_codigo(self):
        return self.codigo

    def get_nome(self):
        return self.nome
