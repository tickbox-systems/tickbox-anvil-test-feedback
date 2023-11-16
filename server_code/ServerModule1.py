import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

# This is a server module. It runs on the Anvil server, rather than in the user's browser.
# To allow anvil.server.call() to call functions here, we mark them with @anvil.server.callable.

@anvil.server.callable
def add_feedback(name, email, feedback):
  app_tables.tblfeedback.add_row(
    Name=name, 
    Email=email, 
    Feedback=feedback, 
    DateCreated=datetime.now()
  )
  # Send email each time feedback is submitted
  anvil.email.send(to="contact.web@tickboxsystems.com", 
                   subject=f"Feedback from {name}",
                   text=f""" A new person has filled out the feedback form! Name: {name} Email address: {email} Feedback: {feedback} """)