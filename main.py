from flask import Flask,render_template,jsonify

app=Flask(__name__)


JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru',
        'Salary':'rs. 10,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi',
        'Salary':'rs. 15,00,000'
    },
    {
        'id':3,
        'title':'Frontend developer',
        'location':'Remote',
        'Salary':'rs. 12,00,000'
    },
    {
        'id':4,
        'title':'Backend developer',
        'location':'Gujarat',
        'Salary':'rs. 16,00,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS,company_name='linkedin')

# if __name__=="__main__":
#     print("I am inside the main now")

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)