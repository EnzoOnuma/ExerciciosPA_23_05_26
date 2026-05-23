class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

p1 = Produto("Celular", 1000)
print(f"Nome: {p1.nome}")
print (f"Preço: {p1.preco}")