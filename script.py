import sys
import requests
import oracledb

# CONFIGURACOES DO BANCO ORACLE 
# Coloque aqui o seu RM e a sua senha do Oracle da FIAP
ORACLE_USER = "seu_rm"
ORACLE_PASSWORD = "sua_senha"
ORACLE_DSN = "oracle.fiap.com.br:1521/ORCL"

# API COINGECKO
API_URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false"

def definir_categoria(market_cap_bilhoes):
    if market_cap_bilhoes >= 100:
        return "MEGA CAP"
    elif market_cap_bilhoes >= 10:
        return "LARGE CAP"
    else:
        return "MID/SMALL CAP"


def transformar_dados(dados_brutos):
    print("[2/4] Transformando dados em memoria...")
    dados_processados = []

    for item in dados_brutos:
        coin_id = item.get("id", "").strip().lower()
        symbol = item.get("symbol", "").strip().upper()
        nome = item.get("name", "").strip().upper()

        preco_usd = float(item.get("current_price") or 0)
        market_cap = float(item.get("market_cap") or 0)

        market_cap_bilhoes = round(market_cap / 1_000_000_000, 2)

        categoria = definir_categoria(market_cap_bilhoes)

        dados_processados.append({
            "id": coin_id,
            "symbol": symbol,
            "nome": nome,
            "preco_usd": preco_usd,
            "market_cap_bilhoes": market_cap_bilhoes,
            "categoria": categoria
        })

    print(f"-> {len(dados_processados)} registros transformados com sucesso.")
    return dados_processados