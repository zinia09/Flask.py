from flask import render_template, url_for, request, redirect
from models import db, app, Project


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def add_project():
    if request.form:
        new_project = Project(title=request.form['title'], date=request.form['date'],
                              description=request.form['description'], skills=request.form['skills'],
                              github_link=request.form['github_link'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


@app.route('/projects/<id>')                            # detail route
def detail():
    return render_template('detail.html')


@app.route('/projects/<id>/edit')                       # edit/update route
def edit():
    return render_template('projectform.html')


@app.route('/projects/<id>/delete')                     # delete route
def delete():
    return


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
