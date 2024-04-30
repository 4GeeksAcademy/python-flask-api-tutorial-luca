from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_todo():
    new_todo = request.json
    todos.append(new_todo)
    return jsonify(new_todo)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):
        del todos[position]
    return jsonify(todos)


if __name__ == '__main__':
    app.run(debug=True)
