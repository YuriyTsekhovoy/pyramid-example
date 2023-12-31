from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')


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
            response = conn.execute(text(f"SELECT * FROM {table} WHERE {table}.{column}='{value}'"))
            table_info = [item[1] for item in conn.execute(text(f'PRAGMA table_info({table});'))]
            return {'response': response, 'table': table, 'table_info': table_info}
        except SQLAlchemyError:
            return Response(db_err_msg, content_type='text/plain', status=500)


db_err_msg = """\
Pyramid is having a problem using your SQL database.
May be you have entered wrong Table Name or wrong Column Name.
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
