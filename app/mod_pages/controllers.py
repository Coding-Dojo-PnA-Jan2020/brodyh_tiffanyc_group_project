from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

mod_pages = Blueprint('pages', __name__, url_prefix = '/')

@mod_pages.route('')
def welcome():
    return render_template('pages/index.html')

@mod_pages.route('/menu')
def render_main_menu():
    return render_template('pages/menu.html')