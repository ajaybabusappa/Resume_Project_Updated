from django import forms
from . models import extrafield,educ,contactdetails,workexp


class Extrafielfform(forms.ModelForm):
	class Meta:
		model = extrafield
		fields = ['field_name','explanation']

			
class Educationdetails(forms.ModelForm):
	class Meta:
		model = educ
		fields =['school_name','school_location','Degree','CGPA','Field_of_Study','Expected_year_of_grad']


class contactdetailsform(forms.ModelForm):
	class Meta:
		model = contactdetails
		fields ='__all__'
	


class jobform(forms.ModelForm):
	class Meta:
		model = workexp
		fields ='__all__'
