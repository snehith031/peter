from flask import *
app=Flask(__name__)
@app.route('/')
def index():
 respu= make_response(render_template('index.html'))
 respu.set_cookie('somecookiename', 'COOKIE IS IN')
 respu.set_cookie('somecookie', 'COOKIE IS SUS')
 return respu
@app.route('/getcookie1')
def get_cookie1():
 c1 = request.cookies.get('somecookiename')
 return c1
@app.route('/getcookie2')
def get_cookie2():
 c2=request.cookies.get('somecookie')
 return c2
if __name__=="__main__":
 app.run(debug=True)
