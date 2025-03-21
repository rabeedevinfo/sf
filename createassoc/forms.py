from django import forms
from .models import Code_Koraa, Participant

from django import forms
from .models import Code_Koraa


class CodeKoraaForm(forms.ModelForm):
    amount = forms.IntegerField(
        label="المبلغ",  # Custom label
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل المبلغ'})
    )

    number_part = forms.IntegerField(
        label="عدد المشاركين",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'عدد المشاركين'})
    )

    date_deb = forms.DateField(
        label="تاريخ البداية",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )



    class Meta:
        model = Code_Koraa
        fields = ['amount', 'number_part', 'date_deb']


class ParticipantForm(forms.ModelForm):
    class Meta:
        #code_koraa = forms.CharField# Correct ForeignKey reference
        name = forms.CharField(max_length=50)
        model = Participant
        fields = ['name']