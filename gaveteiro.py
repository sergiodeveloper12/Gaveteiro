class Gaveta:

    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.roupa = None


class Organizador:

    def __init__(self):

        self.gavetas = {
            "9": Gaveta("9", "Camisa Polo"),
            "8": Gaveta("8", "Bermuda"),
            "7": Gaveta("7", "Cueca e Meia"),
            "6": Gaveta("6", "Camisa Social")
        }

    def guardar_roupa(self, roupa, numero):

        if numero in self.gavetas:

            gaveta = self.gavetas[numero]

            if gaveta.roupa is None:
                gaveta.roupa = roupa
                print(roupa, "guardada na gaveta", gaveta.tipo)

            else:
                print("A gaveta já está ocupada por", gaveta.roupa)

        else:
            print("Gaveta inválida")

    def mostrar_status(self):

        print("\nSTATUS DAS GAVETAS\n")

        for gaveta in self.gavetas.values():

            if gaveta.roupa is None:
                print("Gaveta", gaveta.numero, "-", gaveta.tipo, "→ VAZIA")

            else:
                print("Gaveta", gaveta.numero, "-", gaveta.tipo, "→ EM USO | Roupa:", gaveta.roupa)


organizador = Organizador()

while True:

    print("\n===== MENU =====")
    print("1 - Guardar roupa")
    print("2 - Ver status das gavetas")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        roupa = input("Digite o nome da roupa: ")

        print("(9) Camisa Polo")
        print("(8) Bermuda")
        print("(7) Cueca e Meia")
        print("(6) Camisa Social")

        gaveta = input("Escolha a gaveta: ")

        organizador.guardar_roupa(roupa, gaveta)

    elif opcao == "2":

        organizador.mostrar_status()

    elif opcao == "3":

        print("Saindo do organizador...")
        break

    else:
        print("Opção inválida")