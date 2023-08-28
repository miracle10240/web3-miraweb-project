from dateutil import parser
from datetime import datetime, timedelta
from django.shortcuts import render
from django.utils.timezone import utc
from django.views.generic import TemplateView
from contact.forms import UserMessageForm
from newsletters.forms import NewsletterEmailForm
from partners.models import Partners
from projects.models import Projects
from repository.models import RepoInfo
from .github_api import get_github_commits


# init current time
current_timestamp = datetime.now().replace(tzinfo=utc)


# index page view
class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = UserMessageForm()

        # get only the latest repo info
        latest_repo_info = RepoInfo.objects.order_by('-date_created')[0]

        # get commit from api
        get_commit_info = get_github_commits(latest_repo_info.active_repo)

        # format date
        datetime_obj = parser.parse(get_commit_info['last_commit_time'])

        # use current timezone
        datetime_obj = datetime_obj.replace(tzinfo=utc)

        # set last commit time
        get_commit_info['last_commit_time'] = datetime_obj

        # set context
        context['commit'] = get_commit_info
        context['repo'] = RepoInfo.objects.order_by('-date_created').all()[0]

        # partner context
        context['partners'] = Partners.objects.filter(publish=True)

        # project context; only get the latest
        context['project'] = Projects.objects.order_by('-date_created').filter(
            publish=True, schedule_message__lte=current_timestamp
        )[0]

        # newsletter form
        context['newsletter_form'] = NewsletterEmailForm()

        return context
