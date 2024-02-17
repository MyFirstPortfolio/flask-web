"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, request,flash
from Company_Website import app
from Company_Website import forms 

from flask_mail import Mail, Message

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'alphanerds.contact@gmail.com'
app.config["MAIL_PASSWORD"] = 'xuvqgsdayjalnzuh'
mail.init_app(app)

app.secret_key = 'jhersfdc$j5456s%asd'

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        # 'index - Copy.html',
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route("/work")
def work():
    return render_template(
        'work.html',
        title = "Work",
        )


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = forms.ContactForm()
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='alphanerds.contact@gmail.com', recipients=['alphanerds.contact@gmail.com'])
      msg.body = """ 
From: %s <%s> 
%s 
""" % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template('contact.html', success=True)
  elif request.method == 'GET':
    return render_template('contact.html', form=form)


