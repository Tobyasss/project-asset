from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from config import Config
from models import db, User, Asset, Kategori, Merk, Tipe
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ===============================
# LOGIN
# ===============================
@app.route('/', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            error = "Username atau password salah!"

    return render_template('login.html', error=error)

# ===============================
# DASHBOARD
# ===============================
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# ===============================
# LOGOUT
# ===============================
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# ===============================
# ADD ASSET
# ===============================
@app.route('/add_asset', methods=['GET','POST'])
@login_required
def add_asset():
    kategori_list = Kategori.query.all()
    if request.method == 'POST':
        kategori_id = request.form['kategori']
        merk_id = request.form['merk']
        tipe_id = request.form['tipe']
        nomor_sn = request.form['nomor_sn']
        spesifikasi = request.form['spesifikasi']
        tanggal_beli = datetime.strptime(request.form['tanggal_beli'], "%Y-%m-%d")
        status = request.form['status']

        kategori = Kategori.query.get(kategori_id)
        prefix = kategori.prefix

        last_asset = Asset.query.filter(Asset.id_asset.like(f"{prefix}%")).order_by(Asset.id_asset.desc()).first()
        new_number = int(last_asset.id_asset.replace(prefix, "")) + 1 if last_asset else 1
        new_id = f"{prefix}{str(new_number).zfill(6)}"

        asset = Asset(
            id_asset=new_id,
            kategori_id=kategori_id,
            merk_id=merk_id,
            tipe_id=tipe_id,
            nomor_sn=nomor_sn,
            spesifikasi=spesifikasi,
            tanggal_beli=tanggal_beli,
            status=status
        )
        db.session.add(asset)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('asset_form.html', kategori=kategori_list)

# ===============================
# MASTER PANEL
# ===============================
@app.route('/master_panel', methods=['GET','POST'])
@login_required
def master_panel():
    if current_user.level != 'master':
        return "Access denied", 403

    kategori_list = Kategori.query.all()
    merk_list = Merk.query.all()
    tipe_list = Tipe.query.all()

    if request.method == 'POST':
        jenis = request.form['jenis']
        nama = request.form['nama']

        if jenis == 'kategori':
            prefix = request.form.get('prefix', '')
            db.session.add(Kategori(nama=nama, prefix=prefix))
        elif jenis == 'merk':
            kategori_id = request.form['kategori_id']
            db.session.add(Merk(nama=nama, kategori_id=kategori_id))
        elif jenis == 'tipe':
            merk_id = request.form['merk_id']
            db.session.add(Tipe(nama=nama, merk_id=merk_id))
        db.session.commit()
        return jsonify({"status":"success"})

    return render_template('master_panel.html', kategori=kategori_list, merk=merk_list, tipe=tipe_list)

# ===============================
# AJAX ROUTES
# ===============================
@app.route('/get_merk/<int:kategori_id>')
@login_required
def get_merk(kategori_id):
    merk = Merk.query.filter_by(kategori_id=kategori_id).all()
    return jsonify([{"id": m.id, "nama": m.nama} for m in merk])

@app.route('/get_tipe/<int:merk_id>')
@login_required
def get_tipe(merk_id):
    tipe = Tipe.query.filter_by(merk_id=merk_id).all()
    return jsonify([{"id": t.id, "nama": t.nama} for t in tipe])

# ===============================
# MAIN
# ===============================
if __name__ == '__main__':
    app.run(debug=True)
