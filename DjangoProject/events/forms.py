from django.forms import Form,ModelForm,ChoiceField,RadioSelect
from events.models import *
from events.widgets import *

VOTING_CHOICES = (('1', 'I\'ll go',), ('0', 'I won\'t go',),('-1', 'Haven\'t decided yet',))

class MultiVoteForm(Form):
    def __init__(self, *args, **kwargs):
        if 'dynamic_fields' in kwargs:
            dynamic_fields = kwargs.pop('dynamic_fields') #before calling super or we have an error
        else:
            dynamic_fields = []
        super(MultiVoteForm, self).__init__(*args, **kwargs)

        for field in dynamic_fields:
            self.fields[field['name']] = ChoiceField(
                choices=VOTING_CHOICES,
                label=field['label'],
                required=True,
                initial=VOTING_CHOICES[2][0],
                widget=RadioSelect(renderer=RadioCustomRenderer,attrs={'class': 'Your name',}))
