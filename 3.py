#Questão 3

class Planeta:
    def __init__(self, nome, raio_equatorial, distancia_do_sol, composicao):
        self.nome = nome
        self.raio_equatorial = raio_equatorial
        self.distancia_do_sol = distancia_do_sol # em milhões de km
        self.composicao = composicao

    def apresentar(self):
        print(f"Planeta: {self.nome}")
        print(f"Raio Equatorial: {self.raio_equatorial} km")
        print(f"Distância do Sol: {self.distancia_do_sol} milhões de km")
        print(f"Composição: {self.composicao}")

def distancia_em_UA(distancia_milhoes_km):
    return distancia_milhoes_km / 150

# Criando objetos com dados reais aproximados e pesquisados
terra = Planeta("Terra", 6371, 150, "Rochoso")
jupiter = Planeta("Júpiter", 69911, 770, "Gasoso")
marte = Planeta("Marte", 3389, 228, "Rochoso")

print("\n--- Sistema Solar ---")
planetas = [terra, jupiter, marte]

# Teste
for planeta in planetas:
    planeta.apresentar()
    distancia_ua = distancia_em_UA(planeta.distancia_do_sol)
    print(f"Distância até o Sol em UA: {distancia_ua:.2f}")
    print("-" * 30)
