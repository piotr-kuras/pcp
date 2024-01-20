from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from .models import Product, Price, Shop
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from django.db.models import Min
from django.db.models.functions import TruncDay


class HomePageView(TemplateView):
    template_name = "home.html"


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product_list.html"
    success_url = reverse_lazy("product_list")


class ProductDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        shops = Shop.objects.filter(product=product)
        prices = []
        for shop in shops:
            lowest_price = Price.objects.filter(shop=shop).order_by('price').first()
            if lowest_price:
                prices.append(lowest_price)
        data = {
            'Shop': [price.shop.name for price in prices],
            'Lowest Price': [float(price.price) for price in prices],
        }

        df = pd.DataFrame(data)
        fig = px.bar(df, x='Shop', y='Lowest Price', text='Lowest Price',
                     labels={'Lowest Price': 'Najniższa cena'},
                     title='Historcznie najniższa cena produktu z podziałem na sklep')
        lowest_price_plot = plot(fig, output_type="div")
        context.update({'plot_lowest_price_div': lowest_price_plot})

        prices = Price.objects.filter(shop__in=shops).annotate(day=TruncDay('date')).values('day').annotate(
            min_price=Min('price'))

        data = {
            'Day': [price['day'] for price in prices],
            'Lowest Price': [float(price['min_price']) for price in prices],
        }

        df = pd.DataFrame(data)
        fig = px.line(df, x='Day', y='Lowest Price', text='Lowest Price',
                      labels={'Lowest Price': 'Najniższa cena'},
                      title='Najniższe ceny dla danego produktu danego dnia')
        fig.update_traces(textfont=dict(size=16))
        lowest_price_daily_plot = plot(fig, output_type="div")
        context.update({'plot_lowest_price_daily_div': lowest_price_daily_plot})

        context['shops'] = sorted(shops, key=lambda shop: shop.get_price())

        return context

    def test_func(self):
        obj = self.get_object()
        return obj.added_by == self.request.user


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "product_new.html"
    fields = (
        "name",
        "url",
    )

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = (
        "name",
    )
    template_name = "product_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.added_by == self.request.user


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "product_delete.html"
    success_url = reverse_lazy("product_list")

    def test_func(self):
        obj = self.get_object()
        return obj.added_by == self.request.user
