from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import VideoContent
from .forms import CommentaryForm

class VideocontentView(ListView):
    model = VideoContent
    template_name = 'videocontents/videocontent_list.html'
    queryset = model.objects.all()


class VideocontentDetailView(DetailView):
    model = VideoContent
    template_name = 'videocontents/videocontent_detail.html'
    queryset = model.objects.all()


class AddCommentary(View):

    def post(self, request, pk):
        form = CommentaryForm(request.POST)
        videocontent = VideoContent.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.video = videocontent
            form.save()
        print(videocontent.get_absolute_url())
        return redirect(f"/{videocontent.get_absolute_url()}")
