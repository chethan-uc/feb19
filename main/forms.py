from django import forms
from main.models import Extractor

class ExtractorForm(forms.ModelForm):
	class Meta:
		model = Extractor
		
	def clean(self):
		cleaned_data=super(ExtractorForm, self).clean()
		extractor_file =  cleaned_data['extractor_file']
		if not (str(extractor_file).endswith('.py')):
			raise forms.ValidationError(
				"Extractor script should end with .py"
			)

		return cleaned_data


