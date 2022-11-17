from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pw = request.form['title']
        if verify_pw(pw):
            return '<h1>' + request.form['title'] + '</h1><a href="/">Logout</a>'
        else:
            return '<form method="post"><input type="password" name="title" placeholder="Password"></input><button type="submit">Login</button>'

    return '<form method="post"><input type="password" name="title" placeholder="Password"></input><button type="submit">Login</button>'


def verify_pw(pw):

    if len(pw) > 7:
        return True
    else:
        return False


if __name__ == "__main__":
    app.run(debug=True)
