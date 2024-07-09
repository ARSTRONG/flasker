from flask import Flask, render_template

#Create a Flask Instance
app = Flask(__name__)

#Create new route decorator
@app.route('/')

################
#FILTERS!!!!

# safe
# capitalize
# lower 
# upper
# title
# trim
# striptags

#################

def index():
	# return "<h1>Helllooooo!!!</h1>"
	first_name = 'Arsennn'
	stuff = 'this is <strong>bold</strong> tekst'

	favorite_pizza=['Peperoni', '4Cheese', 'Margarita', 41]
	return render_template('index.html', 
		firstName=first_name, 
		stuff=stuff,
		favorite_pizza=favorite_pizza
		)

@app.route('/about')

def About():
	return "something about mysel"

@app.route('/user/<name>')

def User(name):
	#return 'Hello, {}!'.format(name)
	return render_template('user.html', name=name)

#Create a custom Error Page

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

@app.errorhandler(505)
def page_not_found(e):
	return render_template('505.html')




if __name__ == '__main__':
    app.run(debug=True) > helloW.py