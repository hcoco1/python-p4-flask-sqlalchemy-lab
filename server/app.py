# We're importing necessary modules and classes from the Flask framework and our models.
from flask import Flask, make_response
from models import db, Zookeeper, Enclosure, Animal

# Create an instance of the Flask application.
app = Flask(__name__)

# Configure the database URI for our SQLite database and turn off the SQLALCHEMY_TRACK_MODIFICATIONS setting
# (this is mainly to suppress a warning and to reduce overhead of tracking modifications which we don't need in this case).
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize our database with the app.
db.init_app(app)

@app.route('/')
def home():
    # Basic route to show a welcome message when accessing the root URL.
    response = make_response('<h1>Zoo app</h1>', 200)
    return response

@app.route('/animal/<int:id>')
def animal_by_id(id):
    # Get the animal with the given ID from the database.
    # If it doesn't exist, return None.
    animal = Animal.query.filter(Animal.id == id).first()

    # If the animal doesn't exist, we return a 404 error response.
    if not animal:
        return make_response('<h1>404 animal not found</h1>', 404)

    # If the animal exists, construct a response displaying its details.
    response_body = f'''
        <ul>Name: {animal.name}</ul>
        <ul>Species: {animal.species}</ul>
        <ul>Zookeeper: {animal.zookeeper.name}</ul>
        <ul>Enclosure: {animal.enclosure.environment}</ul>
    '''

    return make_response(response_body, 200)

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    # Similar to the animal route above, but for zookeepers.
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()

    if not zookeeper:
        return make_response('<h1>404 zookeeper not found</h1>', 404)

    # Construct a list of animals the zookeeper takes care of.
    animals_ul = ''.join([f'<ul>Animal: {animal.name} ({animal.species})</ul>' for animal in zookeeper.animals])

    response_body = f'''
        <ul>Name: {zookeeper.name}</ul>
        <ul>Birthday: {zookeeper.birthday}</ul>
        {animals_ul}
    '''

    return make_response(response_body, 200)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    # This route is for enclosures. 
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()

    if not enclosure:
        return make_response('<h1>404 enclosure not found</h1>', 404)

    # Construct a list of animals in the enclosure.
    animals_ul = ''.join([f'<ul>Animal: {animal.name} ({animal.species})</ul>' for animal in enclosure.animals])

    response_body = f'''
        <ul>Environment: {enclosure.environment}</ul>
        <ul>Open to Visitors: {'Yes' if enclosure.open_to_visitors else 'No'}</ul>
        {animals_ul}
    '''

    return make_response(response_body, 200)

# This checks if the script is being run directly (not imported elsewhere).
# If it is, it starts the Flask development server.
if __name__ == '__main__':
    app.run(port=5555, debug=True)



    """
    

# Import necessary libraries/modules
from flask import Flask, render_template_string
from flask_migrate import Migrate
from models import db, Zookeeper, Enclosure, Animal

# Instantiate the Flask application
app = Flask(__name__)

# Configure the SQLite database URL for the application and disable tracking modifications
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up Flask-Migrate for handling database migrations
migrate = Migrate(app, db)

# Initialize the SQLAlchemy extension with our Flask application
db.init_app(app)

@app.route('/')
def home():
    # Define the home route to return a simple message
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    # Fetch an animal record from the database by its ID or return a 404 if not found
    animal = Animal.query.get_or_404(id)
    # Return a formatted string containing the animal's details inside <ul> tags
    return f'''
        <ul>Name: {animal.name}</ul>
        <ul>Species: {animal.species}</ul>
        <ul>Zookeeper: {animal.zookeeper.name}</ul>
        <ul>Enclosure: {animal.enclosure.environment}</ul>
    '''

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    # Fetch a zookeeper record from the database by its ID or return a 404 if not found
    zookeeper = Zookeeper.query.get_or_404(id)
    # Create a list of animals associated with the zookeeper, formatted inside <ul> tags
    animals_ul = ''.join([f'<ul>Animal: {animal.name} ({animal.species})</ul>' for animal in zookeeper.animals])
    # Return a formatted string containing the zookeeper's details and the associated animals inside <ul> tags
    return f'''
        <ul>Name: {zookeeper.name}</ul>
        <ul>Birthday: {zookeeper.birthday}</ul>
        {animals_ul}
    '''

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    # Fetch an enclosure record from the database by its ID or return a 404 if not found
    enclosure = Enclosure.query.get_or_404(id)
    # Create a list of animals associated with the enclosure, formatted inside <ul> tags
    animals_ul = ''.join([f'<ul>Animal: {animal.name} ({animal.species})</ul>' for animal in enclosure.animals])
    # Return a formatted string containing the enclosure's details and the associated animals inside <ul> tags
    return f'''
        <ul>Environment: {enclosure.environment}</ul>
        <ul>Open to Visitors: {'Yes' if enclosure.open_to_visitors else 'No'}</ul>
        {animals_ul}
    '''

# The conditional below checks if this script is being run directly (not imported as a module)
# If so, it runs the Flask application on port 5555 with debugging enabled
if __name__ == '__main__':
    app.run(port=5555, debug=True)
    """



