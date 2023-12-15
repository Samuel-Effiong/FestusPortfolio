from django.db import models

from wagtail.models import Page


class HomePage(Page):
    page_description = "The Homepage of the whole website"

    def get_context(self, request):
        "Upload only published content to the home page"
        contextt = super().get_context(request)



class ArticlePage(Page):
    pass