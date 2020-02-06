from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():
	return render_template('index.html', page_title='Starogen')


@app.route('/about.html')
def about():
	return render_template('about.html', page_title='About')


@app.route('/contact.html')
def contact():
	return render_template('contact.html', page_title='Contact')


@app.route('/download.html')
def download():
	return render_template('download.html', page_title='Download')


@app.route('/wiki.html')
def wiki():
	return render_template('wiki.html', page_title='Wiki')


if __name__ == '__main__':
		app.run(host='127.0.0.1', port=8080)
