from flask import Flask, render_templatec
z
app = Flask(__name__, template_folder='template')

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/welcome')
def wellcome():
    return render_template("welcomepage.html")

if __name__ == '__main__':
    app.run()
