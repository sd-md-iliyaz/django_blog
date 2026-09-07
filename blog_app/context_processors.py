from .models import Category,SocialLink


def get_category(request):
    categories=Category.objects.all()
    return dict(categories=categories)

def get_sociallinks(request):
    social_link=SocialLink.objects.all()
    return dict(social_link=social_link)