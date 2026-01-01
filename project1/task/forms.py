from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','realized','due_date']
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter task title'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter task description   ','rows':4}),
            'realized': forms.CheckboxInput(attrs={'class':'form-check-input'}),                    
            'due_date': forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local'}),                                                                                                                                                                
        }