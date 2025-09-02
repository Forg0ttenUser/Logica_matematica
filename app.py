from flask import Flask, render_template
from tb import tabela_verdade, num_linhas

app = Flask(__name__)

cont = 1

@app.route('/')
def hello_world():
    return render_template("index.html", var = tabela_verdade,enum = enumerate, linha = num_linhas)


if __name__ == '__main__':
    app.run()