from django import template
from retro.models import Student, Section

register = template.Library()

@register.filter
def PrivilegeCreateThread(request, sectionpk):
    print(request.user)
    if Student.objects.filter(student=request.user.userprofile, section_id=sectionpk).exists():
        return True
    if Section.objects.filter(pk=sectionpk, teacher=request.user.userprofile).exists():
        return True
    return False
