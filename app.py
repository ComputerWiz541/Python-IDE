from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    code = request.form['code']
    try:
        result = subprocess.check_output(['python', '-c', code]).decode()
        return result
    except subprocess.CalledProcessError as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
