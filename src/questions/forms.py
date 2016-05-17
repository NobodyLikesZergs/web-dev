# coding: utf=8

from django import forms


class QuestionListForm(forms.Form):
    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(('id', 'ID'),
                                            ('title', u'Название',),
                                            ('modified_at',
                                             u'Дата редактирования')),
                                   required=False)
