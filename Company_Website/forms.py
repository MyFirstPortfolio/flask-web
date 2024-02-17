from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, Email

nameError = "Please Enter a Name"
emailError = "Please Enter a valid Email"
subjecterror = "Please Enter a Subject"
texterror = "Please Enter a body for the email"

class ContactForm(FlaskForm):
  name = StringField("Name", validators=[DataRequired(message=nameError)],render_kw={"placeholder": "Enter your Name"})
  email = StringField("Email", validators=[DataRequired(message=emailError), Email()],render_kw={"placeholder": "Enter your Email"})
  subject = StringField("Subject", validators=[DataRequired(message=subjecterror)],render_kw={"placeholder": "Enter your Subject"})
  message = TextAreaField("Message", validators=[DataRequired(message=texterror)],render_kw={"placeholder": "Enter your Concern Here"})
  # message = TextAreaField("Message", validators=[DataRequired(message=texterror)],render_kw={"placeholder": "Enter your Concern Here",'style':'width 700px'})
  submit = SubmitField("Send") 


from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
  
class ContactForm2(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')