# Checkpoint 5 – Pipeline CoinGecko → Oracle

Projeto do Checkpoint 5 da disciplina **Computational Thinking using Python** (FIAP – Prof. Fernando Almeida).

O programa pega as **10 maiores criptomoedas** na API da CoinGecko, faz alguns tratamentos nos dados em Python e salva o resultado numa tabela no **Oracle da FIAP**.

## Integrantes

| Nome | RM |
| --- | --- |
| Lena Haidar Halawi | RM572258 |
| Manuela de Lima Ramos | RM572956 |

## Como funciona

1. **Consome a API** – faz um GET em `https://api.coingecko.com/api/v3/coins/markets` usando `requests` e trata erros de conexão, timeout e status HTTP (404, 500 etc.).
2. **Transforma os dados** – padroniza os textos (id em minúsculo, símbolo e nome em maiúsculo), converte o valor de mercado para bilhões de dólares e classifica cada moeda em `MEGA CAP`, `LARGE CAP` ou `MID/SMALL CAP`.
3. **Salva no Oracle** – conecta com `oracledb`, cria a tabela `TB_CRIPTOMOEDAS` (se ainda não existir), apaga o ranking antigo e insere o novo. Se tudo der certo faz `commit()`, se der erro faz `rollback()`.

## Como rodar

```bash
pip install requests oracledb
```

Abra o `Script.py` e coloque seu RM e sua senha do Oracle:

```python
ORACLE_USER = "seu_rm"
ORACLE_PASSWORD = "sua_senha"
```

Depois é só rodar:

```bash
python Script.py
```

Para ver os dados no SQL Developer:

```sql
SELECT * FROM TB_CRIPTOMOEDAS ORDER BY MARKET_CAP_BILHOES DESC;
```

## Tecnologias

- Python 3
- requests
- oracledb
- Oracle Database (FIAP)
- API pública CoinGecko