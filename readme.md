# Busca de Filmes por Gênero

Este projeto é uma aplicação web simples desenvolvida com Flask que permite aos usuários buscar filmes por gênero utilizando a API do The Movie Database (TMDb). O usuário pode selecionar um gênero de filme e, em seguida, visualizar uma lista de filmes correspondentes, incluindo sinopses e imagens dos pôsteres.

## Funcionalidades

- Selecione um gênero de filme a partir de um menu suspenso.
- Visualize uma lista de filmes com o título, pôster e sinopse.
- Respostas formatadas de maneira amigável para o usuário.

## Tecnologias Utilizadas

- **Flask**: Framework web em Python.
- **HTML/CSS**: Para a construção da interface do usuário.
- **Bootstrap**: Para estilização responsiva e rápida.
- **API do TMDb**: Para buscar informações sobre filmes.

## Requisitos

- Python 3.x
- Flask
- Requests
- PyInstaller (opcional, para empacotar a aplicação)

## Como Executar

1. **Clone o repositório**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>


2. **Instale as dependências**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux ou macOS
    venv\Scripts\activate     # Para Windows

3. **Instale o Flask e Requests:**
    ```bash
    pip install Flask requests

## 4. **Configure a API do TMDb**
Inscreva-se em The Movie Database (TMDb) para obter uma chave de API e substitua API_KEY no código com sua chave de API.

5. **Execute a aplicação**
    ```bash
    python conv.py

6. **Empacotar a aplicação**
    ```bash
    pip install pyinstaller

**Em seguida, execute o seguinte comando:**
    ```bash
    pyinstaller --onefile --add-data "templates:templates" filmes.py



