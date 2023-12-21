import flask
from flask import render_template, request, redirect, url_for
from dbclass import executeUpdate,fetchAll

app=flask.Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/display")
def display():
    sql="select * from employee3"
    data = fetchAll(sql)
    return render_template("display.html", data=data)

@app.route("/newemployee", methods=["post", "Get"])
def newemployee():
    fullname=request.form['fullname']
    age= request.form['age']
    sql = "Insert into employee3(fullname,age) " \
          "values( '%s', '%s')" % \
          (fullname,age)
    executeUpdate(sql)
    return redirect(url_for("display"))

@app.route("/delete")
def delete():
    sql="select * from employee3"
    data=fetchAll(sql)
    return render_template("delete.html" ,data=data)

@app.route("/deletepage" )
def deletepage():
    args = request.args
    rno = args['rno']
    print("rno : ",rno)
    sql = "delete from employee3 where rno = %s"%(rno)
    executeUpdate(sql)
    return redirect(url_for("delete"))

@app.route("/update")
def update():
    sql="select * from employee3"
    data=fetchAll(sql)
    return render_template("/update.html" ,data=data)

@app.route("/updatepage",methods=["POST","GET"])
def updatepage():
    args=request.args
    rno=request.args['rno']
    sql="select * from employee3 where rno="+str(rno)
    data=fetchAll(sql)[0]
    print(data)
    return render_template("updatepage.html",data=data)

@app.route("/update1" ,methods=["POST" , "GET"])
def update1():
    fullname=request.form['fullname']
    age=request.form['age']
    rno=request.form['rno']
    sql="update employee3 set fullname= '%s',age= '%s'where rno= '%s' "% (fullname,age,rno)
    executeUpdate(sql)
    return redirect(url_for("update"))

if __name__=="__main__":
    app.run(debug=True)
