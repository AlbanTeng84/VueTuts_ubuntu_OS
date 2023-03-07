from flask import Flask,render_template

app = Flask(__name__)

@app.route('/click')
def clickHandle():
        print("OK")

@app.route('/')
def Hello():
    return render_template("index.html")




if __name__== '__main__':
    app.run()