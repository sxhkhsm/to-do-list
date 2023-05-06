from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

with open('tasks.json') as f:
    tasks = json.load(f)

# Get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    sort_by = request.args.get('sort_by', 'id')
    sorted_tasks = sorted(tasks, key=lambda k: k[sort_by])
    response = jsonify(sorted_tasks)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Get a task by ID
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task:
        response = jsonify(task)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        response = jsonify({"message": "Task not found"}), 404
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

# Add a new task
@app.route('/api/tasks', methods=['POST'])
def add_task():
    task = request.json
    task['id'] = len(tasks) + 1
    tasks.append(task)
    response = jsonify(task)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Delete a task by ID
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task:
        tasks.remove(task)
        response = jsonify({"message": "Task deleted successfully"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        response = jsonify({"message": "Task not found"}), 404
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    

with open('personalGoals.json') as f:
    goals = json.load(f)

# Get all goals
@app.route('/api/goals' ,methods=['GET'])
def get_goals():
    sort_by = request.args.get('sort_by', 'id')
    sorted_goals = sorted(goals, key=lambda k: k[sort_by])
    response = jsonify(sorted_goals)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Get a task by ID
@app.route('/api/goals/<int:goal_id>' , methods=['GET'])
def get_goal(goal_id):
    goal = next((item for item in goals if item["id"] == goal_id), None)
    if goal:
        response = jsonify(goal)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        response = jsonify({"message": "goal not found"}), 404
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

# Add a new goal
@app.route('/api/goals', methods=['POST'])
def add_goal():
    goal = request.json
    goal['id'] = len(goals) + 1
    goals.append(goal)
    response = jsonify(goal)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Delete a goal by ID
@app.route('/api/goals/<int:goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
    goal = next((item for item in goals if item["id"] == goal_id), None)
    if goal:
        goals.remove(goal)
        response = jsonify({"message": "goal deleted successfully"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        response = jsonify({"message": "goals not found"}), 404
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
with open('works.json') as f:
    works = json.load(f)

# Get all works
@app.route('/api/works' , methods=['GET'])
def get_works():
    sort_by = request.args.get('sort_by', 'id')
    sorted_works = sorted(works, key=lambda k: k[sort_by])
    response = jsonify(sorted_works)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Get a work by ID
@app.route('/api/works/<int:work_id>' , methods=['GET'])
def get_work(work_id):
    work = next((item for item in works if item["id"] == work_id), None)
    if work:
        response = jsonify(work)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        response = jsonify({"message": "work not found"}), 404
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

# Add a new work
@app.route('/api/works', methods=['POST'])
def add_work():
    work = request.json
    work['id'] = len(works) + 1
    works.append(work)
    response = jsonify(work)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Delete a work by ID
@app.route('/api/works/<int:work_id>', methods=['DELETE'])
def delete_work(work_id):
    work = next((item for item in works if item["id"] == work_id), None)
    if work:
        works.remove(work)
        response = jsonify({"message": "work deleted successfully"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        response = jsonify({"message": "work not found"}), 404
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

if __name__ == '__main__':
    app.run(debug=True)
