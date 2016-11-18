from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def form():
    if request.args:
        name = request.args['name']
        lastname = request.args['lastname']
        birth = request.args['birth']
        phone = request.args['phone']
        email = request.args['email']
        country = request.args['country']
        city = request.args['city']
        sex = request.args['Sex']
        food = request.args['food']
        comment = request.args["comment"]
        num = request.args["num"]
        print(name, birth, phone, country, city, sex, food, num, comment)
        return render_template('aform.html', name=name, birth=birth)
    return render_template('qform.html')


if __name__ == '__main__':
    app.run(debug=True)




