from datetime import datetime
from django.utils.timezone import utc
from django.views.generic import ListView, DetailView
from contact.forms import UserMessageForm
from partners.models import Partners
from .models import Blog


# init current time
current_timestamp = datetime.now().replace(tzinfo=utc)


class PostListViews(ListView):
    model = Blog
    queryset = Blog.objects.filter(publish=True, schedule_message__lte=current_timestamp)
    context_object_name = 'post'
    template_name = 'blog/blog-list.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserMessageForm()
        # partner context
        context['partners'] = Partners.objects.filter(publish=True)

        return context


class PostDetailViews(DetailView):
    model = Blog
    queryset = Blog.objects.filter(publish=True, schedule_message__lte=current_timestamp)
    context_object_name = 'post'
    template_name = 'blog/blog-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserMessageForm()
        # partner context
        context['partners'] = Partners.objects.filter(publish=True)
        return context
