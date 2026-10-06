import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("serviceAccountKey.json")

app = firebase_admin.initialize_app(cred)

print("Firebase project:", app.project_id)

db = firestore.client(database_id="default")

print("Firestore client created")

document = db.collection("news_summaries").add({
    "summary": "This is my first Firestore test",
    "created_at": "2026-09-27 18:30:00"
})

print("Successfully written to Firestore!")
print("Document:", document[1].id)
