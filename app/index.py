from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def resume():
    return render_template('resume.html')


@app.route('/feedback', methods=["POST", "GET"])
def feedback():
    if request.method == "POST":
        name = request.form['name']
        mail = request.form['mail']
        comment = request.form['comment']
        message = name + " " + mail + " " + comment
        return render_template('resume.html', msg=message)


if __name__ == '__main__':
    app.run(debug=False)
