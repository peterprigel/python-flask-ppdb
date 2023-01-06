#Berfungsi : mengimpor aplikasi dan memulai server pengembangan.

#import create_app function through website folder
#why website folder? because there is a file __init__.py that turn the website folder to the python package
from website.__init__ import create_app
# from flask_mysqldb import MySQL

#create_app() berasal dari funsi pada file __init__.py
app = create_app()

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='10.180.1.229', port='5000', debug=True)