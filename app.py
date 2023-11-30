
from flask import Flask, render_template, request, redirect
#importando da classe flask que está no modulo flask
#importando o request = requisição
#importando o redirect = para redirecior para a rota


app = Flask(__name__)
#criação de objeto utilizando a classe flask
#o argumento_name_ é para localizar os arquivos dependendo do nome

class cadpokemon:
    def __init__(self, numero, nome, tipo, altura, peso):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.altura = altura
        self.peso = peso

lista = []
@app.route('/')
def hello_world():  # put application's code here
    return 'começando!'
#diz ao flask que quando alguém
#tem que lembrar de colocar /bianca no localhost, ou / o que tiver naquele /

@app.route('/Pokemon')
def pokemon():
    #renderizar nosso html
    return render_template('Pokemon.html', Titulo="Pokémons Iniciais: ", ListaPokemons=lista)

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = "Cadastro de Pokemon")

#criando uma rota INTERMEDIARIA
#vai receber um metodo post quando for chamada
#ela vai cadastrar todos os campos do cadastrar
@app.route('/criar', methods=['POST'])
def criar():
    numero = request.form['numero']
    nome = request.form['nome']
    tipo = request.form['tipo']
    altura = request.form['altura']
    peso = request.form['peso']
    obj = cadpokemon(numero,nome,tipo,altura,peso)

    #o append ta colocando as informações na lista
    lista.append(obj)
    return redirect('/Pokemon')

#criando uma rota para excluir
@app.route('/excluir/<numeropkm>', methods=['GET', 'DELETE'])
def excluir(numeropkm):
    for i, pkm in enumerate(lista):
        #o enumerate está vendo quando itens tem na minha lista
        #se tiver o numero
        if pkm.numero==numeropkm:
            #apaga ele da lista
            lista.pop(i)
            break

    return redirect('/Pokemon')

@app.route('/editar/<numeropkm>', methods=['GET'])
def editar(numeropkm):
    for i, pkm in enumerate(lista):
        if pkm.numero==numeropkm:
            return render_template("Editar.html", pokemon=pkm, Titulo="Alterar Pokemon")

@app.route('/alterar', methods=['POST', 'PUT'])
def alterar():
    numero = request.form['numero']
    for i, pkm in enumerate(lista):
        if pkm.numero == numero:
            pkm.nome = request.form['nome']
            pkm.tipo = request.form['tipo']
            pkm.altura = request.form['altura']
            pkm.peso = request.form['peso']
    return redirect('/Pokemon')

if __name__ == '__main__':
    app.run()

#SOBRE AS PASTAS:
#static: armazenar arquivos estáticos, como imagens, css e js. São arquivos estáticos, ou seja, não mudam
#templates: é usada para armazenar templates html que o flask usará para renderizar paginas web

