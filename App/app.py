from flask import Flask, request, render_template
from process import keyword_extract



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/output', methods=["GET", "POST"])
def output():
    if request.method == "POST":

        text = request.form["text"]
        if len(text) == 0:
            return render_template('index.html', keywords=['Không có nội dung','1'])
        else:
            return render_template("index.html", keywords=keyword_extract(text))
	

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8088)