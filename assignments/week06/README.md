#django

##setting up a project


###Open a virtualenv or make a new one. 

(See [#](creating a virtualenv))

###If Django isn't installed in the virtualenv, install it using pip.

	pip install django

###Confirm which version of Django is running, if necessary.
	
	which django-admin.py

###Create the project directory. 

	django_admin.py startproject [myproject]

This will create two folders. The outer folder is just the container for the actual project stuff. If you want change the outer folder to a different now, do it now because we're going to set up git next and changing folder names after we do any git commits might get confusing. So keep it simple and either change it right now or don't.

###Check to see if the package development server works. 

Change into the outer `myproject` directory and run:
	
	python manage.py runserver

You should see a message like this:

	0 errors found
	Django version 1.4.3, using settings 'sixProject.settings'
	Development server is running at http://127.0.0.1:8000/
	Quit the server with CONTROL-C.

If not, be sure you're either in the correct directory (the outer directory), or change your path accordingly to call the `manage.py` file.

###Set up git for the project.
	
	git init

And then add all the files you've just made (The two folders, plus the basic django starter files like `manage.py` and `myproject/settings.py`).

	git add myproject

And commit the files to the repo:

	git commit -m 'first commit etc etc'

- ###Add South for database migrations. Not sure why yet, but do it.

	pip install south

South has to be added to the list of installed apps in the `settings.py` file.

###Pick the database you'll be using and get that set up. 