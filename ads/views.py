from ads.models import Ad
from ads.owner import (
    OwnerListView,
    OwnerDetailView,
    OwnerCreateView,
    OwnerUpdateView,
    OwnerDeleteView,
)


class AdListView(OwnerListView):
    model = Ad
    template_name = "ads/ad_list.html"


# class ArticleDetailView(OwnerDetailView):
#     model = Article

# class ArticleCreateView(OwnerCreateView):
#     model = Article
#     # List the fields to copy from the Article model to the Article form
#     fields = ['title', 'text']

# class ArticleUpdateView(OwnerUpdateView):
#     model = Article
#     fields = ['title', 'text']
#     # This would make more sense
#     # fields_exclude = ['owner', 'created_at', 'updated_at']


# class ArticleDeleteView(OwnerDeleteView):
#     model = Article
