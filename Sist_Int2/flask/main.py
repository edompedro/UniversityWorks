from flask import Flask, json, render_template, redirect, session, request
from flask import redirect

app = Flask(__name__)

app.secret_key = "adim"

# abrir o json e lê os dados
with open("alunos.json", "r") as f:
    alunos = json.load(f)

@app.route("/")
def home():
    return render_template("login.html")

@app.route('/user/<username>')
def user(username):
    return f'Hello, {username}!'

@app.route("/about")
def about():
    text = "This is the about page."
    return render_template("about.html", text=text)

# ROUTE TO ADD
@app.route("/chamada", methods=["GET", "POST", "DELETE"])
def chamada():      
    if request.method == "POST" and request.form['type'] == 'Adicionar':
        novo_nome = request.form["nome"]
        nova_matricula = request.form["matricula"]
        print(novo_nome, nova_matricula)
        alunos[str(novo_nome)] = int(nova_matricula)
        # Salvar num arquivo json
        with open("alunos.json", "w") as f:
            json.dump(alunos, f)

    return render_template("chamada.html", alunos=alunos)
    
# ROUTE TO DELETE
@app.route('/chamada/<nome>/<type>', methods=["POST"])
def removeUser(nome,type):
    if request.method == "POST" and type == 'DELETE':
        del alunos[nome]
        with open("alunos.json", "w") as f:
            json.dump(alunos, f)
    return render_template("chamada.html", alunos=alunos)

# ROUTE TO SIGNIN
@app.route("/signin", methods=["POST"])
def signin():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        student_number = request.form["studentNumber"]
        password = request.form["password"]
        app.secret_key = email
        session["username"] = student_number
        print(session.items())  # dict_items([('username', value)])
        return redirect(f"/user/{app.secret_key}")


if __name__ == "__main__":
    app.run(debug=True) 