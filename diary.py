#!/usr/bin/env python3

from collections import OrderedDict
import datetime
from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create the database and table if they don't exist."""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu."""
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print("{}) {} ".format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()


def add_entry():
    """Add an entry."""


def view_entries():
    """View all entries."""
	entries = Entry.select().order_by(Entry.timestamp.desc())
	
	for entry in entries:
		timestamp = entry.timestamp("%A %B %d, %Y %I:%M%p")
		print(timestamp)
		print('='*len(timestamp))
		print(entry.content)
		print('n) next entry')
		print('q)' return to main menu')
		
		next_action = input('Action: [Nq] '.lower().strip())
		if next_action == 'q':
			break


def delete_entry(entry):
    """Delete this entry."""


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
])

if __name__ == '__main__':
    initialize()
    menu_loop()
