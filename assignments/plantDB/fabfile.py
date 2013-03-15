from fabric.api import env, abort, run
from fabric.contrib.project import rsync_project
from fabric.contrib.console import confirm
from fabric.decorators import runs_once
import os.path
 
# The user I want to log in with
env.user = 'uw'
 
# env is an object, so you can append anything else you want to it.
# Here I'm adding a property with the path to my app's directory
# on the server.
env.webapp_path = '/var/www/sites/'
 
 
# another custom property, using env.real_fabfile path to set
# the local project dir.
# see http://fabric.readthedocs.org/en/0.9.0/usage/env.html
env.local_project_dir = os.path.dirname(env.real_fabfile)
 
# another custom property. Used with the 'rsync' command. For Djangor, I
# configured my production environment to dump all static files into a folder
# called 'webroot'. I am excluding it here, because I set up rsync to delete
# files that exist on production but don't exist on my local copy. In general
# the 'delete' flag is a good thing for keeping everything in sync (no cruft
# files floating around on production). But in this case I want to keep webroot.
env.excluded = ['webroot']
 
 
# My <target> is named production. Since Fabric runs functions in order,
# this the simplest way to get "fab <target> <tasks>"
def production():
    env.name = 'production'
    env.hosts = [
        'block647048-4cf.blueboxgrid.com',
    ]
 
 
#######################
 
# My rsync command. Makes use of the contributed `rsync_project` command.
# More info here: http://docs.fabfile.org/en/1.4.0/api/contrib/project.html
def rsync(extras=''):
    """
    Rsync project files
    """
    rsync_project(
        remote_dir=env.webapp_path,
        local_dir="{0}/".format(env.local_project_dir),
        delete=True,
        exclude=env.excluded + ['fabfile.py', '.*', '*.pyc', '*.iml', '*~'],
        extra_opts='--archive --update ' + extras,
    )
 
 
# My collectstatic command. Pretty straightforward. Wrapping this in the
# `runs_once` decorator to ensure we only do this once per command.
@runs_once
def collectstatic():
    """
    Runs collectstatic
    """
    run(env.webapp_path + 'manage.py collectstatic --noinput')
 
 
# a simple command that runs `touch` on the django wsgi file.
# Apache will reload wsgi scripts if the modified data changes on the wsgi file.
# The 'touch' command does just that. In this way we can 'reload' the
# web application without restarting apache.
def touch_WSGI():
    """
    Touches the wsgi file to trigger a refresh of the site
    """
    run('touch ' + env.webapp_path + 'site_config/production-django.wsgi')
 
 
# All of these functions can now be wrapped in a single function. A confirmation
# gate has been added to ensure the user is aware of what they're doing.
def deploy(extras=''):
    """
    Deploy code
    """
    if not confirm('Are you sure you want to deploy to ' + env.name + '?', default=False):
        abort('Deployment aborted')
 
    # upload from local to the server
    rsync(extras)
 
    # collectstatic
    collectstatic()
 
    # touch wsgi
    touch_WSGI()