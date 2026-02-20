from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))
    level = db.Column(db.String(20))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Kategori(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50))
    prefix = db.Column(db.String(10))


class Merk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    kategori_id = db.Column(db.Integer, db.ForeignKey('kategori.id'))


class Tipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    merk_id = db.Column(db.Integer, db.ForeignKey('merk.id'))


class Asset(db.Model):
    id_asset = db.Column(db.String(20), primary_key=True)
    kategori_id = db.Column(db.Integer, db.ForeignKey('kategori.id'))
    merk_id = db.Column(db.Integer, db.ForeignKey('merk.id'))
    tipe_id = db.Column(db.Integer, db.ForeignKey('tipe.id'))
    nomor_sn = db.Column(db.String(100))
    spesifikasi = db.Column(db.Text)
    tanggal_beli = db.Column(db.Date)
    status = db.Column(db.Enum('Aktif','Rusak','Disimpan', name='status_enum'))


class Karyawan(db.Model):
    id_karyawan = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    departemen = db.Column(db.String(100))
    jabatan = db.Column(db.String(100))


class Lisensi(db.Model):
    id_lisensi = db.Column(db.Integer, primary_key=True)
    nama_software = db.Column(db.String(100))
    no_sn = db.Column(db.String(100))
    tanggal_kadaluarsa = db.Column(db.Date)


class Assignment(db.Model):
    id_transaksi = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.String(20), db.ForeignKey('asset.id_asset'))
    karyawan_id = db.Column(db.Integer, db.ForeignKey('karyawan.id_karyawan'))
    tanggal_serah = db.Column(db.Date)
    tanggal_kembali = db.Column(db.Date)
