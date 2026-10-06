import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime


cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred)

db = firestore.client(database_id="default")


def save_summary(summary):

    db.collection("news_summaries").add({
        "summary": summary,
        "created_at": datetime.now()
    })

    print("Summary saved to Firebase!")
