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


def verify_pw(pw):  # guideline: https://owasp.org/www-project-proactive-controls/v3/en/c6-digital-identity
    with open('10-million-password-list-top-1000.txt') as f:
        if pw in f.read():
            print("bad password")
            return False
    if len(pw) < 10:  # no MFA so minimum 10
        print("short password")
        return False
    else:
        print(pw, "OK")
        return True


if __name__ == "__main__":
    app.run(debug=True)
