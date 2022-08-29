import os
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    alunos = "Tudo vai dar certo, caros alunos, confiem!"
    return alunos

@app.route('/calcular')
def calculadora():
    v1 = request.args.get('a')
    v2 = request.args.get('b')
    operacao = request.args.get('operacao')

    try:
        a = int(v1)
    except ValueError:
        abort(404)

    try:
        b = int(v2)
    except ValueError:
        abort(404)

    if (operacao == 'soma'):
        resultado = a + b

    if(operacao == 'sub'):
        resultado = a - b

    if (operacao == 'div'):
        resultado = a / b

    if (operacao == 'mult'):
        resultado = a * b

    return str(resultado)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)
