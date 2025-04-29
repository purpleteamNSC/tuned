# Rules Tuned in Helix

Este projeto é uma ferramenta para gerenciar regras do Helix, permitindo buscar, filtrar e salvar regras específicas em arquivos JSON.

## Funcionalidades

- **Buscar Regras**: Faz requisições à API do Helix para obter todas as regras disponíveis.
- **Filtrar Regras Tuned**: Identifica e separa as regras que estão marcadas como "tuned".
- **Salvar Regras**: Salva as regras obtidas ou filtradas em arquivos JSON.

## Requisitos

- Python 3.8 ou superior
- Biblioteca `requests`
- Biblioteca `python-dotenv`

## Instalação

1. Clone este repositório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API do Helix:
    ```
    API_KEY_HELIX=SuaChaveDeAPI
    ```

## Uso

1. **Buscar e salvar todas as regras**:
    Descomente a linha `save_rule(get_rules())` no final do script para salvar todas as regras em um arquivo `rules.json`.

2. **Filtrar regras tuned**:
    Execute o script para gerar o arquivo `tuned.json` com as regras filtradas.

## Estrutura do Código

- `get_rules()`: Busca todas as regras da API do Helix.
- `save_rule(rules, filename)`: Salva as regras em um arquivo JSON.
- `get_tuned(input_file)`: Filtra as regras marcadas como "tuned" e salva em um arquivo separado.

## Exemplo de Execução

```bash
python script.py
```

## Observações

- Certifique-se de que sua chave de API do Helix está válida e possui permissões para acessar as regras.
- O script cria os arquivos `rules.json` e `tuned.json` na raiz do projeto.

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
