from .models import *
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

class IndexView(ListView):
    model = Student
    template_name = 'student/index.html'
    context_object_name = 'student_list'

    limit = 3
    current_page = 1
    students = Student.objects.all()
    paginator = Paginator(students, limit)

    def get_queryset(self):
        # self.current_page = self.kwargs.get('p','1')
        self.current_page = int(self.request.GET.get('p', 1))
        if self.current_page is None:
            self.current_page = 1
        students = self.paginator.page(self.current_page)
        return students
        # return Student.objects.order_by('-student_age')[:]
        # return Student.objects.filter(student_sex__contains='girl')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        page_list = []
        if self.current_page <= 5:
            for i in range(1, 11):
                page_list.append(i)
        elif self.current_page > self.paginator.num_pages - 5:
            for i in range(self.paginator.num_pages - 9, self.paginator.num_pages + 1):
                page_list.append(i)
        else:
            for i in range(self.current_page - 5, self.current_page + 5):
                page_list.append(i)

        page_data = {'page_num':self.paginator.num_pages,
                     'pre_page':self.current_page - 1,
                     'next_page':self.current_page + 1,
                     'current_page':self.current_page,
                     'page_list':page_list}
        context.update(page_data)
        return context