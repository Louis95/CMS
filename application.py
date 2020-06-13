"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from FlaskWebProject import app
import logging
from logging.handlers import RotatingFileHandler
app.logger.info('Info')


if __name__ == '__main__':
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=app.debug)
    # HOST = environ.get('SERVER_HOST', 'localhost')
    # try:
    #     PORT = int(environ.get('SERVER_PORT', '5555'))
    # except ValueError:
    #     PORT = 5000
    # app.run(HOST, PORT, ssl_context='adhoc')
