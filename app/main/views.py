from flask import render_template,request,redirect,url_for,abort
from ..models import Comment,User,Pitch
from . import main
from .forms import CommentForm, PitchForm,UpdateProfile
from flask_login import login_required, current_user
from .. import db,photos
import markdown2

def save_pitch(pitch):
    Pitch.save_pitch(pitch)