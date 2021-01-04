import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = '6B499.GoKLFH0um6z5WJ41u~5Gh2.cv-AU'

    BLOB_ACCOUNT = 'hellowworld1234'
    BLOB_STORAGE_KEY = '8VChNZcje4O3GFd651xQApy5hsY0+mPLU+hN8q78LWEf61mtrvknloQVU3BFCODl8vjfK1O+otoeRlXIl4vYxQ=='
    BLOB_CONTAINER = 'images'

    SQL_SERVER = 'hellowworlddb.database.windows.net'
    SQL_DATABASE = 'author'
    SQL_USER_NAME = 'bikash'
    SQL_PASSWORD = 'Udacity@9851225856'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "6B499.GoKLFH0um6z5WJ41u~5Gh2.cv-AU"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/2ffc2ede-4d44-4994-8082-487341fa43fb"

    CLIENT_ID = "c5563e24-0233-4f02-9622-d0034ae70241"
#    REDIRECT_FULL_PATH = "http://localhost:5000/getAToken"
    # http://localhost:5000/getAToken
    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD
#    ENDPOINT = 'https://graph.microsoft.com/v1.0/users'
    SCOPE = ["User.ReadBasic.All"]
    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
