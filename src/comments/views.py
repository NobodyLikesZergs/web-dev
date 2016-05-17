from django.views.generic import UpdateView
from django.shortcuts import resolve_url
from .models import Comment


class CommentUpdate(UpdateView):
    model = Comment
    template_name = 'comments/comment_update.html'
    fields = ('text',)

    def get_success_url(self):
        return resolve_url('questions:question_view',
                           pk=self.object.parent_question.pk)
