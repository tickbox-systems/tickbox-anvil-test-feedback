from ._anvil_designer import frmFeedbackTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class frmFeedback(frmFeedbackTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btnSubmit_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Set 'name' to the text in the 'name_box'
    name = self.tbxName.text
    # Set 'email' to the text in the 'email_box'
    email = self.tbxEmail.text
    # Set 'feedback' to the text in the 'feedback_box'
    feedback = self.txaFeedback.text
    # Call your 'add_feedback' server function
    # pass in name, email and feedback as arguments
    anvil.server.call('add_feedback', name, email, feedback)
    Notification("Tickbox Feedback submitted!").show()
    self.clear_inputs()

  def clear_inputs(self):
    # Clear our three text boxes
    self.tbxName.text = ""
    self.tbxEmail.text = ""
    self.txaFeedback.text = ""