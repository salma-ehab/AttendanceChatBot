from flask import Flask,render_template, request,jsonify
from flask_sqlalchemy import SQLAlchemy
import bot

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Attendee(db.Model):
    name= db.Column(db.String(200), nullable=False)
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/chat", methods=['POST'])
def chat():
    if request.method == 'POST':
        message = request.form['Usermessage']
        responce = bot.bot.reply('user',message)
        return jsonify({'reply': str(responce)})

@app.route('/table')
def table():
    attendees = Attendee.query.order_by(Attendee.name).all()
    return render_template("table.html",attendees=attendees)

if __name__ == "__main__":
    app.run(debug = True)