from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

mod_pages = Blueprint('pages', __name__, url_prefix = '/')

@mod_pages.route('')
def welcome():
    return render_template('pages/index.html')

@mod_pages.route('/menu')
def render_main_menu():
    return render_template('pages/menu.html')

@mod_pages.route('/menu/appetizers')
def render_menu_appetizers():
    return render_template('pages/menu_appetizers.html')

@mod_pages.route('/menu/soups_salads')
def render_menu_soups_salads():
    return render_template('pages/menu_soups_salads.html')

@mod_pages.route('/menu/signature_dishes')
def render_menu_main_dishes():
    return render_template('pages/menu_main_dishes.html')

@mod_pages.route('/menu/desserts')
def render_menu_desserts():
    return render_template('pages/menu_desserts.html')

@mod_pages.route('/menu/drinks')
def render_menu_drinks():
    return render_template('pages/menu_drinks.html')

@mod_pages.route('/account_settings')
def render_account_settings():
    return render_template('pages/account_settings.html')