from flask import Flask, render_template, request

app = Flask(__name__)


from get_webdata import get_data
web_data=get_data()

@app.route("/")
def index():
    return render_template ("index1.html")

#render_template("index.html")
@app.route('/hello/<name>', methods=["GET","POST"])
def user(name):
#    return '<p> He22222 %s</p>'  %name
    # Query for currency exchange rate
#    name1=request.form.get('name')
    name2=name
    return render_template("hello_name.html", name=name2)

@app.route('/hellowithoutname', methods=["GET", "POST"])
def noname():
    name='you did not enter your name1'
    return render_template("hello_name2.html", name=name)

@app.route('/hellowithname', methods=["POST"])
def hello2():
    name1=request.form.get('name1234')
    return render_template("hello_name2.html", name=name1)

@app.route('/dataretrieved', methods=["POST"])
def get_data2():
    name12=web_data
    #    name12=request.form.get('data_time')
    return render_template("Data_retrieved.html", data_ret=name12)



@app.route('/hello', methods=["GET","POST"])
def hello():
    return '<p> NO name He22222222</p>'
    # Query for currency exchange rate
#    name1=request.form.get('name')
#    return render_template("hello.html", name=name1)


if __name__== '__main__':
     app.run()
