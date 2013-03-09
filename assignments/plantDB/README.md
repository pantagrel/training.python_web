##Setting up a project
___

###Open a virtualenv or make a new one. 

(See [#](creating a virtualenv))

###If Django isn't installed in the virtualenv, install it using pip.

	pip install django

###Confirm which version of Django is running, if necessary.
	
	which django-admin.py

###Create the project directory. 

	django-admin.py startproject [myproject]

This will create two folders. The outer folder is just the container for the actual project stuff. If you want change the outer folder to a different now, do it now because we're going to set up git next and changing folder names after we do any git commits might get confusing. So keep it simple and either change it right now or don't.

###Check to see if the package development server works. 

Change into the outer `myproject` directory and run:
	
	python manage.py runserver [8080]
	
If you want to change the development port, `[8080]` is the optional argument you would add to the above command.

Go to `127.0.0.1:8000/` in your browser. You should see a message like this:

	0 errors found
	Django version 1.4.3, using settings 'sixProject.settings'
	Development server is running at http://127.0.0.1:8000/
	Quit the server with CONTROL-C.

If not, be sure you're either in the correct directory (the outer directory), or change your path accordingly to call the `manage.py` file.

###Set up git for the project.
	
	git init
	git add myproject
	git commit -m 'first commit etc etc'

Add the files to github, if you wish:

    git remote add origin git@github.com:pantagrel/plantDB.git
    git push -u origin master

###Add South for database migrations. Not sure why yet, but do it.

	pip install south

South, as well as any other apps you will install later, has to be added to the list of installed apps in the `settings.py` file. Put it at the end of the tuple that also contains `django.contrib.admin` at about `line 122`. At the end of the tuple, add south--as a string--like so:
    
    `'south',`

Be sure to include that trailing comma.

##Setting up the database
___

###Pick the database you'll be using and get that set up. 

    `[DATABASE CONTENT GOES HERE.]`

[3.1.2013: I only know know to use sqlite at this time, so this documentation will have to be augmented in future. Stay tuned.]

Once the database is set up, run `syncdb` to set up any new tables. 

        python manage.py syncdb

At this point, this set up all the tables since this is the first time we've run `syncdb` for this project. As you add apps, you'll need to run that command to add the necessary new tables to the database. `syncdb` merely instantiates new, empty tables--it does not update your database. 


###Create an app

	python manage.py startapp [myapp]

###Set up some subclasses

###Re-sync the database to create those new tables

	python manage.py syncdb
	
>I set up a table incorrectly (made an IntegerField have a 
>max_length=2), and the database needed to be deleted and re-synced in 
>order for `class Plant` to work correctly in the interactive shell.

This command creates tables that don't already exist--it *DOESN'T* UPDATE THE DATABASE.


##Django admin
___
###Enable the admin
In `settings.py` file, uncomment (approx) line 118: `django.contrib.admin`. In `urls.py` file, uncomment lines 4, 5, and 16: `from django.contrib import admin`, `admin.autodiscover()`, and `url(r'^admin/', include(admin.site.urls))`.

###Make plants app show up in the admin
Create an admin file inside the app folder.

    from django.contrib import admin
    from plant.models import Plant
    admin.site.register(Plant)
    
**Though the last line may need to be augmented with a PlantAdmin function. Will expand this explanation later.

##Building the app
___
Let's look at how all the files fit together. It's called 'loose coupling'. This is preliminary understandings, after a few weeks of working with Django. (Let's see how this info shakes out in a few months.)

###`models.py`
This piece of the app is what builds the database. You name your tables here, and set the type of data those tables will take. There can be multiple classes in a `models.py` file. Model field reference page in the Django documentation is helpful for styling the data. `django.db.models.fields`

* How many classes are usually in a given file? Just in general.

* The different tables are described as "metadata"...but what is and isn't metadata?

###`views.py`
This piece of the app is where different page views are defined. You're syncing up metadata from `models.py` with template display information via a given function that you write within `views.py`. 

###`app/urls.py`
This piece is where you define what views will appear for a given URL. This makes use of regular expressions, which I do not currently understand how to write, to find and build appropriate URLs at appropriate times. There is other setup/coupling data happening that I also don't totally understand yet.

###`project/urls.py`
This piece is a topmost level of URL-defining. All the app `urls.py` data will do it's thing and then get finally routed through the criteria set up in this file. This is how you manage all the URL info coming in from all the separate apps comprising a given project.

###Templates
This piece pulls in information from `views.py`--dictionaries containing object information about stuff in your database, and how to display certain portions of that dictionary data in on a given web page. Variables and simple loop-stuff can be used. Templates also help build the URLs, using the structures we set up in our `urls.py` files and the variables that get passed in from those dictionaries mentioned above.


##Questions
___
* How do I update entries in the database?
* 

##Tips
___

Play around in the interactive Python shell that comes with Django:

    python manage.py shell
    
Here is the syntax for returning a more descriptive `__unicode__` object? One example:

    return ('%s %s' % (self.genus, self.species))

Create a new superuser:

    manage.py changepassword admin

Change password:
	
    manage.py changepassword <username>



##Things I need to know more about:
___

- Creating and working with custom classes
- Deployment
	- For a real website, where does hosting come from?
	- What other tools do I need besides Django and a database? Javascript? 
