from flask import Flask, request
app = Flask(__name__)  
 
@app.route('/')  
def index():  
    return '<h2>%s</h2>' % request.remote_addr
 
@app.route('/user/<name>')  
def user(name):  
    return '<h2>Hello, %s!</h2><br>' % request.remote_addr
  
if __name__ == '__main__':  
    app.run(debug=False)  