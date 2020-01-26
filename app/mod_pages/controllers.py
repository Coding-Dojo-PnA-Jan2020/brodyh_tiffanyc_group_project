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
    return render_template('pages/menu-appetizers.html')

@mod_pages.route('/menu/soups-salads')
def render_menu_soups_salads():
    return render_template('pages/menu-soups-salads.html')

@mod_pages.route('/menu/signature-dishes')
def render_menu_main_dishes():
    return render_template('pages/menu-main-dishes.html')

@mod_pages.route('/menu/desserts')
def render_menu_desserts():
    return render_template('pages/menu-desserts.html')

@mod_pages.route('/menu/drinks')
def render_menu_drinks():
    return render_template('pages/menu-drinks.html')

@mod_pages.route('/my-account')
def render_account_settings():
    return render_template('pages/my-account.html')