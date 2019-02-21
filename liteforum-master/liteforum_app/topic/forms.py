from django import forms

from .models import Node


class TopicForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea, max_length=20000, required=False)
    node = forms.ModelChoiceField(queryset=Node.objects.all(), empty_label='-请选择一个节点-')


class ReplyForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, max_length=20000)
