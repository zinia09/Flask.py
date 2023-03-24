from flask import render_template, url_for, request, redirect
from models import db, app, Project
from datetime import datetime

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def add_project():
    projects = Project.query.all()
    if request.form:
        new_project = Project(title=request.form['title'], date=datetime.strptime(request.form['date'], '%Y-%m'),
                              description=request.form['description'], skills=request.form['skills'],
                              github=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=projects)


@app.route('/projects/<id>')
def detail(id):
    project = Project.query.get(id)
    skill_list = project.skills.split(", ")
    return render_template('detail.html', project=project, skill_list=skill_list)


@app.route('/projects/<id>/edit',  methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get(id)
    if request.form:
        project.title = request.form['title']
        project.date = datetime.strptime(request.form['date'], '%Y-%m').date()
        project.description = request.form['description']
        project.skills = request.form['skills']
        project.github = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit-project.html', project=project)


@app.route('/projects/<id>/delete')
def delete_project(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
