from flask import Flask , render_template, request, url_for
import csv

app = Flask(__name__)

@app.route("/index.html")
def my_home():
    return render_template("index.html")

@app.route("/generic.html")
def first():
    return render_template("generic.html")

@app.route("/elements.html")
def second():
    return render_template("elements.html")

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        file = f"\n{name}, {email}, {message}\n"
        database.write(file)

def write_to_csv(data):
    with open("database.csv", mode='a', newline='') as database2:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
      try:  
        data = request.form.to_dict()
        write_to_csv(data)
        return "Thank you for your submission!"
      except:
        return "There was an error in your submission. Please try again."
    else:
        return "Something went wrong. Please try again."
    
url_rules = [
    ("/index.html", my_home),
    ("/generic.html", first),
    ("/elements.html", second),
    ("/submit_form", submit_form)
]

app.run(debug=True)

