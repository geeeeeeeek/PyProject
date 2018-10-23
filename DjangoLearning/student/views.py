from .models import *
from django.views import generic
from django.core.paginator import Paginator

class IndexView(generic.ListView):
    model = Student
    template_name = 'student/index.html'
    context_object_name = 'student_list'
    paginate_by = 4

    # def get_queryset(self):
        # self.current_page = int(self.request.GET.get('p', 1))
        # students = self.paginator.page(self.current_page)
        # return students
        # return Student.objects.order_by('-student_age')[:]
        # return Student.objects.filter(student_sex__contains='girl')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        paginator = context.get('paginator')
        page = context.get('page_obj')
        page_data = self.get_page_data(paginator, page)
        context.update(page_data)
        return context


    @staticmethod
    def get_page_data(paginator, page):

        page_list = []

        # ==============分页逻辑===============
        # 条件：页数>=10
        # 当前页<=5时，起始页为1
        # 当前页>(总页数-5)时，起始页为(总页数-9)
        # 其他情况 起始页为(当前页-5)
        # ====================================

        if paginator.num_pages > 10:
            if page.number <= 5:
                start_page = 1
            elif page.number > paginator.num_pages - 5:
                start_page = paginator.num_pages - 9
            else:
                start_page = page.number - 5

            for i in range(start_page, start_page + 10):
                page_list.append(i)
        else:
            for i in range(1, paginator.num_pages + 1):
                page_list.append(i)

        page_data = {'page_list': page_list}
        return page_data


class DetailView(generic.DetailView):
    model = Student
    template_name = 'student/detail.html'
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        comment_list = self.object.comment_set.all()
        context.update({
            'comment_list': comment_list
        })
        return context