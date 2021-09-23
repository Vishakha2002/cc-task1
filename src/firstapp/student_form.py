from wtforms import Form, StringField, SelectField, IntegerField, validators

class StudentSearchForm(Form):
    choices = [('first_name', 'First Name'),
               ('last_name', 'Last Name'),
               ('id', 'Student ID')]
    select = SelectField('Select Identifier:', choices=choices)
    search = StringField('Input Search String:')

class StudentAddForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email')
    mailing_address = StringField('Mailing Address')
    gpa = IntegerField('GPA')
