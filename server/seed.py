#!/usr/bin/env python3

from random import choice as rc
from faker import Faker

from app import app, db
from models import Message

fake = Faker()

# List of random usernames, ensuring "Duane" is included
usernames = [fake.first_name() for _ in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():
    # Ensure the table exists
    db.create_all()

    # Clear existing messages
    Message.query.delete()

    messages = []
    for _ in range(20):
        message = Message(
            body=fake.sentence(),
            username=rc(usernames)
        )
        messages.append(message)

    db.session.add_all(messages)
    db.session.commit()
    print("Database seeded with 20 random messages!")

if __name__ == "__main__":
    with app.app_context():
        make_messages()
