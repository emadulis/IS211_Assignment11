#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""To Do List"""

from flask import Flask, render_template, request, redirect
import re
app = Flask(__name__)

tasks = []

class Task:
    email = None
    task = None
    priority = None

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/submit', methods= ['POST'])
def submit():
    desc = request.form['task']
    priority = request.form['priority']
    email = request.form['email']
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return render_template('index.html', tasks=tasks)
    else:            
        task = Task()
        task.task = desc
        task.priority = priority
        task.email = email
        tasks.append(task)
        return render_template('index.html', tasks=tasks)

@app.route('/clear')
def clear():
    while len(tasks) > 0:
        for item in tasks:
            tasks.pop()
    return redirect('/')

if __name__ == '__main__':
    app.run()
