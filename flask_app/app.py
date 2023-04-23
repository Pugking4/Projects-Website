from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from ratingcal import calculate_rating

app = Flask(__name__)

app.config['STATIC_URL'] = '/flask_app/static/'

@app.route('/')
def home():
    print("Received a request at /")
    return render_template('index.html')

@app.route('/index')
def index():
    print("Received a request at /index")
    return render_template('index.html')

@app.route('/ratingcal')
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


    # Redirect the user to a new page with a success message
    return redirect(url_for('result', constant=constant, achievement=achievement, rating=rating, s_rating=s_rating, splus_rating=splus_rating, ss_rating=ss_rating, ssplus_rating=ssplus_rating, sss_rating=sss_rating, sssplus_rating=sssplus_rating, custom_rating=custom_rating))

@app.route('/result')
def result():
    print("Received a request at /result")
    constant = float(request.args.get('constant'))
    achievement = request.args.get('achievement')
    rating = request.args.get('rating')

    s_rating = request.args.get('s_rating')
    splus_rating = request.args.get('splus_rating')
    ss_rating = request.args.get('ss_rating')
    ssplus_rating = request.args.get('ssplus_rating')
    sss_rating = request.args.get('sss_rating')
    sssplus_rating = request.args.get('sssplus_rating')
    custom_rating = request.args.get('custom_rating')

    header_text = "Calculation complete!"
    #Make it insert data rather than use template or use templates exclusively

    return render_template('ratingcal.html', constant=constant, achievement=achievement, rating=rating, s_rating=s_rating, splus_rating=splus_rating, ss_rating=ss_rating, ssplus_rating=ssplus_rating, sss_rating=sss_rating, sssplus_rating=sssplus_rating, custom_rating=custom_rating, header_text=header_text)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
