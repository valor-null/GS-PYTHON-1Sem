# Cidadão Seguro — Monitor de ocorrências da rua

**Global Solution 2026.2 — CitizenTech**
Pensamento Computacional e Automação em Python — Prof. Dr. Allan Roberto Molto
1º ano de Ciência da Computação — FIAP

- Link do video:
 
## Integrantes

| Nome completo | RM |
|---|---|
| Valeria Conceição Dos Santos | RM 574489 |
| Hellen Fabia Assis dos Santos | RM 575236 |
| Maria Eduarda Laines Braga | RM 576030 |

## Introdução

- **Problema:** poste apagado, bueiro entupido, alagamento e árvore caída ficam dias sem solução, e ninguém sabe quais são os mais urgentes. Na chuva ou à noite, colocam o morador em risco.
- **Público beneficiado:** moradores do bairro fictício Vila Aurora, principalmente idosos e quem circula à noite.
- **Objetivo:** registrar as ocorrências da rua, classificar o risco de cada uma e gerar um relatório com indicadores e uma recomendação de prioridade.
- **ODS 11 — Cidades e comunidades sustentáveis:** ruas mais seguras e bem cuidadas.
- **ODS 13 — Ação contra a mudança global do clima:** prioriza problemas que pioram com chuvas intensas.

## Como executar

1. Ter o Python 3 instalado (ou usar um compilador online)
2. Abrir o terminal na pasta do arquivo.
3. Executar:

```
python cidadao_seguro.py
```

4. No menu, escolher:
   - `1` para cadastrar uma ocorrência (rua, tipo e dias em aberto);
   - `2` para ver o relatório;
   - `3` para encerrar.

O programa não precisa de internet nem de bibliotecas externas.

## Regras de classificação

Cada ocorrência recebe um status calculado pela função `classificar(tipo, dias)`:

| Condição | Status | Motivo |
|---|---|---|
| Alagamento há 2 dias ou mais | **Crítico** | Risco imediato para quem passa pela rua |
| Mais de 7 dias em aberto | **Crítico** | Problema abandonado por mais de uma semana |
| De 4 a 7 dias em aberto | **Atenção** | Precisa de acompanhamento |
| Até 3 dias em aberto | **Normal** | Dentro de um prazo razoável |

## Indicadores do relatório

- Total de ocorrências
- Média de dias em aberto (função `calcular_media`)
- Ocorrência mais antiga (maior número de dias)
- Quantidade de ocorrências por status (Normal, Atenção, Crítico)
- Percentual de ocorrências críticas
- Quantidade de ocorrências por tipo

## Recomendação automática

| Situação encontrada | Recomendação exibida |
|---|---|
| 50% ou mais das ocorrências são críticas | Situação grave: mutirão de manutenção e alerta aos moradores |
| Há ocorrências críticas, mas menos de 50% | Priorizar a crítica aberta há mais tempo |
| Nenhuma crítica, mas há itens em Atenção | Acompanhar para não passar de 7 dias |
| Todas normais | Bairro sob controle |

## Teste realizado e resultados

Cadastramos 4 ocorrências de teste:

| Nº | Rua | Tipo | Dias | Status |
|---|---|---|---|---|
| 1 | Rua das Flores | Poste apagado | 10 | Crítico |
| 2 | Av. Brasil | Alagamento | 2 | Crítico |
| 3 | Rua Sete | Bueiro entupido | 5 | Atenção |
| 4 | Praça Central | Poste apagado | 1 | Normal |

Resultados obtidos:

- Total: 4 ocorrências; média de 4,5 dias em aberto.
- Mais antiga: poste apagado na Rua das Flores (10 dias).
- 2 críticas (50%), 1 em atenção e 1 normal.
- Recomendação: situação grave, com mutirão de manutenção e alerta aos moradores.