from django import forms

VOTING_CHOICES = (('0', 'I\'ll go',), ('1', 'I won\'t go',))
class VoteForm(forms.Form):
    will_go = forms.MultipleChoiceField(required=False,
        widget=forms.RadioSelect,choices=VOTING_CHOICES)

class MultiVoteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        if 'dynamic_fields' in kwargs:
            dynamic_fields = kwargs.pop('dynamic_fields') #before calling super or we have an error
        else:
            dynamic_fields = []
        super(MultiVoteForm, self).__init__(*args, **kwargs)

        for field in dynamic_fields:
            self.fields[field['name']] = forms.MultipleChoiceField(
                choices=VOTING_CHOICES,
                label=field['label'],
                required=False,
                widget=forms.RadioSelect)