from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# lista de tarefas
tasks = []


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add_task", methods=["POST"])
def adicionar_tarefa():
    new_task = request.form.get("Tarefa")
    tasks.append(new_task)
    return redirect(url_for("index"))


# Principal
if __name__ == "__main__":
    app.run()
