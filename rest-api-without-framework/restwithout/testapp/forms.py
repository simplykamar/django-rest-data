from .models import Student
from django import forms

class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields='__all__'

	def clean_marks(self):
		inputmarks=self.cleaned_data['marks']
		if inputmarks < 35:
			raise forms.ValidationError('Marks Should be >= 35')
		return inputmarks
		