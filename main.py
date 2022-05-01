from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# import pandas as pd
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
db = SQLAlchemy(app)
app.secret_key = 'my precious'

# connect flask sqlalchemy to app
db_user = "root"
db_password = ""
db_host = "localhost"
db_name = "spam_detector"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + db_user + ':' + db_password + '@' + db_host + '/' + db_name


class Spam_Detector(db.Model):
    d_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spam_or_ham = db.Column(db.String(11), unique=False, nullable=False)
    data = db.Column(db.String(1000), unique=False, nullable=False)


db.create_all()


# f = pd.read_csv("data/data.csv" ,encoding='latin1')
#
# for index in f.index:
#     spam_or_ham = f["spam_or_ham"][index]
#     data = f["data"][index]
#
#     d = Spam_Detector(spam_or_ham = spam_or_ham , data=data)
#     db.session.add(d)
# db.session.commit()

@app.route("/", methods=["GET", 'POST'])
def home():
    return render_template("home.html")


@app.route("/result", methods=['POST'])
def homer():
    user_input = request.form.get("user_input")
    search = "%{}%".format(user_input)
    fetched_data = Spam_Detector.query.filter(Spam_Detector.data.like(search)).all()
    spam_count = 0
    ham_count = 0
    for data in fetched_data:
        if data.spam_or_ham == "spam":
            spam_count += 1
        else:
            ham_count += 1

    numerator = 0
    denominator = 0
    if spam_count > ham_count:
        numerator = ham_count
        denominator = spam_count
    else:
        numerator = spam_count
        denominator = ham_count

    try:
        spam_per = abs(((numerator / denominator) * 100))
    except:
        spam_per = 0

    if spam_count > ham_count:
        spam_per = abs(spam_per - 100)
    spam_per = round(spam_per, 2)
    ham_per = round(abs(spam_per - 100), 2)
    return render_template("result.html", spam_count=spam_count, ham_count=ham_count, spam_per=spam_per,
                           ham_per=ham_per)


@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("about.html")


app.run(debug=True, host="0.0.0.0")
