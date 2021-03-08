from flask import Flask, Response, request
import main

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  return Response("{'status': '400', 'message': 'Bad request. Read the documentation at 1pt.co/api'}", status=400, mimetype="application/json")

@app.route('/status', methods=['GET'])
def status():
  response = Response("{'status': '200', 'message': 'I'm alive!'}", status=200, mimetype="application/json")
  response.headers['Access-Control-Allow-Origin'] = '*'
  return response



@app.route('/addURL', methods=['GET'])
def add_URL():
  short = request.args.get("short")
  long = request.args.get("long")

  if(long == None):
    response = Response("{'status': '400', 'message': 'Bad request. Read the documentation at 1pt.co/api'}", status=400, mimetype="application/json")
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

  return(main.add_row(short, long))

@app.route('/getURL', methods=['GET'])
def get_URL():
  short_url = request.args.get("url")

  return(main.get_row(short_url))

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
  response = Response("{'status': '404', 'message': 'Not found'}", status=404, mimetype="application/json")
  response.headers['Access-Control-Allow-Origin'] = '*'
  return response

app.run(host='0.0.0.0')
