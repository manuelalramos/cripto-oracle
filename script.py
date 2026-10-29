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