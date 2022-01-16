from django import forms
from django.contrib import admin
from .models import VideoContent, Commentary, Subscription, Disregard, Like
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class VideoContentAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = VideoContent
        fields = '__all__'

@admin.register(VideoContent)
class VideoContentAdmin(admin.ModelAdmin):
    form = VideoContentAdminForm




admin.site.register(Commentary)
admin.site.register(Subscription)
admin.site.register(Disregard)
admin.site.register(Like)
