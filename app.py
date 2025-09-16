from flask import Flask, render_template, request
import random
# pip install flask
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():

    return render_template("index.html")
    #return "<p>Hellooooooooo World!</p>"


@app.route("/8-Ball", methods = ["POST"])
def Ball():
    r=random.choice(["yes","maybe","no"])
    if r == "yes":
        ra=random.choice(["As I see it, yes","Most likely","Outlook good","Yes"])
        return render_template("index.html",rez=ra)
    elif r == "maybe":
        ra=random.choice(["Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict now"])
        return render_template("index.html",rez=ra)
    elif r == "no":
        ra=random.choice(["Don't count on it","My reply is no","Outlook not so good","Very doubtful"])
        return render_template("index.html",rez=ra)

app.run(debug=True)

"""    tmp = dict(request.form)
    ime1 = tmp.get("ime1")
    ime2 = tmp.get("ime2")
    r = f"{ime1} + {ime2} = {random.randint(0,100)} %"
    return render_template("index.html", rezultat = r)
    #return f"{ime1} + {ime2} = {random.randint(0,100)} %" """

