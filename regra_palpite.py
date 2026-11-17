# === GESTVÁRZEA - REGRA DE PALPITES ===
# Versão 1.1 - Novo artefato: janela de palpites de cada partida
# Autor: Allan Oliveira - A-Logic Soluções
#
# Regra de negócio:
#   - o palpite ABRE 2 dias antes do início da partida;
#   - o palpite FECHA 30 minutos antes do início da partida.

from datetime import datetime, timedelta

ABERTURA_ANTES = timedelta(days=2)
FECHAMENTO_ANTES = timedelta(minutes=30)


def situacao_palpite(inicio_partida, agora=None):
    """Retorna 'AGUARDANDO', 'ABERTO' ou 'ENCERRADO' para a partida."""
    agora = agora or datetime.now()
    abre = inicio_partida - ABERTURA_ANTES
    fecha = inicio_partida - FECHAMENTO_ANTES
    if agora < abre:
        return "AGUARDANDO"
    if agora < fecha:
        return "ABERTO"
    return "ENCERRADO"


def pode_palpitar(inicio_partida, agora=None):
    return situacao_palpite(inicio_partida, agora) == "ABERTO"


if __name__ == "__main__":
    jogo = datetime(2026, 11, 22, 15, 0)  # domingo, 15h
    print(f"Partida: Unidos FC x Real Sátiro - {jogo:%d/%m/%Y %H:%M}\n")
    testes = [
        datetime(2026, 11, 19, 10, 0),   # 3 dias antes
        datetime(2026, 11, 20, 15, 0),   # exatamente 2 dias antes
        datetime(2026, 11, 22, 14, 0),   # 1 hora antes
        datetime(2026, 11, 22, 14, 30),  # 30 minutos antes
        datetime(2026, 11, 22, 16, 0),   # jogo em andamento
    ]
    for momento in testes:
        print(f"{momento:%d/%m %H:%M} -> {situacao_palpite(jogo, momento)}")
