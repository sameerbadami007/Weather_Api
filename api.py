from flask import Flask,render_template,request
from aa import we
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
	if request.method=='POST':
		city=request.form['city']
		units=request.form['units']
		info=we(city,units)
		return render_template('home.html',tt='Home Page',info=info)
	return render_template('home.html',tt='Home Page')



app.run(debug=True)
