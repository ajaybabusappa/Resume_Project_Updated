from django import forms
from . models import extrafield,educ,contactdetails,workexp,skills


class Extrafieldform(forms.ModelForm):
	class Meta:
		model = extrafield
		fields ='__all__' 

		widgets = {
     
            'author' : forms.TextInput(attrs={'class':'form-group','type':'hidden'})
            }



			
class Educationdetails(forms.ModelForm):
	class Meta:
		model = educ
		fields ='__all__'
		widgets = {
     
            'author' : forms.TextInput(attrs={'class':'form-group','type':'hidden'})
            }


class contactdetailsform(forms.ModelForm):
	class Meta:
		model = contactdetails
		fields ='__all__'
		widgets = {
     
            'author' : forms.TextInput(attrs={'class':'form-group','type':'hidden'})
            }
	


class jobform(forms.ModelForm):
	class Meta:
		model = workexp
		fields ='__all__'
		widgets = {
     
            'author' : forms.TextInput(attrs={'class':'form-group','type':'hidden'})
            }


 #THE BELOW CODE IS ADDED BY SIRI.
class skilldetails(forms.ModelForm):
	class Meta:
		model=skills
		fields='__all__'
		widgets = {
     
            'author' : forms.TextInput(attrs={'class':'form-group','type':'hidden'})
            }




from django import forms
from .models import Resume_No
class Rform(forms.ModelForm):
    class Meta:
        model = Resume_No
        fields = ('name','author')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-group'}),
            'author' : forms.TextInput(attrs={'class':'form-group','value':'','id' :'a','type':'hidden'})
            }