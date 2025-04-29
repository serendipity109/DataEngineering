# firebase - backend as a service, BaaS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://activity12-5-3a8ca-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# save data
ref = db.reference('py/')
ref.set({
    'alanisawesome': {
        'date_of_birth': 'June 23, 1912',
        'full_name'   : 'Alan Turing'
    },
    'gracehop': {
        'date_of_birth': 'December 9, 1906',
        'full_name'   : 'Grace Hopper'
    }
})

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())