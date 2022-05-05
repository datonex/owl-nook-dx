from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)

    def __init__(self, *args, **kwargs):
        """
        Initialisation function that adds placeholders and classes and
        remove auto-generated labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        self.fields["body"].widget.attrs["placeholder"] = "Add a comment"
        self.fields["body"].label = False
