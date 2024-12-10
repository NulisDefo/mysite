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


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    fields_exclude = ["owner", "created_at", "updated_at"]


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields_exclude = ["owner", "created_at", "updated_at"]


class AdDeleteView(OwnerDeleteView):
    model = Ad
