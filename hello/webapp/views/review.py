from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView

from webapp.forms import ReviewForm
from webapp.models import Review


class ReviewCreate(CreateView):
    model = Review
    template_name = 'review/create.html'
    form_class = ReviewForm

    def form_valid(self, form):
        review = get_object_or_404(Review, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.review = review
        choice.save()
        form.save_m2m()
        return redirect('review_view', pk=review.pk)




class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'review/update.html'
    form_class =ReviewForm
    context_object_name = 'review'

    def get_success_url(self):
        return reverse('review_view', kwargs={'pk': self.object.pk})


class ReviewDeleteView(DeleteView):

    template_name = 'review/delete.html'
    model = Review
    context_object_name = 'review'
    success_url = reverse_lazy('review_list')



