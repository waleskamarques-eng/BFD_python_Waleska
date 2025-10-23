#Questão 1

# Classe Carro
class Carro:
    def __init__(self, modelo, marca, ano, potencia, cambio, preco):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.potencia = potencia
        self.cambio = cambio
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Ano de lançamento: {self.ano}")
        print(f"Potência: {self.potencia}")
        print(f"Câmbio: {self.cambio}")
        print(f"Preço de lançamento: R$ {self.preco:.2f}")
        print("-" * 40)


# Criação dos objetos (instâncias)
carro1 = Carro("Civic", "Honda", 2020, "2.0", "Automático", 120000)
carro2 = Carro("Corolla", "Toyota", 2019, "1.8", "Automático", 110000)
carro3 = Carro("Onix", "Chevrolet", 2021, "1.0", "Manual", 65000)

# Teste do método
print("--- Informações dos Carros ---")
carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()
