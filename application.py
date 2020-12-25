"""
This script runs the FlaskWebProject application using a development server.
"""
import uuid
import requests
from os import environ
from FlaskWebProject import app
from flask import Flask, render_template, session, request, redirect, url_for
import msal

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '3000'))
    except ValueError:
        PORT = 3000
    app.run(HOST, PORT, ssl_context='adhoc')
