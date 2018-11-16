from django.contrib import admin
from .models import Subject, Section, Post, Comment, Threshold, Career, CareerSubjectSection, Student, Thread, ThreadRanking, ThreadFollower, PostFollower, PostRanking, CommentArchive, CommentRanking


admin.site.register(Section)
admin.site.register(Post)
admin.site.register(Subject)
admin.site.register(Comment)
admin.site.register(Threshold)
admin.site.register(Career)
admin.site.register(CareerSubjectSection)
admin.site.register(Student)
admin.site.register(Thread)
admin.site.register(ThreadRanking)
admin.site.register(ThreadFollower)
admin.site.register(PostFollower)
admin.site.register(PostRanking)
admin.site.register(CommentArchive)
admin.site.register(CommentRanking)
# Register your models here.
