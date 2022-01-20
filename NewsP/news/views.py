from django.views.generic import ListView, DetailView
    # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
     # импортируем класс получения деталей объекта
from .models import Author, Category, Post, PostCategory, Comment
from datetime import datetime

class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'allposts.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        #context['value1'] = None   добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        #context['countposts'] = 'posts|length'
        return context

class PostList1(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-dateCreation')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()  # добавим переменную текущей даты time_now
        #context['value1'] = None   добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        #context['countposts'] = 'posts|length'
        return context

# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post.html'  # название шаблона будет product.html
    context_object_name = 'post'  # название объекта. в нём будет
    #postCategoryset = post.postCategory.all()
    #postCategoryset = Post.objects.get(id = 'Post.id').postCategory.all()
    #Post.objects.get(id=3).postCategory.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        #context['value1'] = None   добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        #context['countposts'] = 'posts|length'
        #context['postCategoryset'] = Post.objects.get(id=id).postCategory.all()

        return context