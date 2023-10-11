import csv
from flask import Flask, redirect, render_template, request, send_from_directory, url_for
import os

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def index():
	# print(url_for('static', filename='favicon.ico'))
	return render_template("index.html")

@app.route("/work/<int:work_num>")
def work(work_num):
	return render_template("work.html")

@app.route("/<string:page_name>")
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email, subject, message = data['email'], data['subject'], data['message']
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as csvfile:
		email, subject, message = data['email'], data['subject'], data['message']
		csv_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		# csv_writer.writeheader()
		csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
			# {'email': 'b@g.com', 'subject': 'test', 'message': 'Hello'}
		write_to_csv(data)
		return render_template('thankyou.html', email=data['email'])
	else:
		return 'something went wrong! Try again!'

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static', 'assets'),
		'favicon.ico',mimetype='image/vnd.microsoft.icon')


# @app.route("/about.html")
# def about():
# 	return render_template("about.html")

# @app.route("/contact.html")
# def contact():
# 	return render_template("contact.html")
