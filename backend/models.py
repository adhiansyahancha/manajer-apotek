from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

from .extensions import db

class Pengguna(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    surel = db.Column(db.String(64), index=True, unique=True)
    kata_sandi = db.Column(db.String(128))
    nama = db.Column(db.String(16), index=True)
    level = db.Column(db.SmallInteger, unique=True)
    # Level 1: Superuser
    # Level 2: Administrator
    # Level 3: Pengguna

    def __repr__(self):
        return f'<Pengguna yang didaftarkan: {self.surel}>'

    def set_sandi(self, p):
        self.kata_sandi = generate_password_hash(p)

    def cek_sandi(self, p):
        return check_password_hash(self.kata_sandi, p)

    def foto_profil(self):
        hashed = md5(self.surel.encode('utf-8')).hexdigest()
        if self.level == 0:
            return 'https://www.gravatar.com/avatar/073849a13f3d3aef61083b768a1c277d?s=500'
        else:
            return f'https://www.gravatar.com/avatar/{hashed}?d=identicon&s=500'


class DataMasterObat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    waktu_dimodifikasi = db.Column(db.DateTime, index=True, default=datetime.now)
    nama_obat = db.Column(db.String(60), index=True, unique=True)
    
    # Harga dalam beberapa satuan
    harga_buah = db.Column(db.Integer, index=True)
    harga_strip = db.Column(db.Integer, index=True)
    harga_eceran = db.Column(db.Integer, index=True)

    # Jumlah dalam beberapa satuan
    jumlah_buah = db.Column(db.Integer, index=True)
    jumlah_strip = db.Column(db.Integer, index=True)
    jumlah_eceran = db.Column(db.Integer, index=True)

    total = db.Column(db.Integer, index=True)
    

    def __repr__(self):
        return f'<Obat yang didaftarkan: {self.nama_obat}>'

    def __init__(self, waktu_dimodifikasi, nama_obat, harga, jumlah, total):
        self.waktu_dimodifikasi = waktu_dimodifikasi
        self.nama_obat = nama_obat
        self.harga = harga
        self.jumlah = jumlah
        self.total = total


class TransaksiObat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    waktu_transaksi = db.Column(db.DateTime, index=True, default=datetime.now) 
    nama_obat = db.Column(db.String(60))
    total = db.Column(db.Integer)

    def __repr__(self):
        return f'Transaksi yang dicatat: {self.kode}'

    def __init__(self, waktu_transaksi, kode, 
    harga_buah, harga_strip, harga_eceran, jumlah_buah, jumlah_strip, jumlah_eceran, total):
        self.waktu_transaksi = waktu_transaksi
        self.kode = kode
        self.harga_buah = harga_buah
        self.harga_strip = harga_strip
        self.harga_eceran = harga_eceran
        self.jumlah_buah = jumlah_buah
        self.jumlah_strip = jumlah_strip
        self.jumlah_eceran = jumlah_eceran
        self.total = total

