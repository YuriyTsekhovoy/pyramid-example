from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')
Session = sessionmaker(bind=engine)
session = Session(bind=engine)


@view_config(
    route_name='filtering',
    renderer='templates/filtering.mako'
)
def filtering(request):
    value = '%(value)s' % request.matchdict
    column = '%(column)s' % request.matchdict
    table = '%(table)s' % request.matchdict
    with engine.begin() as conn:
        try:
            t = text(f"SELECT * FROM {table} WHERE {table}.{column}='{value}'")
            response = conn.execute(t)
            table_info = text(f'PRAGMA table_info({table});')
            table_info = conn.execute(table_info)
            table_info = [item[1] for item in table_info]
        except SQLAlchemyError:
            return Response(db_err_msg, content_type='text/plain', status=500)
    return {'response': response, 'table': table, 'table_info': table_info}


db_err_msg = """\
Pyramid is having a problem using your SQL database.
May be you have entered wrong Table Name or wrong Column Name.
Table Name and Column Name needs to be capitalized or CamelCased.
/{Table}/{Column}/{value}
After you fix the problem, please restart the Pyramid application to
try it again.
"""

if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_mako')
        config.include('pyramid_debugtoolbar')
        config.add_route('filtering', '/{table}/{column}/{value}')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
