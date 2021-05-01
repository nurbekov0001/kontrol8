from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView

from webapp.forms import ReviewForm
from webapp.models import Review, Product






class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'review/update.html'
    form_class =ReviewForm
    context_object_name = 'review'
    permission_required = 'webapp.change_review'


    def get_success_url(self):
        return reverse('review_view', kwargs={'pk': self.object.pk})


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):

    template_name = 'review/delete.html'
    model = Review
    context_object_name = 'review'
    permission_required = "webapp.delete_review"
    success_url = reverse_lazy('review_list')



