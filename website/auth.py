from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', boolean=True)


@auth.route('/logout')
def logout():
    return '<p>Logout</p>'


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    return render_template('sign_up.html')

    if len(email) < 4:
        flash('Email most be grater than 3 characters', category='error')
    elif len(firstName) < 2:
        flash('Firstname most be grater than 1 characters', category='error')
    elif password1 != password2:
        flash("Passwords don't match", category='error')
    elif len(password1) < 7:
        flash('Password must be at least 7 characters.', category='error')
    else:
        flash('Account created!', category='success')

    return render_template('sign_up.html')
