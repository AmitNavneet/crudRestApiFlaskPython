from flask import Flask, request
from flask import render_template,jsonify

app=Flask(__name__)

studentsData=[
    {"roll":1,"name":"amit","score":9.50},
    {"roll":2,"name":"dhoom","score":5.50},
    {"roll":3,"name":"dev","score":1.50}
]

@app.route('/')
def index():
    return render_template("index.html")

@app.get("/students")
def get_students():
    return jsonify(studentsData)

@app.route("/postStudent",methods=["POST"])
def post_student():
    roll=int(request.form['studRoll'])
    name=request.form["studName"]
    score=float(request.form["studScore"])
    new_student={'roll':roll,'score':score,"name":name}
    studentsData.append(new_student)
    return jsonify(studentsData)


@app.route("/updateStudent", methods=["POST"])
def update_student():
    roll=int( request.form['studRoll'])
    name=request.form['studName']
    score=float(request.form['studScore'])

    index=0
    for student in studentsData:

        if student['roll']==roll:
            student['name']=name
            student['score']=score
            studentsData[index]=student
            return studentsData
        index=index+1

    return {"error":f"Roll Number:{roll} not found"}

@app.route("/deleteStudent", methods=["POST"])
def delete_student():
    frmRoll=int(request.form['studRoll'])

    index=0
    for student in studentsData:
        if student['roll']==frmRoll:
            del studentsData[index]
            return studentsData
        index=index+1
    return {"error":f"Roll number {frmRoll} not found"}

    


if __name__=="__main__":
    app.run(debug=True)