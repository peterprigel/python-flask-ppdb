#Berfungsi : untuk membuat route yang mengarah ke beberapa halaman pada website

from flask import Blueprint, render_template, session, url_for, redirect
from flask_login import login_required, current_user
from flask_mysqldb import MySQL
from django.shortcuts import render
from django.http import HttpResponse

#membuat blueprint
#jika buat routing, jangan lupa di store ke file __init__.py
views = Blueprint('views', __name__)

mysql = MySQL()

#routing untuk page home, ketika mengakses link/
@views.route('/')
#home function
def home():
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pendaftaran_siswa')
    data = cur.fetchall()
    data = len(data)
    dataF = {f'{data}'}
    # data = cur.fetchone()
    # cur.close()

    if 'loggedin' in session:
        return render_template('home.html', tPendaftar = dataF)  

    #alihkan ke home page (home.html)
    # return redirect(url_for("auth.login"))
    return render_template('index.html', tPendaftar = dataF)
