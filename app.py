from flask import Flask, render_template, request, redirect, url_for
from tb import gerar_tabela

app = Flask(__name__)




@app.route('/')
def pagina_apresentacao():
    return  render_template("apresentacao.html")

@app.route('/1', methods=['GET','POST'])
def pagina_tabela():
    controlador_exibicional = False
    if request.method == 'POST':
        retorno_funcao_gerar = gerar_tabela(int(request.form.get("tabela")))
        controlador_exibicional = True
        return render_template("index.html", tabela = retorno_funcao_gerar[0], num_linhas = retorno_funcao_gerar[1], exibicao_tabela = controlador_exibicional)
    return render_template("index.html", exibicao_tabela = controlador_exibicional)


if __name__ == '__main__':
    app.run()