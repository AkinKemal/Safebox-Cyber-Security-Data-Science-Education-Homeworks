from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/todoapp' # PostgreSQL bağlantı URL'si
db = SQLAlchemy(app)

# Veritabanı modeli
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Todo %r>' % self.id

# Ana sayfa
@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

# Yeni todo ekleme
@app.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    new_todo = Todo(content=content)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))

# Todo silme
@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
