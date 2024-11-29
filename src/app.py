from flask import Flask,jsonify,request
app = Flask(__name__)

todos = [
  {"label": "My task 1", "done": False },
  {"label": "My task 2", "done": False },
  {"label": "My task 3", "done": False }
]

# @app.route('/todos', methods=['GET'])
# def hello_world():
#     return "<h1>Hello!</h1>"

@app.route('/todos', methods=['GET'])
def taskList():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete:", position)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['PUT'])
def edit_todo(position):
    todos[position] = request.json
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)