
from django.views.generic import ListView, DetailView
from .models import Ad, Category
from django.db.models import Q


class AdListView(ListView):
    model = Ad
    template_name = 'board/ad_list.html'
    context_object_name = 'ads'
    paginate_by = 10

    def get_queryset(self):
        queryset = Ad.objects.select_related(
            'category', 'user').filter(is_active=True)
        category = self.request.GET.get('category')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        ordering = self.request.GET.get('ordering')
        search = self.request.GET.get('search')

        if category:
            queryset = queryset.filter(category__id=category)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if search:
            queryset = queryset.filter(title__icontains=search)
        if ordering in ['price', '-price', 'created_at', '-created_at']:
            queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category', '')
        context['min_price'] = self.request.GET.get('min_price', '')
        context['max_price'] = self.request.GET.get('max_price', '')
        context['ordering'] = self.request.GET.get('ordering', '')
        context['search'] = self.request.GET.get('search', '')
        return context


class AdDetailView(DetailView):
    model = Ad
    template_name = 'board/ad_detail.html'
    context_object_name = 'ad'
