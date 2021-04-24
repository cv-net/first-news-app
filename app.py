from flask import Flask
from flask import render_template
app = Flask(__name__) 

@app.route('/')
def index():
    template = 'index.html'
    return render_template(template)

#Configure Flask to make a page at site's root URL
if __name__ == '__main__':
    #fire up flask test server
    app.run(debug=True, use_reloader=True)