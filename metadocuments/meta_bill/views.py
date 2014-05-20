from __future__ import absolute_import

from . import application


views = application['views']
for view_name, view in views.items():
    globals()[view_name] = view
del view
del view_name