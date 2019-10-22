from . import auth
from flask import render_template,redirect,url_for, flash,request
from ..models import User
from flask_login import login_user,logout_user,login_required
from .forms import LoginForm,RegistrationForm
from .. import db
from ..email import mail_message