from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():
	return render_template('index.html', page_title='Home')

@app.route('/about.html')
def about():
	return render_template('about.html', page_title='About')

@app.route('/portfolio.html')
def portfolio():
	return render_template('portfolio.html', page_title='Portfolio')

@app.route('/contact.html')
def contact():
	return render_template('contact.html', page_title='Contact')

if __name__ == '__main__':
		app.run(host='127.0.0.1', port=8080)
