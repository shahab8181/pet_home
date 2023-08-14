from django.shortcuts import render
from django.views.generic.base import TemplateView
from site_module.models import SiteSetting
from account_module.models import User
from django.db.models import Q

# Create your views here.

class AboutUsView(TemplateView):
    template_name = r'aboutus_module/about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SiteSetting.objects.get(is_main_setting=True)
        context['admin'] = User.objects.get(user_group=User.UserGroup.admin)
        context['users'] = User.objects.filter(
            Q(user_group=User.UserGroup.admin) | 
            Q(user_group=User.UserGroup.programmer) | 
            Q(user_group=User.UserGroup.graphic_designer) | 
            Q(user_group=User.UserGroup.SEO)
        ).order_by('user_group')
        return context