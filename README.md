# gestvarzea-scm

Repositório da Aula Prática de **Projeto de Software** (U4 – A1 – Gerenciamento de Configuração).

O **GestVárzea** é um sistema real, em produção, para gestão de campeonatos de futebol amador
(várzea): cadastro de times, geração da tabela de jogos, resultados, classificação e palpites.
Neste repositório ficam os artefatos de documentação e módulos isolados do projeto, usados para
praticar o controle de versão com Git e GitHub. O código de produção fica em repositório próprio.

## Itens de configuração

| Artefato | Descrição |
|---|---|
| `README.md` | Documentação do repositório |
| `.gitignore` | Arquivos que o Git deve ignorar |
| `docs/requisitos.md` | Visão geral e requisitos do GestVárzea |
| `gerador_rodadas.py` | Gerador da tabela de jogos (todos contra todos) – v1.0 |

## Como executar

```bash
python gerador_rodadas.py
```

## Histórico de versões

- **v1.0** – Documento de requisitos e gerador de rodadas em turno único.

Autor: Allan Oliveira – A-Logic Soluções
