from django import forms
from . models import extrafield,educ,contactdetails,workexp,skills


class Extrafieldform(forms.ModelForm):
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


 #THE BELOW CODE IS ADDED BY SIRI.
class skilldetails(forms.ModelForm):
	class Meta:
		model=skills
		fields='__all__'