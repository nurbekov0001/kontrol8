from urllib.parse import urlencode

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import ProductForm, SearchForm, ReviewForm
from webapp.models import Product, Review
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView



class ProductList(ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'product'
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(ProductList, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class ProductCreate(PermissionRequiredMixin, CreateView):
    template_name = 'review/create.html'
    model = Product
    form_class = ProductForm
    permission_required = 'webapp.add_product'


    def get_success_url(self):
        return reverse('product:view', kwargs={'pk': self.object.pk})


class ReviewCreate(PermissionRequiredMixin, CreateView):
    model = Review
    template_name = 'review/create.html'
    form_class = ReviewForm
    permission_required = 'webapp.add_review'

    def form_valid(self, form):
        review = get_object_or_404(Review, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.review = review
        choice.save()
        form.save_m2m()
        return redirect('product:view', pk=review.pk)

    def has_permission(self):
        return super().has_permission() and self.request.user in Product.objects.get(
            pk=self.kwargs.get('pk')).user.all()



class ProductView(DetailView):
    model = Product
    template_name = 'product/view.html'
    context_object_name = 'product'



class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm
    context_object_name = 'product'
    permission_required = 'webapp.change_product'



    def get_success_url(self):
        return reverse('product:view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product/delete.html'
    model = Product
    context_object_name = 'product'
    permission_required = 'webapp.delete_product'
    success_url = reverse_lazy('product:list')


