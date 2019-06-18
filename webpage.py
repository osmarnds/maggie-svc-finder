from models.models import Services_List
from models.models import Service
from models.models import Details
from models.models import Logs
import labio
from flask import Flask, render_template

app = Flask(__name__)
labio.db.init()

lista = Service.query.all()

@app.route('/')
@app.route('/index')
def index():
    items = [item.name for item in lista]
    return render_template('index.html', title='Home', items=items)
    