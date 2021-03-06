from django.template import Library

register = Library()


@register.inclusion_tag('templatetags/tree_structure.html ')
def tree_structure(category):
    subs = category.subs.all()
    return {"subs": subs}
