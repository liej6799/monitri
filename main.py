from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms.validators import InputRequired
from wtforms import TextAreaField
from maeapi.maeapi import MAE  # noqa: E402
from models.header_auth_model import HeaderAuthModel
from peewee import *

app = Flask(__name__)

@app.route("/")
def index():

    is_api_configured = False
    is_api_valid = False
    
    try:
        key = HeaderAuthModel.get(HeaderAuthModel.status == True).key
        try:
            MAE(key)
            is_api_valid = True
        except:
            is_api_valid = False
        is_api_configured = True
    except DoesNotExist:
        is_api_configured = False


    return render_template('index.html', is_api_configured = is_api_configured,
    is_api_valid = is_api_valid)


# More powerful approach using WTForms
class HeaderAuthForm(Form):
    headers_auth = TextAreaField('Headers Auth: ', [InputRequired()])

@app.route('/header_auth', methods=['GET', 'POST'])
def header_auth():
    error = ""
    form = HeaderAuthForm(request.form)

    if request.method == 'POST':
        headers_auth = form.headers_auth.data
        try:
            mae = MAE(headers_auth)
            # insert into sqlite
            try:
                auth = HeaderAuthModel.create(key=headers_auth)
                auth.save()
            except IntegrityError:
                error = "Cannot store multiple similar headers auth."
                return redirect("/")
        except:
            error = "Wrong Headers Auth provided."
    return render_template('header_auth.html', form=form, message=error)
