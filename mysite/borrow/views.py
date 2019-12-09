from datetime import date, timedelta, datetime

from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from django.utils.translation import gettext as _
from django.shortcuts import render, HttpResponseRedirect, redirect

from .models import Borrow, Borrow_Item, Reserve, Tab
from item.models import Item

def add_cart(request):
    username = None
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)

        if 'item' in request.POST:
            print(request.POST)
            addcart = request.POST['addcart']
            items = request.POST.getlist('item')
            #check user choose reserve or borrow
            if addcart == 'reserve':
                if request.POST['borrow_date'] == '':
                    messages.success(request, _('กรุณาเลือกวันที่ต้องการจองพัสดุ'))
                    return redirect('/item')
                for it in items:
                    it_id = int(it)
                    item = Item.objects.get(id=it_id)
                    if item.reserve_status == '02':
                        messages.success(request, _('พัสดุที่เลือกถูกจองแล้ว'))
                        return redirect('/item')
                borrow = Borrow.objects.filter(student_id=user.id, status='00')
                borrow_date = request.POST['borrow_date']
                #user have reserve-cart, then add just new item to reserve-cart
                if borrow:
                    print('have reserve-cart')
                    for br in borrow:
                        borrow = Borrow.objects.get(id=br.id)
                        break
                    borrow.borrow_date = borrow_date
                    borrow.save()
                    for it in items:
                        it_id = int(it)
                        item_id = Item.objects.get(id=it_id)
                        count = 0
                        borrow_item = Borrow_Item.objects.filter(borrow_id=br.id)
                        for brit in borrow_item:
                            print('add item: ', item_id.item_name)
                            if item_id.id == brit.item_id.id:
                                print('count')
                                count = count+1
                                print(item_id.id, '=', brit.item_id.id, 'break loop')
                                break
                        if count == 0:
                            borrow_item = Borrow_Item(id=None, borrow_id=borrow, item_id=item_id)
                            borrow_item.save()
                            reserve = Reserve(borrow_item_id=borrow_item, borrow_id=borrow, item_id=item_id)
                            reserve.save()
                #user do not have reserve-cart, then create new reserve-cart
                else:
                    print('do not have reserve-cart')
                    borrow = Borrow.objects.create(status='00', student_id=user, borrow_date=borrow_date)
                    for it in items:
                        it_id = int(it)
                        item_id = Item.objects.get(id=it_id)
                        borrow_item = Borrow_Item(id=None, borrow_id=borrow, item_id=item_id)
                        borrow_item.save()
                        reserve = Reserve(borrow_item_id=borrow_item, borrow_id=borrow, item_id=item_id)
                        reserve.save()
                print('go to reserve date')
                return HttpResponseRedirect('/borrow/reserve_date/%d' % (borrow.id))
            else:
                print('borrow')
                borrow = Borrow.objects.filter(student_id=user.id, status='01')

                if borrow:
                    for br in borrow:
                        borrow = Borrow.objects.get(id=br.id)
                        break
                    try:
                        for it in items:
                            it_id = int(it)
                            item_id = Item.objects.get(id=it_id)
                            print('pass 1')
                            count = 0
                            borrow_item = Borrow_Item.objects.filter(borrow_id=borrow)
                            print('brit0')
                            for brit in borrow_item:
                                print('brit1')
                                if item_id.id == brit.item_id.id:  # if item has been in cart
                                    count = count + 1
                                    break
                                    print('pass 2')
                            if count == 0:
                                borrow_item = Borrow_Item(id=None, borrow_id=borrow, item_id=item_id)
                                borrow_item.save()
                                print('pass 3')
                    except:
                        print('error')
                        return HttpResponseRedirect('/borrow/cart')
                else:
                    borrow = Borrow.objects.create(status='01', student_id=user)

                    for it in items:
                        it_id = int(it)
                        item_id = Item.objects.get(id=it_id)
                        borrow_item = Borrow_Item(id=None, borrow_id=borrow, item_id=item_id)
                        borrow_item.save()
                        print("borrow_id:", borrow.id, "saved")
                        if addcart == 'reserve':
                            reserve = Reserve(borrow_item_id=borrow_item, borrow_id=borrow.id, item_id=item_id)
                            reserve.save()

                return HttpResponseRedirect('/borrow/cart')
        else:
            print(request.POST)
            messages.success(request, _('เลือกร้านด้วยจ้าาาาาาาาาาาาาาาาาาาาาาาาาาาาาา'))
            return redirect('/item')
