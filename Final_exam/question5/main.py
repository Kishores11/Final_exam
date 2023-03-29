from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://reqres.in/api/users?page=1'
    response = requests.get(url)    #using requests method to get the data from the link
    data = response.json()
    return render_template('table.html', data=data['data'])


app.run(debug=True)

'''
after checking the url by using postman all the information are present inside (data) so we are passing those
as input.After rendering it the final output is displayed as table format 
We can see the output by starting our flask server.

'''