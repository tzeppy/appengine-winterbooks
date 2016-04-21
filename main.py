"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
import flask
app = flask.Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def home():
    return flask.render_template('home.html')


@app.route('/books')
def books():
    return flask.render_template('books.html')


@app.route('/about')
def about():
    return flask.render_template('about.html')


@app.route('/blogs')
def blogs():
    return flask.render_template('blogs.html')

@app.route('/ava')
def ava():
    return flask.render_template('ava.html')

@app.route('/support_authors')
def support_authors():
	return flask.render_template('support_authors.html')


@app.route('/fund_ava.php')
def fund_ava():
    return flask.render_template('fund_ava.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
