from bottle import *
import bottle
import os

application = default_app()

@route("/")
def home():
	return template("index.html")

@route('/favicon.ico')
def get_favicon():
	return server_static('/static/sharingan.ico')

#specifying the path for the file
@route('/<filepath:path>')
@route('/anotherPage/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static/')

if __name__=='__main__':
	application.run(reloader=True, host="0.0.0.0", port=int(os.environ.get("PORT", 9594)))