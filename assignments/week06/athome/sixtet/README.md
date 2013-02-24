#Week 06

###Done:
- files moved into new (athome) directory
- djangor app installed
- database updated
- server still works
- Build the required models to represent the blog data.
- Add a column for 'pub_date' to the entry model
- Build the urlconf required to present an entry list and a view for posting a
  new entry.  


###To do:
- Allow each entry to be 'owned' by a User. Add a relation field to represent this.
* *HINT* ``django.contrib.auth.models`` defines a ``User`` model.

- Add two new urls:
	* One should show the archive of all posts from a given month and year
  	* One should show all the posts by a single user
- Build views for each URL
- Deploy the blog to VM

###Questions:
- Should I use `get_absolute_url()` as well as doing `pattern()` stuff in the `url.py` file?
- `urls.py` seems to exist globally (for the program) and locally (for the app). What are the important differences between those two uses?
- Does each app have its own set of templates (is that the common protocol?)? Or should `base.html` be in a top-level `templates/` directory?
- maybe I don't need the 'Archive' and `Author` classes in my `djangor/models.py`?