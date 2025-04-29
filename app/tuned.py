import requests
import os
from dotenv import load_dotenv
from pprint import pprint
import json

load_dotenv()

# VARIAVEIS DE AMBIENTE
API_KEY_HELIX = os.getenv("API_KEY_HELIX")

# TODO:
# [X] Buscar as regras no helix
# [X] separar as regras tuned
# [X] Regra de referencia (TRELLIX ENDPOINT ENS [DAC])
# [X] salvar o nome da regra e o tuned


# FUNÇOES ------------------------>

# Função para buscar as regras no Helix
def get_rules():
    all_rules = []
    offset = 0
    limit = 100

    url = "https://apps.fireeye.com/helix/id/hexmcz675/api/v1/rules/"
    headers = {
        'accept': 'application/json',
        'x-fireeye-api-key': API_KEY_HELIX
    }

    while True:
        params = {
            'limit': limit,
            'offset': offset,
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            rules = data.get('rules', [])
            if not rules:
                break  # Exit loop if no more rules are returned

            all_rules.extend(rules)
            offset += limit  # Increment offset for the next batch
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None
        
    print(f"Total de regras encontradas: {len(all_rules)}")
    return all_rules

# Função para salvar as regras em um arquivo JSON
def save_rule(rules, filename="rules.json"):
    try:
        # verifica se o arquivo existe, se nao existir cria um novo
        if not os.path.exists(filename):
            with open(filename, 'w', encoding='utf-8') as file:
                pass

        with open(filename, 'w', encoding='utf-8') as file:
            # Escreve os dados no arquivo JSON
            json.dump(rules, file, ensure_ascii=False, indent=4)
        print(f"Arquivo {filename} criado com sucesso.")
    except IOError as e:
        print(f"Erro ao criar o arquivo: {e}")

# Função para filtrar as regras que estão tuned
def get_tuned(input_file="rules.json"):
    tuneds = []
    # Filtra as regras que estão tuned
    try:
        with open(input_file , 'r', encoding='utf-8') as file:
            rules = json.load(file)
        
        for rule in rules:
            if rule.get('isTuned') == True:
                data = {
                'Nome': rule.get('message'),
                'Modificação': rule.get('tuningSearch')
                }
                tuneds.append(data)
        save_rule(tuneds, "tuned.json")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
    
# FUNÇOES ------------------------>


# EXECUÇÃO
# save_rule(get_rules())
get_tuned()