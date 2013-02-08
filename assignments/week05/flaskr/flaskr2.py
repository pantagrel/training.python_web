import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

app = Flask(__name__)

#learn how to separate config files and load them
#from_ennvvar() ##app.config.from_envvar('FLASKR_SETTINGS', silent=True)
