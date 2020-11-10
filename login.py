from .backend.models import Pengguna
from .backend.forms import FormMasuk

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user

bp = Blueprint('login', __name__)

@bp.route('/masuk/', methods=['GET', 'POST'])
def masuk():
    if current_user.is_authenticated:
        return redirect(url_for('dasbor.root'))
    form = FormMasuk()
    if form.validate_on_submit():
        pengguna = Pengguna.query.filter_by(surel=form.surel.data).first()
        if not pengguna:
            flash('Surel tidak ada dalam basisdata')
            return redirect(url_for('login.masuk'))
        if pengguna is None or not pengguna.cek_sandi(form.kata_sandi.data):
            flash('Kata sandi salah!')
            return redirect(url_for('login.masuk'))
        login_user(pengguna, remember=form.ingat_saya.data)
        return redirect(url_for('login.masuk'))
    return render_template('login/super.html', form=form)

@bp.route('/keluar/')
def keluar():
    logout_user()
    return redirect(url_for('login.masuk'))
