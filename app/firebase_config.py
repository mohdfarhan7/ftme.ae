import firebase_admin
from firebase_admin import credentials, firestore

# Path to the Firebase service account key
SERVICE_ACCOUNT_KEY = "firebase_key.json"

# Initialize Firebase app
cred = credentials.Certificate(SERVICE_ACCOUNT_KEY)
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()
