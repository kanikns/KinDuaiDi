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
            messages.success(request, _('กรุณาเลือกพัสดุ'))
            return redirect('/item')

def delete_cart(request, id):
    # for delete all item in cart
    borrow = Borrow.objects.get(id=id)
    borrow_item = Borrow_Item.objects.filter(borrow_id=id)
    reserve_item = Reserve.objects.filter(borrow_id=id)
    for reserve in reserve_item:
        reserve.delete()
    for brit in borrow_item:
        brit.delete()
    borrow.delete()
    return redirect('/item')

def delete_itemcart(request, id, item_id, slug):
    borrow = Borrow.objects.get(id=id)
    borrow_item = Borrow_Item.objects.filter(borrow_id=id, item_id=item_id)
    reserve_item = Reserve.objects.filter(borrow_id=id, item_id=item_id)
    reserve_item.delete()
    borrow_item.delete()
    count_brit = Borrow_Item.objects.filter(borrow_id=id).count()
    count_rsit = Reserve.objects.filter(borrow_id=id).count()
    if count_brit == 0:
        borrow.delete()
        return redirect('/item')
    if slug == 'reserve':
        return HttpResponseRedirect('/borrow/reserve_check')
    else:
        return redirect('/borrow/cart')

def cart(request):
    if not request.user.is_authenticated:
        return redirect('/')
    user = User.objects.get(username=request.user.username)
    borrow = Borrow.objects.filter(student_id=user.id, status='01')
    br = None
    for b in borrow:
        print('borrowid: ', b.id)
        br = Borrow.objects.get(id=b)
    if borrow:
        for br in borrow:
            borrow = Borrow.objects.get(id=br.id)
            break
        borrow_item = Borrow_Item.objects.filter(borrow_id=br.id)
    else:
        message = 'ไม่มีพัสดุที่เลือก'
        return render(request, 'borrow/cart.html', {'message': message})
    item = Item.objects.all()
    print('borrow.id', borrow.id)
    status = '0'
    rt_status = '0'
    if request.POST:
        print('request: ', request.POST)
        return_date = request.POST['return_date']
        rd = return_date.split('-')
        return_date = date(int(rd[0]),int(rd[1]),int(rd[2]))
        current_date = date.today()
        diff = return_date - current_date
        if diff.days > 5 or diff.days < 0: #check invalid diff day
            rt_status = '01'

        for brit in borrow_item:
            name = 'borrow_amount' + str(brit.item_id)
            borrow_amount = request.POST.get(name)
            try:
                if (int(borrow_amount) > brit.item_id.current_amount) or (int(borrow_amount) <= 0):
                    status = '01'
                else:
                    pass
            except:
                messages.success(request, _('ไม่มีพัสดุที่สามารถยืมได้'))
                print(messages)
                return redirect('/borrow/cart')

        if status == '0' and rt_status == '0':
            borrow.status = '02'
            borrow.request_date = date.today()
            borrow.request_time = datetime.now().time().strftime("%H:%M:%S")
            borrow.return_date = return_date
            borrow.save()
            count=0
            for brit in borrow_item:
                name = 'borrow_amount' + str(brit.item_id)
                borrow_amount = request.POST.get(name)
                print('borrow_item_id: ', brit.id)
                brit.borrow_amount = borrow_amount
                brit.save()
                count = count + 1
            if count == 0:
                borrow.delete()
            return redirect('/borrow/history/02')

    context = {
        'borrow': borrow,
        'borrow_item': borrow_item,
        'item': item,
        'status': status,
        'rt_status': rt_status,
        'br': br,
    }
    return render(request, 'borrow/cart.html', context)

def reserve_check(request):
    print('reserve check')
    if not request.user.is_authenticated:
        return redirect('/')
    user = User.objects.get(username=request.user.username)
    borrow = Borrow.objects.filter(student_id=user.id, status='00')
    for br in borrow:
        borrow = Borrow.objects.get(id=br.id)
        break
    if not borrow:
        return redirect('/borrow/reserve')
    return HttpResponseRedirect('/borrow/reserve_date/%d' % (borrow.id))

def reserve_date(request, borrow_id):
    if not request.user.is_authenticated:
        return redirect('/')
    import datetime
    borrow = Borrow.objects.get(id=borrow_id)
    message = None
    borrow_all = Borrow.objects.exclude(id=borrow_id).filter(status='03')
    borrow_item = Borrow_Item.objects.filter(borrow_id=borrow_id)
    current_date = date.today()
    next_date = date.today() + datetime.timedelta(days=3)
    if borrow.borrow_date:
        if current_date <= borrow.borrow_date <= next_date:
            for brit in borrow_item:
                can_borrow = brit.item_id.current_amount
                for brw in borrow_all:
                    if brw.return_date < borrow.borrow_date:
                        #borrow date is requested from this user, return_date is requested from other user
                        #borrow date must more than return date in each borrow id, then will calculate can borrow amount
                        borrow_item2 = Borrow_Item.objects.filter(item_id=brit.item_id, borrow_id=brw.id).exclude(
                            id=brit.id)
                        # for b in brit2:
                        # print('brit id:', b.id, ' ยืมไป:', b.item_id, b.borrow_amount)
                        for brit2 in borrow_item2:
                            if brit.item_id == brit2.item_id:
                                can_borrow = can_borrow + brit2.borrow_amount
                reserve = Reserve.objects.get(borrow_item_id=brit.id)
                reserve.can_borrow = can_borrow
                reserve.save()
            return HttpResponseRedirect('/borrow/reserve')
        else:
            borrow.borrow_date = None
            borrow.save()
            messages.success(request, _('สามารถจองล่วงหน้าได้ไม่เกิน 3 วัน'))
            return redirect('/item')
    else:
        if request.POST:
            borrow_date = request.POST['borrow_date']
            print('brd ', borrow_date)
            brd = borrow_date.split('-')
            borrow_date = date(int(brd[0]), int(brd[1]), int(brd[2]))
            if current_date <= borrow_date <= next_date:
                for brit in borrow_item:
                    can_borrow = brit.item_id.current_amount
                    for brw in borrow_all:
                        if brw.return_date < borrow_date:
                        # borrow date must more than return date in each borrow id, then will calculate can borrow amount
                            borrow_item2 = Borrow_Item.objects.filter(item_id=brit.item_id, borrow_id=brw.id).exclude(id=brit.id)
                            # for b in brit2:
                            #     print('brit id:', b.id, ' ยืมไป:', b.item_id, b.borrow_amount)
                            for brit2 in borrow_item2:
                                if brit.item_id == brit2.item_id:
                                    can_borrow = can_borrow + brit2.borrow_amount
                    reserve = Reserve.objects.get(borrow_item_id = brit.id)
                    reserve.can_borrow = can_borrow
                    reserve.save()
                borrow.borrow_date = borrow_date
                borrow.save()
                return HttpResponseRedirect('/borrow/reserve')
            else:
                message = 'สามารถจองล่วงหน้าได้ไม่เกิน 3 วัน'
        print('message: ', message)
        return render(request, 'borrow/reserve_date.html', {'message':message})

def edit_reservedate(request):
    if not request.user.is_authenticated:
        return redirect('/')

    user = User.objects.get(username=request.user.username)
    borrow = Borrow.objects.filter(student_id=user.id, status='00')
    for br in borrow:
        borrow = Borrow.objects.get(id=br.id)
        break
    borrow.borrow_date = None
    borrow.save()
    return HttpResponseRedirect('/borrow/reserve_date/%d' % (borrow.id))

def reserve(request):
    if not request.user.is_authenticated:
        return redirect('/')
    user = User.objects.get(username=request.user.username)
    borrow = Borrow.objects.filter(student_id=user.id, status='00')
    if borrow:
        for br in borrow:
            borrow = Borrow.objects.get(id=br.id)
            break
        if not borrow.borrow_date:
            return redirect('reserve_check')
    else:
        message = 'ไม่มีพัสดุที่เลือก'
        return render(request, 'borrow/reserve.html', {'message': message})

    borrow_items = Borrow_Item.objects.filter(borrow_id=br.id)
    reserves = Reserve.objects.filter(borrow_id=br.id)
    rt_status = '0'
    status = '0'
    if request.POST:
        return_date = request.POST['return_date']
        rd = return_date.split('-')
        return_date = date(int(rd[0]), int(rd[1]), int(rd[2]))
        diff = return_date - borrow.borrow_date

        #check invalid amount input
        for reserve in reserves:
            name = 'borrow_amount' + str(reserve.item_id)
            borrow_amount = int(request.POST.get(name))
            if borrow_amount > reserve.can_borrow or borrow_amount <= 0:
                status = '01'
            if diff.days > 5 or diff.days < 0:
                rt_status = '01'

        if status == '0' and rt_status == '0':
            borrow.status = '07'
            borrow.request_date = date.today()
            borrow.request_time = datetime.now().time().strftime("%H:%M:%S")
            borrow.return_date = return_date
            borrow.save()
            count = 0

            for brit in borrow_items:
                name = 'borrow_amount' + str(brit.item_id)
                borrow_amount = request.POST.get(name)
                brit.borrow_amount = borrow_amount
                brit.save()
                count = count + 1
                item = Item.objects.get(id=brit.item_id.id)
                item.amount_forreserve = int(borrow_amount)
                item.reserve_status = '02'
                if item.current_amount >= item.amount_forreserve:
                    item.current_amount = item.current_amount - item.amount_forreserve
                    item.amount_forreserve = 0
                else:
                    item.amount_forreserve = item.amount_forreserve - item.current_amount
                    item.current_amount = 0
                item.save()
            if count == 0:
                borrow.delete()
            return redirect('/borrow/history/07')

    context = {
        'borrow': borrow,
        'borrow_items': borrow_items,
        'reserves': reserves,
        'rt_status': rt_status,
        'status': status
    }

    return render(request, 'borrow/reserve.html', context)

def admin_dashboard(request, status):
    if not request.user.is_authenticated:
        return redirect('/')
    if not request.user.is_staff:
        return redirect('/priv_error')
    borrow_list = None
    borrowitem_list = None
    list_count = 0
    if status == '02' or status == '07':
        borrow_list = Borrow.objects.filter(status=status).order_by('request_date')
        borrowitem_list = Borrow_Item.objects.all()
        list_count = Borrow.objects.filter(status=status).count()
    elif status == '03':
        borrow_list = Borrow.objects.filter(status=status).order_by('return_date')
        borrowitem_list = Borrow_Item.objects.all()
        list_count = Borrow.objects.filter(status=status).count()
    elif status == '06' or status == '04':
        borrow_list = Borrow.objects.filter(status=status).order_by('-takeback_date')
        borrowitem_list = Borrow_Item.objects.all()
        list_count = Borrow.objects.filter(status=status).count()
    elif status == '05':
        borrow_list = Borrow.objects.filter(status=status).order_by('-request_date')
        borrowitem_list = Borrow_Item.objects.all()
        list_count = Borrow.objects.filter(status=status).count()
    status = status
    tabs = Tab.objects.all()

    if 'username_contains' in request.GET:
        user_list = User.objects.all()
        query = None
        username_contains_query = request.GET['username_contains']
        firstname_contains_query = request.GET['firstname_contains']
        lastname_contains_query = request.GET.get('lastname_contains')
        if username_contains_query != '' and username_contains_query is not None:
            borrow_list = borrow_list.filter(student_id__username__icontains=username_contains_query)
            list_count = (borrow_list.filter(student_id__username__icontains=username_contains_query)).count()
            print('query username')
            query = 'not none'
        if firstname_contains_query != '' and firstname_contains_query is not None:
            borrow_list = borrow_list.filter(student_id__first_name__icontains=firstname_contains_query)
            list_count = borrow_list.filter(student_id__first_name__icontains=firstname_contains_query).count()
            print('query firstname')
            query = 'not none'
        if lastname_contains_query != '' and lastname_contains_query is not None:
            borrow_list = borrow_list.filter(student_id__last_name__icontains=lastname_contains_query)
            list_count = borrow_list.filter(student_id__last_name__icontains=lastname_contains_query).count()
            print('query lastname')
            query = 'not none'
    print('list count', list_count)
    context = {
        'borrow_list': borrow_list,
        'borrowitem_list': borrowitem_list,
        'list_count': list_count,
        'status': status,
        'tabs': tabs,
    }
    if request.POST:
        user = User.objects.get(username=request.user.username)
        borrows = Borrow.objects.exclude(status='01')
        for borrow in borrows:
            cf = 'confirm'
            confirm = request.POST.get(cf)

            if confirm == 'confirm' + str(borrow.id):
                borrowitems = Borrow_Item.objects.filter(borrow_id = borrow)
                check = 0
                for brit in borrowitems:
                    if brit.borrow_amount > brit.item_id.current_amount: #if item amount that user request is less than current item amount
                        check = 1 #user cannot borrow any item
                if check == 0:
                    for brit in borrowitems:
                        item = Item.objects.get(id = brit.item_id.id)
                        if borrow.status == '07':
                            item.reserve_status = '01'
                            item.amount_forreserve = 0
                        else:
                            item.current_amount = item.current_amount - brit.borrow_amount
                        item.save()
                        print('saved')
                    borrow.confirm_by = user
                    borrow.status = '03'
                    borrow.borrow_date = date.today()
                    borrow.save()
                    return redirect('/borrow/admin_dashboard/03')
                else:
                    messages.success(request, _('จำนวนพัสดุไม่เพียงพอ'))
                    return redirect('/borrow/admin_dashboard/02')


            elif confirm == 'cancel' + str(borrow.id):
                print('cancel: ', confirm)
                if borrow.status == '07':
                    reserves = Reserve.objects.filter(borrow_id=borrow)
                    for reserve in reserves:
                        item = Item.objects.get(id=reserve.item_id.id)
                        item.current_amount = item.current_amount + reserve.borrow_item_id.borrow_amount
                        item.reserve_status = '01'
                        item.amount_forreserve = 0
                        item.save()
                borrow.cancel_by = user
                borrow.status = '05'
                borrow.save()
                return redirect('/borrow/admin_dashboard/05')

            elif confirm == 'return' + str(borrow.id):
                print('return', confirm)
                print('defected or confirmed:', borrow.status)
                if borrow.status == '03':
                    current_date = date.today()
                    diff = current_date - borrow.return_date

                    if diff.days > 0:
                        borrow.fine = diff.days * 20
                borrowitems = Borrow_Item.objects.filter(borrow_id=borrow)
                for brit in borrowitems:
                    item = Item.objects.get(id=brit.item_id.id)
                    item.current_amount = item.current_amount + brit.borrow_amount
                    if item.reserve_status == '02':
                        if (item.amount_forreserve <= item.current_amount) and (item.amount_forreserve != 0):
                            item.current_amount = item.current_amount - item.amount_forreserve
                            item.amount_forreserve = 0
                            print('reserve at 1: ')

                        elif (item.amount_forreserve > item.current_amount) and (item.amount_forreserve != 0):
                            item.amount_forreserve = item.amount_forreserve - item.current_amount
                            item.current_amount = 0
                            print('reserve at 2: ')
                    item.save()
                    print('reserved ', item.amount_forreserve)
                    #
                    # # check reserve
                    # checkreserve = Borrow.objects.filter(status='07')
                    # if checkreserve:
                    #     for chk in checkreserve:
                    #         print(chk.id)
                    # else:
                    #     print('none')

                borrow.takeback_date = date.today()
                borrow.return_by = user
                borrow.status = '04'
                print(borrow.fine)
                borrow.save()

                return redirect('/borrow/admin_dashboard/04')

            elif confirm == 'defective' + str(borrow.id):
                borrow.status = '06'
                borrow.defective_by = user
                borrow.save()
                return redirect('/borrow/admin_dashboard/06')
    return render(request, 'borrow/admin_dashboard.html', context)

def history(request, status):
    print('borrow history')
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        user = request.user.id
    list_count = 0
    tabs = Tab.objects.all()
    borrow_list = None
    borrowitem_list = None
    if status == '02' or status == '07':
        borrow_list = Borrow.objects.filter(status=status).order_by('request_date')
        borrowitem_list = Borrow_Item.objects.all()
        list_count = Borrow.objects.filter(status=status).count()
    elif status == '03':
        borrow_list = Borrow.objects.filter(status=status).order_by('return_date')
        borrowitem_list = Borrow_Item.objects.all()
        list_count = Borrow.objects.filter(status=status).count()
    elif status == '06' or status == '04':
        borrow_list = Borrow.objects.filter(status=status).order_by('-takeback_date')
        borrowitem_list = Borrow_Item.objects.all()
        list_count = Borrow.objects.filter(status=status).count()
    elif status == '05':
        borrow_list = Borrow.objects.filter(status=status).order_by('-request_date')
        borrowitem_list = Borrow_Item.objects.all()
        list_count = Borrow.objects.filter(status=status).count()
    status = status
    if 'username_contains' in request.GET:
        user_list = User.objects.all()
        query = None
        username_contains_query = request.GET['username_contains']
        firstname_contains_query = request.GET['firstname_contains']
        lastname_contains_query = request.GET.get('lastname_contains')
        if username_contains_query != '' and username_contains_query is not None:
            borrow_list = borrow_list.filter(student_id__username__icontains=username_contains_query)
            list_count = (borrow_list.filter(student_id__username__icontains=username_contains_query)).count()
            query = 'not none'
        if firstname_contains_query != '' and firstname_contains_query is not None:
            user_list = user_list.filter(first_name__icontains=firstname_contains_query)
            query = 'not none'
        if lastname_contains_query != '' and lastname_contains_query is not None:
            user_list = user_list.filter(last_name__icontains=lastname_contains_query)
            query = 'not none'
    print('list count', list_count)
    bf = Borrow.objects.get(id=109)
    context = {
        'borrow_list': borrow_list,
        'borrowitem_list': borrowitem_list,
        'list_count': list_count,
        'status': status,
        'tabs': tabs,
    }

    return render(request, 'borrow/history.html', context)