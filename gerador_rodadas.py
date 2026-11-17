# === GESTVÁRZEA - GERADOR DE RODADAS ===
# Versão 1.0 - Tabela "todos contra todos" em turno único (método do círculo)
# Autor: Allan Oliveira - A-Logic Soluções


def gerar_rodadas(times):
    """Recebe a lista de times e devolve a lista de rodadas.

    Cada rodada é uma lista de jogos (mandante, visitante).
    Com número ímpar de times, um time folga em cada rodada.
    """
    lista = list(times)
    if len(lista) < 2:
        return []
    if len(lista) % 2 != 0:
        lista.append(None)  # None = folga

    n = len(lista)
    rodadas = []
    for r in range(n - 1):
        jogos = []
        for i in range(n // 2):
            casa = lista[i]
            fora = lista[n - 1 - i]
            if casa is None or fora is None:
                continue
            # alterna o mando para equilibrar jogos em casa
            if r % 2 == 1 and i == 0:
                casa, fora = fora, casa
            jogos.append((casa, fora))
        rodadas.append(jogos)
        # gira todos menos o primeiro (método do círculo)
        lista = [lista[0]] + [lista[-1]] + lista[1:-1]
    return rodadas


def imprimir_tabela(rodadas):
    for numero, jogos in enumerate(rodadas, start=1):
        print(f"--- Rodada {numero} ---")
        for casa, fora in jogos:
            print(f"  {casa} x {fora}")
    print()


if __name__ == "__main__":
    times = ["Unidos FC", "Real Sátiro", "Botafogo da Vila", "Ypiranga", "Juventude", "Estrela"]
    rodadas = gerar_rodadas(times)
    print(f"Campeonato com {len(times)} times: {len(rodadas)} rodadas\n")
    imprimir_tabela(rodadas)
