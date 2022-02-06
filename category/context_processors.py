from .models import Category

def menu_links(req):
    links = Category.objects.all().order_by('category_name')
    return dict(links=links)
