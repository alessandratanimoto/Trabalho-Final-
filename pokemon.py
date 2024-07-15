import random


class jogoPokemon:
    def __init__(self, nome, tipo, hp, atk):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.atk = atk

    def informacoes(self):
        print(f'''
        Nome: {self.nome}
        Tipo: {self.tipo}
        HP: {self.hp}
        Ataque: {self.atk}
        ''')

def capturar_pokemons(pokemons_d,pokemons_c): #d = disponíveis/c = capturados
    pokemon_novo = random.choice(pokemons_d)
    pokemons_c.append(pokemon_novo)
    print(f"Você capturou um {pokemon_novo.nome}!")

def ver_pokemons_capturados(capturar_pokemons):
    if capturar_pokemons:
        print("Os pokémons capturados foram: ")
        for i, pokemon in enumerate(capturar_pokemons, 1):
            print(f"{i}: {pokemon.nome}")

    else:
        print("Nenhum pokémon foi capturado ainda.")

def pokemon_batalhas(pokemons_c):
    if len(pokemons_c) < 2:
        print("Você precisa ter no mínimo dois pokémons capturados para iniciar uma batalha.")
        return
    
    print(f"Escolha seus pokémons para batalhar:")

    for i,p in enumerate(pokemons_c):
        print(f"{i}. {p.nome}")

    p1_index = int(input("Escolha o primeiro Pokémon (número): ")) - 1
    p2_index = int(input("Escolha o segundo Pokémon (número): ")) - 1

    pokemon1 = pokemons_c[p1_index]
    pokemon2 = pokemons_c[p2_index]

    print(f"{pokemon1.nome}(HP:{pokemon1.hp}, Ataque: {pokemon1.atk}) VS {pokemon2.nome}(HP:{pokemon2.hp}, Ataque: {pokemon2.atk})")

    while pokemon1.hp > 0 and pokemon2.hp > 0:
        pokemon2.hp -= pokemon1.atk
        if pokemon2.hp <= 0:
            print(f"{pokemon1.nome} venceu a batalha!")
            break

        pokemon1.hp -= pokemon2.atk
    
        if pokemon1.hp <= 0:
            print(f"{pokemon2.nome} venceu a batalha!")
            break

def ver_info_pokemon_especifico(pokemons_c):
    ver_pokemons_capturados(pokemons_c)
    if pokemons_c:
            p_index = int(input("Escolha um Pokémon para ver mais informações sobre ele (número): ")) - 1
            pokemons_c[p_index].informacoes()

def main():
    pikachu = jogoPokemon("Pikachu", "Elétrico", 35, 55)
    charmander = jogoPokemon("Charmander", "Fogo", 39, 52)
    bulbasaur = jogoPokemon("Bulbasaur", "Planta", 45, 49)
    squirtle = jogoPokemon("Squirtle", "Água", 44, 48)
            
    pokemons_d = [pikachu, charmander, bulbasaur, squirtle]
    pokemons_c = []

    while True:
        print('''
                Menu:
    
        1: Capturar Pokémon.
        2: Ver Pokémon Capturados.
        3: Batalha Pokémon.
        4: Ver Informações de um Pokémon Específico.
        5: Sair
                ''')

        escolha = input("Escolha uma das opções acima: ")

        if escolha == '1':
            capturar_pokemons(pokemons_d, pokemons_c)
        elif escolha == '2':
            ver_pokemons_capturados(pokemons_c)
        elif escolha == '3':
            pokemon_batalhas(pokemons_c)
        elif escolha == '4':
            ver_info_pokemon_especifico(pokemons_c)
        elif escolha == '5':
            print("Encerrando o jogo. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
        main()