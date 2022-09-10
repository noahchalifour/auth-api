
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from auth.api.authorize_api import AuthorizeApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from auth.api.authorize_api import AuthorizeApi
from auth.api.clients_api import ClientsApi
from auth.api.init_api import InitApi
