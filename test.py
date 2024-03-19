from flask import Flask,render_template,redirect,request
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyB7-5v_4scJzU6tfXhVOfW3SRlWk74b6cg",
  "authDomain": "authentication-app-59d78.firebaseapp.com",
  "databaseURL": "https://authentication-app-59d78-default-rtdb.firebaseio.com",
  "projectId": "authentication-app-59d78",
  "storageBucket": "authentication-app-59d78.appspot.com",
  "messagingSenderId": "517158776062",
  "appId": "1:517158776062:web:43d436c5d540578c8749af"
}
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

# Read data:
# data = db.child("users").get().val()
# print(data)

auth = firebase.auth()

# Sign in a user:
# user = auth.sign_in_with_email_and_password(email, password)

# # Create a user:
# user = auth.create_user_with_email_and_password(email, password)


# # Send the data:
db.child("intents_and_questions").set({
          "greet": ["None"]
          })

# db.reference('intents_and_questions').set({
#     'greet': []
# })

# updated the data:
# db.child("users").update({"name": "todeti"})

# retrive  the data:
# users=db.child("users").child("name").get()
# print(users.val())
# print(users.key())

# remove the data the data:
# db.child("users").child("name").remove()



# Get data from the "user" node:
# user_data = db.reference('user').get()

# # Push a new intent:
# db.reference('user').push({"intentname": intentname})

# # Update an intent:
# db.reference('user').child(intent_id).update({"intentname": new_intent_name})

# # Delete an intent:
# db.reference('user').child(intent_id).delete()




