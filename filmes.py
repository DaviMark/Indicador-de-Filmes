from flask import Flask, render_template, request, jsonify
import requests
import os
import sys
import webbrowser
import threading

# Verifica se a aplicação está empacotada com PyInstaller
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
else:
    template_folder = 'templates'

app = Flask(__name__, template_folder=template_folder)

API_KEY = '7959e8162abae1e19311d0242bda8d45'
BASE_URL = 'https://api.themoviedb.org/3'

GENRES = {
    'ação': 28,
    'comédia': 35,
    'drama': 18,
    'fantasia': 14,
    'terror': 27,
    'romance': 10749,
    'ficção científica': 878,
    'aventura': 12,
    'mais assistidos': 'popular',
    'recém lançados': 'now_playing',
    'mais premiados': 'top_rated'  # Adicionando a opção de mais premiados
}

def buscar_filmes_por_genero(genero_id):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genero_id}&language=pt-BR"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return []

    filmes = resposta.json().get('results', [])
    for filme in filmes:
        poster_path = filme.get('poster_path')
        filme['poster_url'] = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
        filme['sinopse'] = filme.get('overview')  # Adicionando a sinopse
        filme['avaliacao'] = filme.get('vote_average')  # Adicionando a avaliação
    return filmes

def buscar_mais_assistidos():
    return buscar_filmes('popular')

def buscar_recem_lancados():
    return buscar_filmes('now_playing')

def buscar_mais_premiados():
    return buscar_filmes('top_rated')

def buscar_filmes(tipo):
    url = f"{BASE_URL}/movie/{tipo}?api_key={API_KEY}&language=pt-BR"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return []

    filmes = resposta.json().get('results', [])
    for filme in filmes:
        poster_path = filme.get('poster_path')
        filme['poster_url'] = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
        filme['sinopse'] = filme.get('overview')  # Adicionando a sinopse
        filme['avaliacao'] = filme.get('vote_average')  # Adicionando a avaliação
    return filmes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/filmes', methods=['POST'])
def filmes():
    genero = request.form['genero'].lower()
    
    if genero == 'mais assistidos':
        filmes = buscar_mais_assistidos()
    elif genero == 'recém lançados':
        filmes = buscar_recem_lancados()
    elif genero == 'mais premiados':
        filmes = buscar_mais_premiados()
    elif genero in GENRES:
        genero_id = GENRES[genero]
        filmes = buscar_filmes_por_genero(genero_id)
    else:
        return jsonify({'error': 'Gênero inválido.'})
    
    return jsonify(filmes)

def abrir_navegador():
    webbrowser.open('http://127.0.0.1:5000')

if __name__ == "__main__":
    # Inicia o servidor Flask em uma nova thread e abre o navegador
    threading.Thread(target=abrir_navegador).start()
    app.run(debug=True)
