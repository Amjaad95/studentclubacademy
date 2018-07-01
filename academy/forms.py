from django.forms import ModelForm
from academy.models import NewStudent

class NewStudentForm(forms.Form):
    class meta:
        model = models.NewStudent
        fields = [ 'batch', 'worked_in_stuedntclub', 'past_Experience', 'why_would_you_join_us',
        'wants_to_work']
