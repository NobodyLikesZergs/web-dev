from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import resolve_url, get_object_or_404
from .models import Question
from comments.models import Comment
from .forms import QuestionListForm


class QuestionList(ListView):
    model = Question
    template_name = 'questions/question_list.html'
    qform = QuestionListForm()

    def dispatch(self, request, *args, **kwargs):
        self.form = QuestionListForm(data=request.GET)
        self.form.is_valid()
        return super(QuestionList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Question.objects.all()
        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(
                title__contains=self.form.cleaned_data['search'])
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_field'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(QuestionList, self).get_context_data(**kwargs)
        context['qform'] = self.qform
        return context


class QuestionView(CreateView):
    model = Comment
    template_name = 'questions/question_view.html'
    fields = ('text', )

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.question = get_object_or_404(Question, id=pk)
        return super(QuestionView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        context['question'] = self.question
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.parent_question = self.question
        return super(QuestionView, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('questions:question_view', pk=self.question.pk)


class QuestionCreate(CreateView):
    model = Question
    template_name = 'questions/question_create.html'
    fields = ('title', 'text')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(QuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('questions:question_view', pk=self.object.pk)


class QuestionUpdate(UpdateView):
    model = Question
    template_name = 'questions/question_update.html'
    fields = ('title', 'text')

    def get_success_url(self):
        return resolve_url('questions:question_view', pk=self.object.pk)
