# === GESTVÁRZEA - GERADOR DE RODADAS ===
# Versão 1.1 - Tabela "todos contra todos" com opção de turno e returno
# Autor: Allan Oliveira - A-Logic Soluções
# Mudança v1.1: novo parâmetro ida_e_volta (returno com mando invertido)


def gerar_rodadas(times, ida_e_volta=False):
    """Recebe a lista de times e devolve a lista de rodadas.

    Cada rodada é uma lista de jogos (mandante, visitante).
    Com número ímpar de times, um time folga em cada rodada.
    Se ida_e_volta=True, gera também o returno com o mando invertido.
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

    if ida_e_volta:
        returno = [[(fora, casa) for casa, fora in jogos] for jogos in rodadas]
        rodadas = rodadas + returno
    return rodadas


def imprimir_tabela(rodadas, total_turno=None):
    for numero, jogos in enumerate(rodadas, start=1):
        if total_turno and numero == total_turno + 1:
            print("========== RETURNO ==========")
        print(f"--- Rodada {numero} ---")
        for casa, fora in jogos:
            print(f"  {casa} x {fora}")
    print()


if __name__ == "__main__":
    times = ["Unidos FC", "Real Sátiro", "Botafogo da Vila", "Ypiranga"]
    turno = gerar_rodadas(times)
    rodadas = gerar_rodadas(times, ida_e_volta=True)
    print(f"Campeonato com {len(times)} times em turno e returno: {len(rodadas)} rodadas\n")
    imprimir_tabela(rodadas, total_turno=len(turno))
