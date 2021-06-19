from flask import Flask, render_template, url_for
app = Flask(__name__)
from OpenSSL import SSL

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) 
context.load_cert_chain('certificate.crt', 'private.key')

comments=[
{
    'title': 'Reliable',
    'name': 'Donald',
    'comment': 'Great for managing employees',
    'date_posted': '16/04/2020'
},
{
    'title': 'Awesome software',
    'name': 'Macklemore',
    'comment': 'Really gets the job done',
    'date_posted': '27/08/2020'   
}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', comments=comments)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/download')
def download():
    return render_template('download.html')


if __name__=='__main__':
    app.run(host="0.0.0.0", ssl_context=context)
