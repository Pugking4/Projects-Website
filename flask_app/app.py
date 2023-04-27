from flask import Flask, render_template, request, send_from_directory, session, send_file, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_apscheduler import APScheduler
import os
import datetime
import json

from backend_python.ratingcal import calculate_rating
#from backend_python.nested_record_scrape import *

#Get .env variable
segaid = 'pugking4'
password = 'Cocothe4th00'


#Init variables

app = Flask(__name__)
scheduler = APScheduler()
auth = HTTPBasicAuth()

app.secret_key = 'maimai'


users = {
    "admin": "rats",
    "guest": "temp",
}

#Config
scheduler.api_enabled = True


#Variables
#data = []
#with open(r'C:\Users\joshu\Documents\GitHub\Projects-Website\flask_app\output_gen.txt', 'r', encoding='utf-8') as f:
#    data = f.read()
    

#Init modules
scheduler.init_app(app)
scheduler.start()

#Functions
def records_search_data(date):
    data = []
    with open(fr'records\{date}.json', 'r') as f:
        data = json.load(f)
    return data

def auto_record_scrape():
    scrape_records(segaid, password)


#Auth routes
@auth.verify_password
def check_auth(username, password):
    if username in users and users[username] == password:
        return username
    else:
        print("Incorrect username or password.")
        return False

#Webpage routes
@app.route('/')
def home():
    print("Received a request at /")
    return render_template('index.html')

#Serve static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/index')
def index():
    print("Received a request at /index")
    return render_template('index.html')

@app.route('/rating-calculator')
def ratingcal():
    print("Received a request at /ratingcal")
    return render_template('ratingcal.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    print("Received a POST request at /calculate")
    # Get the input values from the form

    if request.form['constant']:
        constant = float(request.form['constant'])
    else:
        constant = 0

    if request.form['achievement']:
        achievement = float(request.form['achievement'])
    else:
        achievement = 0

    if request.form['rating']:
        rating = request.form['rating']
    else:
        rating = 0
    
    print(f"Constant: {constant}")
    print(f"Achievement: {achievement}")
    print(f"Rating: {rating}")

    # Process the data here
    s_rating, splus_rating, ss_rating, ssplus_rating, sss_rating, sssplus_rating, custom_rating = calculate_rating(constant=constant, achievement=achievement, rating=rating)

    # Store the result in session variables
    session['constant'] = constant
    session['achievement'] = achievement
    session['rating'] = rating
    session['s_rating'] = s_rating
    session['splus_rating'] = splus_rating
    session['ss_rating'] = ss_rating
    session['ssplus_rating'] = ssplus_rating
    session['sss_rating'] = sss_rating
    session['sssplus_rating'] = sssplus_rating
    session['custom_rating'] = custom_rating

    # Return the result through POST method
    return render_template('ratingcal.html', constant=constant, achievement=achievement, rating=rating, s_rating=s_rating, splus_rating=splus_rating, ss_rating=ss_rating, ssplus_rating=ssplus_rating, sss_rating=sss_rating, sssplus_rating=sssplus_rating, custom_rating=custom_rating)

@app.route('/privacy-policy')
def privacy_policy():
    print("Received a request at /privacy-policy")
    return render_template('privacy-policy.html')

@app.route('/db-export')
def db_export():
    print("Received a request at /db-export")
    return render_template('db-export.html')

@app.route('/db-export/download')
def db_export_download():
    print("Received a request at /db-export/download")
    path = "/home/admin/Desktop/Projects-Website/flask_app/db/20230423db.sqlite3"
    return send_file(path, as_attachment=True)

@app.route('/mai-camera')
@auth.login_required
def mai_camera():
    print("Received a request at /mai-camera")
    username = auth.username()
    print(f"Username: {username}")

    image_dir = 'static/images/mai-camera'
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    return render_template('mai-camera.html', username=username, image_files=image_files)

#@app.route('/mai-camera/upload', methods=['POST'])

@app.route('/manual-scrape')
def manual_scrape():
    global data
    print("Received a request at /test")
    data = scrape_records(segaid, password)
    return render_template('index.html')

@app.route('/reload-records')
def reload_records():
    global data
    data = []
    print("Received a request at /reload-records")
    time = datetime.datetime.now().strftime("%Y-%m-%d")
    time = '2023-04-27'
    with open(fr'records\{time}.json', 'r') as f:
        data = json.load(f)
        #print(data)
    #for i in raw_data:
        #data.append(dict(i))
    return render_template('index.html')

@app.route('/view-records')
def view_records50():
    print("Received a request at /view-records50")
    reload_records()
    return render_template('view-records50.html', data=data)
    #if data:
    #    return render_template('view-records50.html', data=data)
    #else:
        #return render_template('view-records50_nodata.html', data=data)

@app.route('/view-records-search', methods=['POST'])
def view_records_search():
    print("Received a request at /view-records-search")

    form_date = request.form['date']

    print(f"Date: {form_date}")

    data = records_search_data(form_date)

    return data
    if data:
        return render_template('view-records50.html', data=data)
    else:
        return render_template('view-records50_nodata.html', data=data)

#@app.route('/view-records/<string:segaid>')

@app.route('/test', methods=['POST'])
def test():
    print("Received a POST request at /test")
    # Get the values for the "Time", "Title", and "Type" fields from the POST request
    time = request.form.get('time')
    title = request.form.get('title')
    type = request.form.get('type')

    # Do something with the data (e.g., save to a database)
    print(f"Time: {time}")
    print(f"Title: {title}")
    print(f"Type: {type}")
    # Return the data as a JSON response
    return jsonify({'time': time, 'title': title, 'type': type})

@app.route('/display-test', methods=['GET'])
def display_test():
    # Get the data from the query string
    time = request.args.get('time')
    title = request.args.get('title')
    type = request.args.get('type')

    # Store the result in session variables
    #session['time'] = time
    #session['title'] = title
    #session['type'] = type

    print('time:', time)
    print('title:', title)
    print('type:', type)

    # Render the template with the data
    return render_template('test.html', time=time, title=title, type=type)



#Scheduler routes
#@scheduler.task('interval', id='do_job_1', seconds=300, misfire_grace_time=900)
#def job1():
#    print('Job 1 executed')
'''
@scheduler.task('interval', id='scrape_records_job', minutes=90, misfire_grace_time=900)
def scrape_records_job():
    #time = datetime.datetime.now().strftime("%H:%M:%S")
    print('Auto record scraping started')
    scrape_records(segaid, password)
    print('Auto record scraping executed')
    #print(f'Auto record scraping took {datetime.datetime.now().strftime("%H:%M:%S") - time}')
'''
#Misc routes
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
