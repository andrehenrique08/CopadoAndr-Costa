"""
Copa do Mundo 2026 - Flask App
"""

from flask import Flask, render_template, request, redirect, url_for

config = {
    "username": "Andre Henrique"
}

app = Flask(__name__)

dados = [[config['username']]]
lista = []


@app.route("/", methods=["GET"])
def home():
    return render_template("base.html", lista_front=lista, lista_dados=dados)


@app.route("/add", methods=["POST"])
def add():
    selecao = request.form.get("selecao")
    continente = request.form.get("continente")
    titulos = request.form.get("titulos")

    if selecao != '' and continente != '' and titulos != '':
        entry = [selecao.strip(), continente.strip(), titulos.strip()]
        lista.append(entry)
        print('Add: {}'.format(lista))
    else:
        print('** Seleção não cadastrada: todos os campos devem ser preenchidos **')

    return redirect(url_for("home"))


@app.route("/sort", methods=["POST"])
def sort():
    if lista:
        print('** Ordenando a lista **')
        lista.sort()

    return redirect(url_for("home"))


@app.route("/reverse", methods=["POST"])
def reverse():
    global lista

    if lista:
        print('** Invertendo a lista **')
        lista = sorted(lista, reverse=True, key=lambda x: x[0])

    return redirect(url_for("home"))


@app.route("/clear", methods=["POST"])
def clear():
    global lista

    print('==> Apagando toda a lista <==')
    lista = []

    return redirect(url_for("home"))


@app.route("/delete/<selecao_nome>", methods=["GET"])
def delete(selecao_nome):
    print('==> Removendo: {}'.format(selecao_nome))

    for i in range(len(lista)):
        if selecao_nome in lista[i]:
            del lista[i]
            break

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
    