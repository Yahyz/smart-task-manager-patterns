from flask import Flask, render_template, request, redirect
from manager import TaskManager
from task import Task
from observer import EmailNotifier, SMSNotifier
from strategy import SortByName, SortByPriority, TaskSorter

app = Flask(__name__)

manager = TaskManager()

# ✅ Store notifications
notifications = []

email = EmailNotifier(notifications)
sms = SMSNotifier(notifications)

@app.route('/')
def home():
    return render_template('index.html', tasks=manager.tasks, notifications=notifications)

@app.route('/add', methods=['POST'])
def add_task():
    name = request.form['name']
    priority = int(request.form['priority'])

    task = Task(name)
    task.priority = priority

    task.attach(email)
    task.attach(sms)

    manager.add_task(task)
    return redirect('/')

@app.route('/clear_notifications')
def clear_notifications():
    notifications.clear()
    return redirect('/')

@app.route('/update/<int:index>', methods=['POST'])
def update_task(index):
    status = request.form['status']
    task = manager.tasks[index]

    task.change_status(status)

    if status == "Done":
        manager.tasks.pop(index)

    return redirect('/')

@app.route('/sort/<type>')
def sort_tasks(type):
    if type == 'name':
        sorter = TaskSorter(SortByName())
    else:
        sorter = TaskSorter(SortByPriority())

    manager.tasks = sorter.sort_tasks(manager.tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)