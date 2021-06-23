from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def Home():
    return render_template('Home.html')

@app.route('/Socials')
def Socials():
    return render_template('Socials.html')

@app.route('/Github')
def Github():
    return render_template('Github.html')

@app.route('/Projects')
def Projects():
    return render_template('Projects.html')


if __name__=='__main__':
    app.run(host="0.0.0.0", port="443")
