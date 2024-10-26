from flask import Flask, render_template, request, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def process_input():
    Name = request.form['name']
    Gender = request.form['gender']
    Age = request.form['age']
    if Gender.islower() == 'male':
        Gender = 1
    else:
        Gender = 0

    data = [[Age,Gender]]


    from joblib import load
    modal = load('../music_typepredictor.z')
    music = modal.predict(data)
    return render_template('modal.html', name=Name, genre=music )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080,debug=True)
