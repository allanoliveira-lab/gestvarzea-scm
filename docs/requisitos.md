# GestVárzea – Visão geral e requisitos

## 1. Visão geral

O GestVárzea é uma plataforma web para organizar campeonatos de futebol amador. Substitui
planilhas e grupos de mensagem por um sistema único, acessível pelo celular, onde organizadores
cadastram o campeonato e torcedores acompanham jogos, classificação e fazem palpites.

- **Arquitetura:** backend em Python (Flask) com API REST e banco SQLite; aplicativo em Flutter Web.
- **Publicação:** hospedado na nuvem (Render) com domínio próprio.

## 2. Atores

| Ator | Descrição |
|---|---|
| Organizador | Cria o campeonato, cadastra times e lança resultados |
| Torcedor | Consulta tabela e classificação e faz palpites |

## 3. Requisitos funcionais

| ID | Requisito |
|---|---|
| RF01 | Cadastrar campeonatos e times participantes |
| RF02 | Gerar automaticamente a tabela de jogos (todos contra todos) |
| RF03 | Lançar o resultado de cada partida |
| RF04 | Calcular a classificação (pontos, saldo de gols, vitórias) |
| RF05 | Permitir palpites dos torcedores nas partidas |
| RF06 | Compartilhar resultados em imagem nas redes sociais |

## 4. Requisitos não funcionais

| ID | Requisito |
|---|---|
| RNF01 | Interface responsiva, pensada para uso no celular |
| RNF02 | Senhas e chaves fora do código-fonte (variáveis de ambiente) |
| RNF03 | Todo artefato do projeto versionado em repositório Git |
