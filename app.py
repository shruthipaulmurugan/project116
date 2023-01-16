# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "shruthi" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/family_tree/templates/father.html")
def father():
    name = "father"
    age = "51"
    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/family_tree/templates/mother.html")
def mother():
    name = "mother"
    age = "51"
    return render_template('index.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/family_tree/templates/friend.html")
def friend():
    name = "friend"
    age = "16"
    return render_template('index.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
