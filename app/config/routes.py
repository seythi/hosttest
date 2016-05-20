"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'bookrevs'
routes['POST']['/processRegister'] = 'bookrevs#register'
routes['POST']['/processLogin'] = 'bookrevs#login'
routes['/logout'] = 'bookrevs#logout'
routes['/books/add'] = 'bookrevs#add'
routes['POST']['/addbook'] = 'bookrevs#addbook'
routes['/books'] = 'bookrevs#books'
routes['/home'] = 'bookrevs#index'
routes['/books/<id>'] ='bookrevs#specbook'
routes['POST']['/review']='bookrevs#review'