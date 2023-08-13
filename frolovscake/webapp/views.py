from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Menu, Dish, Sales
from django.views.generic import TemplateView, ListView
import json
from django.shortcuts import get_object_or_404, get_list_or_404

class View(TemplateView):
    
     

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['menu'] = json.dumps(
            [
                {
                    'menu_id': obj.m_id,
                    'dish_id': obj.dish_id,
                    'price': obj.price,
                    'sale_id': obj.sale
                }
                for obj in Menu.objects.all()
            ]
        )

        context['dish'] = json.dumps(
            [
                {
                    'dish_id': obj.d_id,
                    'dish_name': obj.dish_name,
                    'desc': obj.dish_desc,
                    'photo': obj.dish_photo
                }
                for obj in Dish.objects.all()
            ]
        )
        context['sales'] = json.dumps(
            [
                {
                    'sale_id': obj.s_id,
                    'dish_id': obj.dish_id,
                    'sale': obj.sale,
                    
                }
                for obj in Sales.objects.all()
            ]
        )

        return context

class Menu_list(ListView):
    context_object_name = 'dishes'
    template_name='webapp/main.html'
    model = Menu

    def get_queryset(self):
       dishes_id= Menu.objects.all()
       dishes = []
       for i in dishes_id:
           find = Dish.objects.get(d_id=i.dish_id)
           sale = Sales.objects.filter(dish_id=i.dish_id).first()
           if sale is None:    
             dishes.append({'id':i.dish_id,'name':find.dish_name,'desc': find.dish_desc,
                            'photo':find.dish_photo, 'price': i.price, 'sale':None })
           else:
             dishes.append({'id':i.dish_id,'name':find.dish_name,'desc': find.dish_desc,
                            'photo':find.dish_photo, 'price': i.price, 'sale':sale.sale })  
       
       return dishes
       
    
