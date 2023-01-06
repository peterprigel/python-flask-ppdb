# Berfungsi : menginisialisasi aplikasi Anda membuat instance aplikasi Flask.

# inisialisasi adalah pemberian nilai awal yang dilakukan saat deklarasi variabel atau objek
# instance adalah variabel yang menyimpan alaman memori objek
# this file is used to make website folder to > python package.
# used for some "import things" in website folder
from flask import Flask
from flask_mysqldb import MySQL
from flask_login import LoginManager

#create_app function
def create_app():
    #mengimpor flask
    app = Flask(__name__)
    #membuat secret key untuk keperluan security
    app.config['SECRET_KEY'] = 'webppdb-tugasbesaralpro'

    # Konfigurasi koneksi untuk database MySQL
    app.config['MYSQL_HOST'] = 'localhost' 
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'ppdb_db'
    # app.config['SERVER_NAME'] = 'tritheppdb.com:5000'
    mysql = MySQL(app)

    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)

    #meng-import file views dan auth
    from .auth import auth
    from .views import views
    
    #registerasi blueprint file views dan auth
    # fungsi nya kurang tau untuk apa (?)
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))

    return app
