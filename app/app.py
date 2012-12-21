from flask.app import Flask
from flask.globals import request
from flask.templating import render_template
from flask.ext.babel import Babel, gettext
from datetime import date, datetime
import sys, os

def static(filename):
	"""Provides the 'static' function that also appends the file's timestamp to the URL, usable in a template."""
	timestamp = os.path.getmtime(os.path.join(app.static_folder, filename))
	return "%s/%s?%s" % (app.static_url_path, filename, timestamp)

app = Flask(__name__)
app.config.from_object("settings_dev")
app.static_url_path = app.config["STATIC_URL"]
app.jinja_env.globals.update(static=static)

babel = Babel(app)

greeting_words = ["Monday Monday, it's not always that gloomy, isn't it?",
				"Happy Tuesday, is everything on track?",
				"It's Wednesday, go go go!",
				"It's Thursday, why not have a good dinner tonight?",
				"Happy Friday, the weekend is coming.",
				"Wow Saturday, how would you like to celebrate it?",
				"It's Sunday, stay tuned for the upcoming great week. Are you ready for it?"]

@app.route('/')
def main():
	greeting = gettext(greeting_words[date.today().weekday()])
	return render_template("index.html", greeting=greeting)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

if __name__ == "__main__":
	app.run();