import io
from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = '1234'

@app.route("/")
def hello_world():
    return "<p>Hello!</p>"

@app.route("/api/inscricao", methods=['POST'])
def inscreverEmail():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    return jsonify({"message:": f"Nome: {name}, Email: {email}"})

if __name__ == '__main__':
    app.run(debug=True)
