from wtforms                 import fields
from wtforms_local.bootstrap import widgets

class TextField(fields.TextField):
    widget = widgets.TextInput()

class PasswordField(fields.PasswordField):
    widget = widgets.PasswordInput()

class BooleanField(fields.BooleanField):
    widget = widgets.CheckboxInput()
