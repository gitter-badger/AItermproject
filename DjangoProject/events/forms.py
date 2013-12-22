from django import forms

VOTING_CHOICES = (('1', 'I\'ll go',), ('0', 'I won\'t go',),('-1', 'Haven\'t decided yet',))
class VoteForm(forms.Form):
    will_go = forms.ChoiceField(required=False,
        widget=forms.RadioSelect,choices=VOTING_CHOICES)

class MultiVoteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        if 'dynamic_fields' in kwargs:
            dynamic_fields = kwargs.pop('dynamic_fields') #before calling super or we have an error
        else:
            dynamic_fields = []
        super(MultiVoteForm, self).__init__(*args, **kwargs)

        for field in dynamic_fields:
            self.fields[field['name']] = forms.ChoiceField(
                choices=VOTING_CHOICES,
                label=field['label'],
                required=True,
                initial=VOTING_CHOICES[2][0],
                widget=forms.RadioSelect)