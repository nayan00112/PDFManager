from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class Sub_Input(forms.Form):

    SUBJECTS = (
        (('physics'),('Physics')),
        (('mathematic'),('Mathematic')),
        (('bme'),('BME')),
        (('es'),('ES')),
        (('other'),('Other')),
    )

    title = forms.CharField(max_length=30, required=True)
    subject = forms.ChoiceField(choices=SUBJECTS)
    pdf_document = forms.FileField(required=True)
    date = forms.DateField(required=True, widget=DateInput())
    discription = forms.CharField(required=True)
    userhid = forms.CharField( max_length=50, required=True, widget=forms.HiddenInput())