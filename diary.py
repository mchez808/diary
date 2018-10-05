#!/usr/bin/env python3

from collections import OrderedDict
import datetime
import sys

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
		print("------------------")
		print("Enter 'q' to quit.")
		for key, value in menu.items():
			print("{}) {} ".format(key, value.__doc__))
		choice = input('Action: ').lower().strip()

		if choice in menu:
			menu[choice]()


def add_entry():
	"""Add an entry."""
	# print("Enter a diary entry. Press CTRL+D to submit.")
	# data = sys.stdin.read().strip()
	print("Enter a one-line diary entry. Press Enter to submit.")
	data = input()

	if data:
		if input("Submit entry? [Yn] ").lower() != "n":
			Entry.create(content=data)
			print("Entry submitted.")


def view_entries(search_query=None):
	"""View all entries."""
	entries = Entry.select().order_by(Entry.timestamp.desc())
	if search_query:
		entries = entries.where(Entry.content.contains(search_query))

	for entry in entries:
		timestamp = entry.timestamp("%A %B %d, %Y %I:%M%p")
		print(timestamp)
		print('='*len(timestamp))
		print(entry.content)
		print("n) next entry")
		print("d) delete entry")
		print("q)' return to main menu")

		next_action = input('Action: [Ndq] '.lower().strip())
		if next_action == 'q':
			break
		elif next_action == 'q':
			delete_entry(entry)


def search_entries():
	"""Search entries for a string."""
	view_entries(input('Search query: '))


def delete_entry(entry):
    """Delete this entry."""
    if ("Are you sure you want to delete? [yN] ").lower() == 'y':
        Entry.delete_instance()
        input("Entry deleted.")


menu = OrderedDict([
	('a', add_entry),
	('v', view_entries),
	('s', search_entries),
])


if __name__ == '__main__':
	initialize()
	menu_loop()
