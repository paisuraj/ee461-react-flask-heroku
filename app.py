#from django.shortcuts import redirect
from flask import Flask, send_from_directory, redirect


app = Flask(__name__, static_url_path='', static_folder='ui/build/')

@app.route('/')
def index():
    #return send_from_directory('ui/build/', 'index.html')
    return redirect('/home')


@app.route('/home')
def index2():
    return send_from_directory('ui/build/', 'index.html')


@app.route('/checkin')
def checkIn_hardware(projectId, qty):
    
    if qty is None:
        qty = 0
    return f'  hardware checked in'


@app.route('/join')
def joinProject(projectId):
    if projectId is None:
        projectId = 1
    return f'Joined {projectId}'.format(projectId)

@app.route('/leave')
def leaveProject(projectId):
    if projectId is None:
        projectId = 1
    #return f'Left {id}'.format(projectId)
    return 'Left ' + str(projectId)

@app.route('/checkout')
def checkOut_hardware(projectId, qty):
    if qty is None:
        qty = 0
    return f' hardware checked out'


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))