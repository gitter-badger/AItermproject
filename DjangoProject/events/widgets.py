from django import forms
from django.forms.widgets import RadioFieldRenderer, RadioInput
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.util import ValidationError

class RadioCustomRenderer(RadioFieldRenderer):
    def __iter__(self):
        for i, choice in enumerate(self.choices):
            yield RadioInput(self.name, self.value, self.attrs.copy(), choice, i)

    def __getitem__(self, idx):
        choice = self.choices[idx]
        return RadioInput(self.name, self.value, self.attrs.copy(), choice, idx)

    def render(self):
        return mark_safe(u'%s' % u'\n'.join([u'%s' % force_unicode(w) for w in self]))