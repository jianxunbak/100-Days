from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Boolean, Time, DateTime, Date, ForeignKey
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, SelectField, DateTimeField, TimeField
from wtforms.validators import DataRequired, URL
from datetime import datetime
from flask_ckeditor import CKEditor, CKEditorField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
Bootstrap5(app)
ckeditor = CKEditor(app)
csrf = CSRFProtect(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# create database to store use to do list input
class ToDo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(250), unique=True, nullable=False)
    to_to = db.Column(String(500), nullable=False)
    date = db.Column(Date, nullable=False)
    time = db.Column(Time, nullable=False)
    list_id = db.Column(Integer, ForeignKey('list.id'), nullable=False)
    list = relationship("List", back_populates="todos")
    completed = db.Column(Boolean, default=False)


class List(db.Model):
    __tablename__ = 'list'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), unique=True, nullable=False)
    todos = relationship("ToDo", back_populates="list")


class AddToDo(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    to_to = CKEditorField('Details', validators=[DataRequired()])
    date = DateTimeField("Date", format='%Y-%m-%d', id="date-picker", validators=[DataRequired()])
    time = TimeField("Time", format='%H:%M', validators=[DataRequired()])
    list = SelectField("List", coerce=int, validators=[DataRequired()])
    submit = SubmitField('Add New List')


class CreateListForm(FlaskForm):
    name = StringField("List Name", validators=[DataRequired()])
    submit = SubmitField('Create List')


with app.app_context():
    db.create_all()


# home route to display todo list, check how to create a submit button here also
@app.route("/")
def home():
    results = db.session.execute(db.select(ToDo).order_by(ToDo.id))
    to_do = results.scalars().all()

    results_lists = db.session.execute(db.select(List))
    lists = results_lists.scalars().all()
    list_names = {lst.id: lst.name for lst in lists}

    grouped_todos = {}
    completed_todos = []

    for item in to_do:
        if item.completed:
            completed_todos.append(item)
        else:
            if item.list_id not in grouped_todos:
                grouped_todos[item.list_id] = []
            grouped_todos[item.list_id].append(item)

    print(grouped_todos)  # Debugging output
    print(list_names)  # Debugging output
    return render_template('index.html', grouped_todos=grouped_todos, list_names=list_names, completed_todos=completed_todos)


@app.route('/add-list', methods=["GET", "POST"])
def new_todo():
    page_title = 'New Cafe'
    form = AddToDo()
    form.list.choices = [(lst.id, lst.name) for lst in List.query.all()]

    if form.validate_on_submit():
        if request.method == "POST":
            todo = ToDo(title=form.title.data,
                        to_to=form.to_to.data,
                        date=form.date.data,
                        time=form.time.data,
                        list_id=form.list.data
                        )
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('add.html', form=form, page_title=page_title)


@app.route('/create-list', methods=["GET", "POST"])
def create_list():
    form = CreateListForm()
    if form.validate_on_submit():
        new_list = List(name=form.name.data)
        db.session.add(new_list)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_list.html', form=form)


@app.route('/delete/<int:todo_id>', methods =['POST'])
def delete(todo_id):
    post_to_delete = db.session.execute(db.select(ToDo).where(ToDo.id == todo_id)).scalar()
    if post_to_delete:
        db.session.delete(post_to_delete)
        db.session.commit()
        return jsonify({"success": True})
    return jsonify({"success": False, "error": "Todo item not found"})


@app.route('/completed/<int:todo_id>', methods=['POST'])

def completed(todo_id):
    todo = db.session.execute(db.select(ToDo).where(ToDo.id == todo_id)).scalar()
    if todo:
        todo.completed = True
        db.session.commit()
        return jsonify({"success": True})
    return jsonify({"success": False, "error": "Todo item not found"})


@app.route('/completed')
def all_completed_items():
    results = db.session.execute(db.select(ToDo).where(ToDo.completed == True).order_by(ToDo.id))
    completed_todos = results.scalars().all()

    results_lists = db.session.execute(db.select(List))
    lists = results_lists.scalars().all()
    list_names = {lst.id: lst.name for lst in lists}

    return render_template('completed.html', completed_todos=completed_todos, list_names=list_names)



@app.route('/revert/<int:todo_id>', methods=['POST'])
def revert(todo_id):
    todo = db.session.execute(db.select(ToDo).where(ToDo.id == todo_id)).scalar()
    if todo:
        todo.completed = False
        db.session.commit()
        return jsonify({"success": True})
    return jsonify({"success": False, "error": "Todo item not found"})


@app.route('/update-status/<int:id>', methods=['POST'])
def update_status(id):
    todo = ToDo.query.get_or_404(id)
    # Check if the completed field is set in the form data
    todo.completed = request.form.get('completed') == '1'  # Use boolean logic to update
    todo.completed = completed

    if completed:
        # Mark as completed and move to a completed list (if applicable)
        todo.completed = True
    else:
        # Mark as not completed and move it back to its original list
        todo.completed = False
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
