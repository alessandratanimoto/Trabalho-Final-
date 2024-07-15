class CustosBolsa:
    def __init__(self, tamanho, cor):
        self.cor = cor
        self.tamanho = tamanho
        self.valor_metro = 0.0
        self.qtd_metro = 0
        self.valor_zipper = 0.0
        self.qtd_zipper = 0
        self.valor_alca = 0.0
        self.qtd_alca = 0
        self.bordado = ''

    def definir_custos(self):
        self.valor_metro = float(input(f"Valor do tecido por metro para bolsa {self.tamanho}: "))
        self.qtd_metro = int(input("Quantidade de metros de tecido: "))
        self.valor_zipper = float(input(f"Valor do zipper por metro para bolsa {self.tamanho}: "))
        self.qtd_zipper = int(input("Quantidade de metros de zipper: "))
        self.valor_alca = float(input(f"Valor da alça para bolsa {self.tamanho}: "))
        self.qtd_alca = int(input("Quantidade de alças: "))

        while True:
            self.bordado = input(f"Tamanho do bordado para bolsa {self.tamanho} (P, M, G): ").upper()
            if self.bordado in ["P", "M", "G"]:
                break
            else:
                print("Informação Inválida! Por favor, insira P, M ou G.")

    def calcular_custo_total(self):
        custo_tecido = self.valor_metro * self.qtd_metro
        custo_zipper = self.valor_zipper * self.qtd_zipper
        custo_alca = self.valor_alca * self.qtd_alca
        if self.bordado == "P":
            custo_bordado = 1.00
        elif self.bordado == "M":
            custo_bordado = 1.50
        elif self.bordado == "G":
            custo_bordado = 2.00
        else:
            custo_bordado = 0.0
        
        custo_total = custo_tecido + custo_zipper + custo_alca + custo_bordado
        return custo_total

    def mostrar_informacoes(self):
        custo_tecido = self.valor_metro * self.qtd_metro
        custo_zipper = self.valor_zipper * self.qtd_zipper
        custo_alca = self.valor_alca * self.qtd_alca
        if self.bordado == "P":
            custo_bordado = 1.00
        elif self.bordado == "M":
            custo_bordado = 1.50
        elif self.bordado == "G":
            custo_bordado = 2.00
        else:
            custo_bordado = 0.0

        custo_total = self.calcular_custo_total()

        print(f'''
        Tamanho: {self.tamanho}
        Cor: {self.cor}
        Custo do tecido: R$ {custo_tecido:.2f}
        Custo do zipper: R$ {custo_zipper:.2f}
        Custo da alça: R$ {custo_alca:.2f}
        Custo do bordado: R$ {custo_bordado:.2f}
        Custo total da bolsa: R$ {custo_total:.2f}
        ''')
        return custo_total


def main():
    bolsas = []

    while True:
        tamanho = input("Informe o tamanho da bolsa (P, M, G): ").upper()
        while tamanho not in ["P", "M", "G"]:
            print("Tamanho inválido! Por favor, insira P, M ou G.")
            tamanho = input("Informe o tamanho da bolsa (P, M, G): ").upper()
        
        cor = input("Informe a cor da bolsa: ")

        bolsa = CustosBolsa(tamanho, cor)
        bolsa.definir_custos()
        bolsas.append(bolsa)

        continuar = input("Deseja adicionar outra bolsa? (s/n): ").lower()
        if continuar != 's':
            break

    total_custo_bolsas = 0
    for bolsa in bolsas:
        total_custo_bolsas += bolsa.mostrar_informacoes()

    print(f"Valor total de todas as bolsas adicionadas: R$ {total_custo_bolsas:.2f}")


if __name__ == "__main__":
    main()
