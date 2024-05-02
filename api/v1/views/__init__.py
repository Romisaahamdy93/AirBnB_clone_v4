<<<<<<< HEAD
from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *
=======
#!/usr/bin/python3
"""Entry point for Airbnb_clone_v3 api calls."""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='api/v1')

from api.v1.views.index import *
>>>>>>> 3caa80f4bf3d46c3e6211aafac37fafcaf4aa00d
