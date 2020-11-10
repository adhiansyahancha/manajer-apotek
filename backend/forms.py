from flask_wtf import FlaskForm
from wtforms.validators import *
from wtforms.fields.html5 import *
from wtforms import *

from .models import DataMasterObat

def indeks_semua_obat():
    data = [(None, None)]
    
    for itr in DataMasterObat.query.all():
        data += [(itr.kode, itr.kode)]

    return data

class FormMasuk(FlaskForm):
    nama = StringField('Nama ', validators=[DataRequired(), Email()])
    kata_sandi = PasswordField('Kata sandi ', validators=[DataRequired()])
    ingat_saya = BooleanField('Ingat saya')
    submit = SubmitField('Masuk')

class FormDataMasterObat(FlaskForm):
    batch = StringField('Nomor batch', validators=[DataRequired()])
    kode = StringField('Kode', validators=[DataRequired(), \
        Regexp('[A-Z]{3,}(-[A-Z0-9]{1,})?(-[A-Z0-9]{1,})?(-[0-9]{1,''})?', flags=0, message="Masukkan sesuai aturan nama kode")])
    kadaluarsa = DateField('Kadaluarsa', validators=[DataRequired()])
    keterangan = StringField('Keterangan', default=None)
    masuk = IntegerField('Masuk', validators=[DataRequired()])
    keluar = IntegerField('Keluar', validators=[DataRequired()])
    sisa = IntegerField('Sisa', validators=[DataRequired()])
    pencatat = StringField('Pencatat')
    submit = SubmitField('Catat')

class FormPenjualanObat(FlaskForm):
    obat_terjual = SelectField('Pilih obat', choices=indeks_semua_obat())
    harga = IntegerField('Harga', validators=[DataRequired()])
    jumlah = IntegerField('Jumlah', validators=[DataRequired()])


# Tanpa model basisdata
class FormCariObat(FlaskForm):
    daftar_atribut = [(None, None), ('kode', 'Kode'), ('keterangan', 'Keterangan'), 
    ('kadaluarsa', 'Kadaluarsa'), ('pencatat', 'Pencatat')]

    pilihan = SelectField('Pilih atribut', choices=daftar_atribut)
    kotak_pencarian = SearchField('Cari sesuatu', validators=[DataRequired()])
    submit_cari = SubmitField('Cari')
    reset = SubmitField('Batalkan')

class FormHapusObat(FlaskForm):
    pilihan_obat = SelectField('Pilih obat', choices=indeks_semua_obat())
    submit = SubmitField('Hapus')
    batal = SubmitField('Batalkan')

