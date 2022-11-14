from django.forms import ModelForm, TextInput, Textarea, EmailInput

from blog.models import Contact, Email, Comment


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Enter your name',
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'type': 'email',
                    'placeholder': 'Enter your email',
                }
            ),
            'subject': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Enter subject',
                }
            ),
            'message': Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '8',
                    'placeholder': 'Enter your message',
                }
            )
        }


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ('email',)
        widgets = {
            'email': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Enter your email',
                }
            )
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'author', 'message')
        widgets = {
            'author': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Enter your name',
                }
            ),
            'email': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Enter your email',
                }
            ),
            'message': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your comment',
                }
            )
        }
