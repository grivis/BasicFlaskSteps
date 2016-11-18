from flask import Flask
from flask import url_for, render_template, request, redirect
import pickle

app = Flask(__name__)


@app.route('/')
def form():
    worddic = {}
    if request.args:
        worddic['name'] = request.args['name']
        worddic['lastname'] = request.args['lastname']
        worddic['birth'] = request.args['birth']
        worddic['phone'] = request.args['phone']
        worddic['email'] = request.args['email']
        worddic['country'] = request.args['country']
        worddic['city'] = request.args['city']
        worddic['Sex'] = request.args['Sex']
        worddic['food'] = request.args['food']
        worddic['comment'] = request.args["comment"]
        worddic['num'] = request.args["num"]
        f = open('questions.dic', 'wb')
        pickle.dump(worddic, f)
        f.close()
        return render_template('aform.html', name=worddic['name'], birth=worddic['birth'])
    return render_template('qform.html')


if __name__ == '__main__':
    app.run(debug=True)