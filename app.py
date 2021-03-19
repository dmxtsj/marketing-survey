from flask import Flask, render_template, request, redirect
import pymysql

app=Flask(__name__)

#connect to aws rds account
db = pymysql.connect(host="digitalmarketing-survey.cy158xucdakx.ap-southeast-1.rds.amazonaws.com",user="tsjia",password="SSiijjiiaa97!!")
#connect to selected RDS SQL database, which is marketing survey
db.select_db("Marketing_Survey")
#everytime you use db after line 9, you will be selecting marketing survey database everytime alr
cursor = db.cursor()
cursor.execute("select version()")

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/submitted_page")
def submit_page():
    return render_template("submittedpage.html")

@app.route("/submit_form", methods=["GET","POST"])
def submit_form():
    if request.method == "POST":
        marketing_tools = request.form.get("default")
        gender = request.form.get("gender")
        age = request.form.get("agefield")
        email = request.form.get("emailfield")
        textfield = request.form.get("textfield")

        if marketing_tools == "others":
            marketing_tools = request.form.get("textfield")
        
        # previous test table name is test_survey
        sql="INSERT INTO survey_results (gender, age, marketing_tool, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (gender, age, marketing_tools, email))
        db.commit()

        return redirect("/submitted_page")
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)