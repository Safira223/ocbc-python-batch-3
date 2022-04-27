from flask import Flask, request, render_template
# from flask import request
# from flask import render_template
from markupsafe import escape

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '<h2>Hello, World</h2>'

# HTML Escaping
# http://127.0.0.1:5000/fira
@app.route('/<name>')
def hello(name):
    return f"Hello,{escape(name)}!"

# Routing
@app.route('/')
def index():    
    # return 'Index Page'
    return render_template ('hello.html')

@app.route('/hello/')
def hello():    
    return 'Hello, World'

# Variable Rules
@app.route('/user/<username>')
def show_user_profile(username):    
    # show the user profile for that user    
    return f'User {escape(username)}'

@app.route('/book/<string:title>')
def show_book_title(title):    
    # show the post with the given id, the id is an integer    
    return f'Detail Book : {escape(title)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):    
    # show the post with the given id, the id is an integer    
    return f'Post {post_id}'

@app.route('/post/<string:post_id_str>')
def show_post_str(post_id_str):    
    # show the post with the given id, the id is an integer    
    return f'Post {post_id_str}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):    
    # show the subpath after /path/    
    return f'Subpath {escape(subpath)}'

# HTTP Methods
@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':        
        return do_the_login()    
    else:        
        return show_the_login_form()

def do_the_login():
    return 'Do the login ...'

def show_the_login_form():
    return 'Displaying login to form ...'

# Rendering Templates
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):    
    # return 'Hello, World'
     return render_template('hello_name.html', name=name)

if __name__ == '__main__':  
    # cara run manual 
    # app.run()
    # cara run auto update
    app.run(debug=True)    

