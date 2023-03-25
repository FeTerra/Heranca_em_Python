class Pai:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")

class Filho(Pai):
    def __init__(self, nome, idade, brinquedo):
        super().__init__(nome, idade)
        self.brinquedo = brinquedo

    def brincar(self):
        print(f"{self.nome} está brincando com {self.brinquedo}.")

class Neto(Filho):
    def __init__(self, nome, idade, brinquedo, escola):
        super().__init__(nome, idade, brinquedo)
        self.escola = escola

    def estudar(self):
        print(f"{self.nome} está estudando na escola {self.escola}.")
        
p = Pai("João", 45)
f = Filho("Pedro", 10, "bola")
n = Neto("Lucas", 5, "carrinho", "Escola ABC")
