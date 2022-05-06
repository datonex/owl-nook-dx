from django.forms import ModelForm

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)

    def __init__(self, *args, **kwargs):
        """
        Initialisation function that adds placeholder and
        remove auto-generated label
        """

        super().__init__(*args, **kwargs)
        self.fields["body"].widget.attrs["placeholder"] = "Add a comment"
        self.fields["body"].label = False
