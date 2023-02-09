from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1> LoVe </h1><p>Live the moment</p>'

@app.route('/users/<name>')
def users(name):
    return '<h2>Welcome {}</h2>'.format(name.upper())

if __name__=='__main__':
    app.run(debug=True)