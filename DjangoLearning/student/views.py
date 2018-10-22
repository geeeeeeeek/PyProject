from .models import *
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

class IndexView(ListView):
    model = Student
    template_name = 'student/index.html'
    context_object_name = 'student_list'

    # def get_queryset(self):
        # self.current_page = int(self.request.GET.get('p', 1))
        # students = self.paginator.page(self.current_page)
        # return students
        # return Student.objects.order_by('-student_age')[:]
        # return Student.objects.filter(student_sex__contains='girl')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        page_data = self.get_page_data()
        context.update(page_data)
        return context

    def get_page_data(self):
        current_page = int(self.request.GET.get('p', 1))

        limit = 3
        students = Student.objects.all()
        paginator = Paginator(students, limit)
        students = paginator.page(current_page)

        page_num = paginator.num_pages
        page_list = []
        page_size = 10

        # 页数>=10
        if page_num >= page_size:
            if current_page <= page_size / 2:
                start_page = 1
            elif current_page > page_num - 5:
                start_page = page_num - 9
            else:
                start_page = current_page - 5

            for i in range(start_page, start_page + 10):
                page_list.append(i)
        else:
            for i in range(1, 11):
                page_list.append(i)

        page_data = {'page_num': page_num,
                     'pre_page': current_page - 1,
                     'next_page': current_page + 1,
                     'current_page': current_page,
                     'page_list': page_list,
                     'student_list': students}
        return page_data