import os
import FlaskForm

app = Flask(__name__)
# Configure Secret Key
app.config['SECRET_KEY'] = os.

# Load model et. al

# Create form
class ClassifierForm(FlaskForm):
    radius = TextField('Tumour Radius')
    texture = TextField('Tumour Texture')
    radius = TextField('Tumour Radius')
    radius = TextField('Tumour Radius')
    radius = TextField('Tumour Radius')
    # might want to rename 'Run Prediction'
    submit = SubmitField('Run Prediction')


@app.route('/', methods = ['GET', 'POST'])
def index():
    # Create instance of form
    form = ClassifierForm()
    # If the form is valid on submission
    if form.validate_on_submit():
        # Grab data from form input fields
        session['radius'] = form.radius
        session['texture'] = form.texture

if __name__ == ‘__main__’:
    app.run(debug=True)
