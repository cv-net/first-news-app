import csv
from flask import Flask
from flask import render_template
app = Flask(__name__) 

def get_csv():
#open csv, save it to variable
    csv_path = './static/la-riots-deaths.csv'
    csv_file = open(csv_path, 'r')
#csv module DictReader, parse csv and return list of dictionaries
    csv_obj = csv.DictReader(csv_file)
#convert csv object to a permanent list so it doesnt disappear on use
    csv_list = list(csv_obj)
    return csv_list

@app.route('/')
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['id'] == row_id:
            return render_template(template, object=row)
    abort(404)

#Configure Flask to make a page at site's root URL
if __name__ == '__main__':
    #fire up flask test server
    app.run(debug=True, use_reloader=True)