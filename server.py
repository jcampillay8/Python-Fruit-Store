from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    num_apple = request.form['apple']
    num_blackberry = request.form['blackberry']
    num_raspberry = request.form['raspberry']
    num_strawberry = request.form['strawberry']
    name = request.form['first_name']
    lastname = request.form['last_name']
    studentid = request.form['student_id']
    count= int(num_apple)+int(num_blackberry)+int(num_raspberry)+int(num_strawberry)
    return render_template("checkout.html", num_apple=num_apple,num_blackberry=num_blackberry,num_raspberry=num_raspberry,num_strawberry=num_strawberry, name=name, lastname= lastname, studentid = studentid, count=count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    