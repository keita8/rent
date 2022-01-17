from .models import Social

def social_links(request):
    media_social = Social.objects.first()
    return dict(media_social=media_social)