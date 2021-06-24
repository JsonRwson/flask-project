from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def Home():
    return render_template('Home.html')

@app.route('/Projects')
def Projects():
    return render_template('Projects.html')


if __name__=='__main__':
    app.run(host="0.0.0.0", port="443", ssl_context=('/etc/letsencrypt/live/jayjay8182.tk/fullchain.pem', '/etc/letsencrypt/live/jayjay8182.tk/privkey.pem'))
