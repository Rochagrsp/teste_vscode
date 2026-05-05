from collections import deque

class SistemaFila:
    def __init__(self):
        self.fila_normal = deque()
        self.fila_prioritaria = deque()
        self.ultimo_numero = 0

    def gerar_senha(self, tipo):
        self.ultimo_numero += 1
        
        senha = f"{tipo}{self.ultimo_numero:03}"
        
        if tipo == "P":
            self.fila_prioritaria.append(senha)
        else:
            self.fila_normal.append(senha)
        
        print(f"Senha gerada: {senha}")

    def chamar_proximo(self):
        if self.fila_prioritaria:
            senha = self.fila_prioritaria.popleft()
        elif self.fila_normal:
            senha = self.fila_normal.popleft()
        else:
            print("Fila vazia!")
            return
        
        print(f"Chamando senha: {senha}")

    def mostrar_filas(self):
        print("\n--- FILAS ---")
        print("Prioritária:", list(self.fila_prioritaria))
        print("Normal:", list(self.fila_normal))


# Simulação
sistema = SistemaFila()

while True:
    print("\n1 - Nova senha normal")
    print("2 - Nova senha prioritária")
    print("3 - Chamar próximo")
    print("4 - Ver filas")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        sistema.gerar_senha("N")
    elif op == "2":
        sistema.gerar_senha("P")
    elif op == "3":
        sistema.chamar_proximo()
    elif op == "4":
        sistema.mostrar_filas()
    elif op == "0":
        break