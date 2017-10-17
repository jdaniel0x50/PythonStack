# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import Item
from models import Purchase_Order
from models import Purchase_Line_Item
from django.db.models import Count, Min, Sum, Avg

def store_home(request):
    if 'purchase_item' in request.session:
        del request.session['purchase_item']
    context = {"items": Item.objects.all()}
    return render(request, "amadon/home.html", context)

def create_item(request):
    context = {"items": Item.objects.all()}
    return render(request, "amadon/create_item.html", context)

def create_submit(request):
    item_name = request.POST['item']
    item_price = request.POST['price']
    if item_name and item_price:
        new_item = Item(item=item_name, price=item_price)
        new_item.save()
    return redirect('/amadon/create_item')

def delete_items(request):
    for item in Item.objects.all():
        item.delete()
    return redirect('/amadon/create_item')

def checkout(request):
    if not len(request.POST['name']) > 0:
        return redirect('/amadon/home')
    name = request.POST['name']
    # request.session['purchase_item'] = []
    is_item_quantity = False
    for item in Item.objects.all():
        if int(request.POST["quantity_" + str(item.id)]) > 0:
            item_order = {
                'item_id': str(item.id),
                'item_name': str(item.item),
                'item_price': str(item.price),
                'item_qty': str(request.POST["quantity_" + str(item.id)])
            }
            if not 'purchase_item' in request.session:
                request.session['purchase_item'] = []
                request.session['purchase_item'] = [item_order]
            else:
                order_list = request.session['purchase_item']
                order_list.append(item_order)
                # request.session['purchase_item'].append(item_order)
                request.session['purchase_item'] = order_list
            is_item_quantity = True
            print request.session['purchase_item']

    if is_item_quantity:
        new_purchase = Purchase_Order(customer_name = name)
        new_purchase.save()
        for item in request.session['purchase_item']:
            new_purchase_line = Purchase_Line_Item(related_purchase_order = new_purchase, item_to_purchase = Item.objects.get(id=item['item_id']), quantity_to_purchase = item['item_qty'])
            new_purchase_line.save()
    return redirect('/amadon/order_confirmation')

def confirmation(request):
    purchase_totals = {}
    for purchase in Purchase_Order.objects.all():
        purchase_totals[purchase.id] = Purchase_Line_Item.objects.filter(related_purchase_order__id=purchase.id).aggregate(total_price=Sum('item_to_purchase__price'))
    context = {
        "purchases": Purchase_Order.objects.all(),
        "purchase_lines": Purchase_Line_Item.objects.all(),
        "purchase_totals": purchase_totals
        }
    return render(request, "amadon/order_confirmation.html", context)

    # return redirect('/amadon/home')
