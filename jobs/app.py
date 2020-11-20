import sqlite3
from flask import Flask, render_template, g
import datetime
from flask import Flask, render_template, g, request, redirect, url_for

PATH = 'db/jobs.sqlite'

@@ -45,4 +46,19 @@ def employer(employer_id):
    employer = execute_sql('SELECT * FROM employer WHERE id=?', [employer_id], single=True)
    jobs = execute_sql('SELECT job.id, job.title, job.description, job.salary FROM job JOIN employer ON employer.id = job.employer_id WHERE employer.id = ?', [employer_id])
    reviews = execute_sql('SELECT review, rating, title, date, status FROM review JOIN employer ON employer.id = review.employer_id WHERE employer.id = ?', [employer_id])
    return render_template('employer.html', employer=employer, jobs=jobs, reviews=reviews) 
    return render_template('employer.html', employer=employer, jobs=jobs, reviews=reviews)

@app.route('/employer/<employer_id>/review', methods=('GET', 'POST'))
def review(employer_id):
    if request.method == 'POST':
        review = request.form['review']
        rating = request.form['rating']
        title = request.form['title']
        status = request.form['status']

        date = datetime.datetime.now().strftime("%m/%d/%Y")
        execute_sql('INSERT INTO review (review, rating, title, date, status, employer_id) VALUES (?, ?, ?, ?, ?, ?)', (review, rating, title, date, status, employer_id), commit=True)

        return redirect(url_for('employer', employer_id=employer_id))

    return render_template('review.html', employer_id=employer_id) 