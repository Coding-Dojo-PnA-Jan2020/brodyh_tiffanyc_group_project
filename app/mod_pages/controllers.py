from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

mod_pages = Blueprint('pages', __name__, url_prefix = '/')

@mod_pages.route('')
def root():
    return redirect('/menu')

@mod_pages.route('/about-us')
def about():
    return render_template('pages/about-us.html')

@mod_pages.route('/contact-us')
def contact():
    return render_template('pages/contact-us.html')

@mod_pages.route('/my-account')
def render_account_settings():
    return redirect('/users/me')


# DEVELOPMENT ROUTES: REMOVE ROUTES BELOW FOR PRODUCTION
@mod_pages.route('/menu-for-development')
def menu_for_development():
    return render_template('pages/menu-for-development.html')
