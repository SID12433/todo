from django import forms
from task.models import Todos

# class TodoCreateForm(forms.Form):
#     title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     user=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     due_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"date"}))

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["title","user","due_date"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "user":forms.TextInput(attrs={"class":"form-control"}),
            "due_date":forms.DateInput(attrs={"type":"date","class":"form-control"})
    }
    
        
# class TodoChangeForm(forms.Form):
#     title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     due_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"date"}))
#     status=forms.BooleanField()

class TodoChangeForm(forms.ModelForm):
    
    class Meta:
        model=Todos
        fields=["title","status","due_date"]  
        widget={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "due_date":forms.DateInput(attrs={"type":"date","class":"form-control"})
        }                  
       
