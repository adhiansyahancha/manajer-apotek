from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required

from .backend.models import DataMasterObat, db
from .backend.forms import FormDataMasterObat, FormCariObat, FormHapusObat

from datetime import datetime

bp = Blueprint('dasbor', __name__)
@login_required
@bp.route('/', methods=['GET', 'POST'])
def root():
    if current_user.is_authenticated:
        form_dmo = FormDataMasterObat()
        form_cari = FormCariObat()
        form_hapus = FormHapusObat()

        # Segala form pembatalan operasi
        if form_cari.reset.data or form_hapus.batal.data:
            return redirect(url_for('dasbor.root'))

        # Form pencarian
        if form_cari.validate_on_submit and form_cari.submit_cari.data:
            kueri = form_cari.kotak_pencarian.data
            pilihan = form_cari.pilihan.data

            if pilihan == 'batch':
                hasil_pencarian = DataMasterObat.query.filter(DataMasterObat.batch.contains(kueri)).all()
            elif pilihan == 'kode':
                hasil_pencarian = DataMasterObat.query.filter(DataMasterObat.kode.contains(kueri)).all()
            elif pilihan == 'keterangan':
                hasil_pencarian = DataMasterObat.query.filter(DataMasterObat.keterangan.contains(kueri)).all()
            elif pilihan == 'kadaluarsa':
                hasil_pencarian = DataMasterObat.query.filter(DataMasterObat.kadaluarsa.contains(kueri)).all()
            elif pilihan == 'pencatat':
                hasil_pencarian = DataMasterObat.query.filter(DataMasterObat.pencatat.contains(kueri)).all()
            else:
                return redirect(url_for('dasbor.root'))

            if not hasil_pencarian:
                flash('Tidak ada hasil')
                return(redirect(url_for('dasbor.root')))

            return render_template('dasbor/super.html',
            DataMasterObat=DataMasterObat, form_dmo=form_dmo,
            hasil_pencarian=hasil_pencarian, form_cari=form_cari, form_hapus=form_hapus)

        # Form pendaftaran data
        try:
            if form_dmo.validate_on_submit and form_dmo.submit.data:
                entri_baru = DataMasterObat(
                    waktu_dimodifikasi=datetime.now(),
                    batch=form_dmo.batch.data,
                    kode=form_dmo.kode.data,
                    kadaluarsa=form_dmo.kadaluarsa.data,
                    keterangan=form_dmo.keterangan.data,
                    masuk=form_dmo.masuk.data,
                    keluar=form_dmo.keluar.data,
                    sisa=(form_dmo.masuk.data - form_dmo.keluar.data),
                    pencatat=current_user.nama
                )
                db.session.add(entri_baru) 
                db.session.commit()
                return redirect(url_for('dasbor.root'))
        except TypeError:
            if form_hapus.validate_on_submit and form_hapus.submit.data:
                DataMasterObat.query.filter_by(kode=form_hapus.pilihan_obat.data).delete()
                db.session.commit()
                db.session.close()
                return redirect(url_for('dasbor.root'))

        return render_template('dasbor/super.html', DataMasterObat=DataMasterObat, 
        form_dmo=form_dmo, form_cari=form_cari, form_hapus=form_hapus)
    else:
        return redirect(url_for('login.masuk'))