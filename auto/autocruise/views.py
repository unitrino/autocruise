from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import xlwt

from models import CruiseData


def add_new(request):
    if request.POST:
        data = request.POST["data"]
        empty = ''
        from_place = request.POST["city"]
        full_name = request.POST["full_name"]
        numb = request.POST["numb"]
        tel = request.POST["tel"]
        to_place = request.POST["to"]
        note = request.POST["note"]
        CruiseData(data = data,empty = empty, from_place = from_place,full_name = full_name,numb = numb,tel = tel,to_place = to_place,note = note).save()
        return render(request,'html/form.html',{'add_success':1})
    elif request.GET:
        return render(request,'html/form.html',{'add_success':0})
    else:
        return render(request,'html/form.html',{'add_success':0})


def index(request):
    if request.session.get('logged_in','is_incorrect') == 'true':
        out = []
        for db_object in CruiseData.objects.all():
            out.append([db_object.data,db_object.empty,db_object.from_place,db_object.full_name,db_object.numb,db_object.tel,db_object.to_place,db_object.note])

        return render(request,'html/index.html',{'data_from_db':out[1:]})
    else:
        return HttpResponse("ERROR")

def generate_xls(request):
    if request.session.get('logged_in','is_incorrect') == 'true':
        wb = xlwt.Workbook()

        out = []
        for db_object in CruiseData.objects.all().order_by('data'):
            out.append([db_object.id,db_object.data,db_object.empty,db_object.from_place,db_object.full_name,db_object.numb,db_object.tel,db_object.to_place,db_object.note])

        work_sheets_groups = dict()
        for i in out:
            if i[3] not in work_sheets_groups:
                work_sheets_groups[i[3]] = [i[0]]
            else:
                work_sheets_groups[i[3]].append(i[0])

        for i in work_sheets_groups:
            ids = work_sheets_groups[i]
            ws = wb.add_sheet(i)
            row_numb = 0
            for j in ids:
                for elem in out:
                    if elem[0] == j:
                        ws.write(row_numb, 0, elem[1])
                        ws.write(row_numb, 1, elem[2])
                        ws.write(row_numb, 2, elem[3])
                        ws.write(row_numb, 3, elem[4])
                        ws.write(row_numb, 4, elem[5])
                        ws.write(row_numb, 5, elem[6])
                        ws.write(row_numb, 6, elem[7])
                        ws.write(row_numb, 7, elem[8])
                        row_numb += 1

        filename = "example.xls"
        wb.save(filename)
        response = HttpResponse(open(filename,'rb'), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        return response
    else:
        return HttpResponse("NOT LOGGED IN")


def logged_in(request):
    if request.POST:
        passwrd = request.POST["password"]
        if passwrd == "12345":
            request.session['logged_in'] = 'true'
            request.session.set_expiry(0)
            return  HttpResponseRedirect(reverse('index'))
        else:
             return render(request,'html/login.html', {'errors': 'Password incorrect'})
    else:
        return render(request,'html/login.html', {'errors': ''})

