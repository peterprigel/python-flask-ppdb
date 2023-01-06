#Berfungsi : untuk membuat route yang mengarah ke beberapa halaman pada website

from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
# from flask import Flask, send_from_directory
# import os
# from . import mysql

#membuat blueprint
#jika buat routing, jangan lupa di store ke file __init__.py
auth = Blueprint('auth', __name__)

#definisi variabel untuk MySQL()
mysql = MySQL()

# @auth.route('/')
# #home function
# def home():
#     print(session)
#     if 'loggedin' in session:
#         return render_template('home.html')
#     #alihkan ke home page (home.html)
#     return redirect(url_for("auth.login"))
#     # return render_template('index.html')


#routing untuk page login, ketika mengakses link/login. mendefinisikan juga GET dan POST
@auth.route('/login', methods=['GET','POST'])
#login function
def login():
    if 'loggedin' in session:
        return redirect(url_for("views.home"))
    else:
        #menanggapi request POST
        if request.method == 'POST':
            #mengambil data input dari form di website
            nisn = request.form.get('nisn')
            password = request.form.get('password')

            #mengambil data email pada database, sesuai dengan input email pada form website
            cur = mysql.connection.cursor()
            cur.execute(f"SELECT * FROM user WHERE nisn = '{nisn}'") #teks dalam kutip adalah sintaks mysql
            #variabel menampung data database yang diambil, dalam bentuk tuple
            data = cur.fetchone()
            # user = data[0]

            #program if untuk mengecek apakah email ada pada database atau tidak
            if data != None:
                #jika email ada jalankan percabangan untuk passwd
                if check_password_hash(data[3], password):
                    print("Benar")
                    #jika passwd benar pop up berhasil login muncul pada tampilan website
                    # flash('Login Succeed.', category='success')
                    session['loggedin'] = True
                    session['username'] = data[1]
                    # login_user(user, remember=True)
                    #jika passwd benar alihkan ke page home
                    return redirect(url_for('views.home'))
                else:
                    print("Salah")
                    #pop up error muncul pada tampilan website
                    flash('Password tidak sesuai')
            else:
                #jika tidak ada email tampilkan pesan error
                flash("Akun belum terdaftar")

    # #kembali ke tampilan login.html jika eksekusi gagal
    return render_template("login.html")

#routing untuk page logout
@auth.route('/logout',methods=['GET','POST'])
# @login_required
#logout function
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    print(session)
    return redirect(url_for('views.home'))

#routing untuk page sign up, mendefinisikan juga GET dan POST
@auth.route('/sign-up', methods=['GET','POST'])
#signup function
def signup():
    if 'loggedin' in session:
        return redirect(url_for("views.home"))
    else:
        #menanggapi request POST
        if request.method == 'POST':
            #mengambil data input dari form di website
            nisn = request.form.get('nisn')
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

            print(nisn,username,email,password)

            cur = mysql.connection.cursor()
            cur.execute(f'SELECT * FROM user WHERE nisn={nisn}')
            # data = cur.fetchall()
            dataCek = cur.fetchone()
            cur.close()

            #program if untuk mengecek & memberi warning apakah inputan sesuai apa tidak
            #jika tidak sesuai makan akan muncul tampilan pesan error
            #jika sesuai maka akan lanjut ke input data ke database dan muncul tampilkan berhasil sign up
            if dataCek != None:
                flash('NISN telah terdaftar')
            elif len(nisn) < 10:
                flash('Format NISN tidak sesuai')
            elif len(username) < 4:
                flash('Username terlalu pendek')
            elif len(email) < 4:
                flash('Email tidak sesuai')
            elif len(password) < 7:
                flash('Password harus 8 digit atau lebih')
            else:
                #jika inputan sesuai, lanjut untuk input data ke dalam database
                cursor = mysql.connection.cursor()
                password = generate_password_hash(password)
                cursor.execute("INSERT INTO user(nisn,username,email,password) VALUES (%s, %s, %s, %s)", (nisn, username, email, password)) #teks dalam kutip adalah sintaks mysql
                mysql.connection.commit()
                #jika berhasil alihkan ke page login
                return redirect(url_for('auth.login'))
                #jika berhasil tampilkan pesan berhasil
                flash('Account created!', category='success')

    # #jika proses di atas dilewati hingga mengeksekusi bagian sini, alihkan ke page sign up saja
    return render_template("registrasi.html")


@auth.route('/informasi-sekolah')
def informasi_sekolah():
    return render_template("informasi_sekolah.html")

@auth.route('/informasi-persyaratan')
def informasi_persyaratan():
    return render_template("informasi_persyaratan.html")

@auth.route('/pendaftaran-siswa', methods=['GET','POST'])
def pendaftaran_siswa():

    if 'loggedin' in session:
        if request.method == 'POST':
            nisn = request.form.get('nisn')
            nama = request.form.get('nama')
            tempat_lahir = request.form.get('tempat_lahir')
            tanggal_lahir = request.form.get('tanggal_lahir')
            jenis_k = request.form.get('jenis_k')
            agama = request.form.get('agama')
            alamat_rumah = request.form.get('alamat_rumah')
            kabupaten_kota = request.form.get('kabupaten_kota')
            provinsi = request.form.get('provinsi')
            no_telp = request.form.get('no_telp')
            
            nama_ayah = request.form.get('nama_ayah')
            nama_ibu = request.form.get('nama_ibu')
            alamat_rumah_ot = request.form.get('alamat_rumah_ot')
            no_telp_ot = request.form.get('no_telp_ot')

            nama_wali = request.form.get('nama_wali')
            alamat_rumah_w = request.form.get('alamat_rumah_w')
            no_telp_w = request.form.get('no_telp_w')

            bindo = request.form.get('bindo')
            bing = request.form.get('bing')
            matematika = request.form.get('matematika')
            ipa = request.form.get('ipa')

            jalur_pendaftaran = request.form.get('jalur_pendaftaran')
            jurusan_pertama = request.form.get('jurusan_pertama')
            jurusan_kedua = request.form.get('jurusan_kedua')
                
            print(nisn,nama,tempat_lahir,tanggal_lahir,agama)

            #jika inputan sesuai, lanjut untuk input data ke dalam database
            cursor = mysql.connection.cursor()
            attr = """INSERT INTO pendaftaran_siswa 
            (nisn, nama, tempat_lahir, tanggal_lahir, jenis_k, agama, alamat_rumah, kabupaten_kota, provinsi, no_telp, nama_ayah, nama_ibu, alamat_rumah_ot, no_telp_ot, nama_wali, alamat_rumah_w, no_telp_w, bindo, bing, matematika, ipa, jalur_pendaftaran, jurusan_pertama, jurusan_kedua) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            nilai = (nisn, nama, tempat_lahir, tanggal_lahir, jenis_k, agama, alamat_rumah, kabupaten_kota, provinsi, no_telp, nama_ayah, nama_ibu, alamat_rumah_ot, no_telp_ot, nama_wali, alamat_rumah_w, no_telp_w, bindo, bing, matematika, ipa, jalur_pendaftaran, jurusan_pertama, jurusan_kedua)
            cursor.execute(attr,nilai)
            mysql.connection.commit()

            #jika berhasil alihkan ke page login
            return redirect(url_for('auth.status_pendaftaran_siswa'))

        return render_template("pendaftaran_siswa.html")
        
    return redirect(url_for('auth.login'))

@auth.route('/status-pendaftaran-siswa')
#logout function
def status_pendaftaran_siswa():
    if 'loggedin' in session:
    
        cur = mysql.connection.cursor()
        cur.execute('SELECT nisn,nama,jurusan_pertama,jurusan_kedua FROM pendaftaran_siswa')
        data = cur.fetchall()
        # data = cur.fetchone()
        cur.close()

        # return render_template('mahasiswa/data-mahasiswa.html', mahasiswa = data)
        return render_template('status_pendaftaran_siswa.html', mahasiswa = data)

    return redirect(url_for('auth.login'))
