from flask import Flask, render_template, request, redirect, url_for
from tb import gerar_tabela

app = Flask(__name__)


@app.route('/')
def pagina_apresentacao():
    return  render_template("apresentacao.html")

@app.route('/fundamentacao')
def pagina_fundamentacao():
    return  render_template("fundamentacao.html")


@app.route('/tabela', methods=['GET','POST'])
def pagina_tabela():
    controlador_exibicional = False
    mensagem_erro = False
    if request.method == 'POST':
        if  request.form.get("tabela").isnumeric():
            retorno_funcao_gerar = gerar_tabela(int(request.form.get("tabela")))
            controlador_exibicional  = True
            return render_template("gerador.html", tabela = retorno_funcao_gerar[0], num_linhas = retorno_funcao_gerar[1], exibicao_tabela = controlador_exibicional, erro = mensagem_erro)
        mensagem_erro = True
        return render_template("gerador.html", exibicao_tabela = controlador_exibicional, erro = mensagem_erro)
    return render_template("gerador.html", exibicao_tabela = controlador_exibicional, erro = mensagem_erro)


if __name__ == '__main__':
    app.run()