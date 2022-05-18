from django.shortcuts import render, redirect
from .models import Cafe, Table
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
import json


@login_required
def view_create_cafe(request):
    if not request.user.is_staff:
        #? if a regular user tries to access this page, make it unaccessible 
        messages.add_message(request, level=messages.INFO, message="You aren't allowed to create a centre.")
        return redirect("home")

    if request.method == "POST":
        if request.FILES:
            image = request.FILES.get('image')
            cafe_name = request.POST.get('cafe_name')

            #? Creating Cafe object
            cafe = Cafe.objects.get(name=cafe_name)
            cafe.image = image
            cafe.save()

            messages.add_message(request, level=messages.INFO, message="Colors saved!")

            return redirect('home')

        for i in request:
            #? Get tables positions and information from JSON
            data = json.loads(i)
            tables_distance_top = list(data['array_distance_top'])
            tables_distance_left = list(data['array_distance_left'])
            tables_label = list(data['array_labels'])
            tables_numbers = list(range(len(tables_label)))
            cafe_name = data['cafe_name']

            print(tables_label)

            cafe = Cafe.objects.create(name=cafe_name)
            cafe.save()

            for table_number, table_distance_top, \
                table_distance_left, table_label in zip(
                                                        tables_numbers,
                                                        tables_distance_top,
                                                        tables_distance_left,
                                                        tables_label):
                table = Table.objects.create(table_number=table_number, 
                                    top=table_distance_top,
                                    left=table_distance_left,
                                    label=table_label,
                                    cafe=cafe)
                table.save()
            
            break
    return render(request, 'cafe/create-cafe.html')
    

def view_detail_cafe(request, pk):
    cafe = Cafe.objects.get(pk=pk)    
    tables = cafe.tables.all()
    context = {'cafe': cafe, 'tables': tables, 'title': 'Detail Cafe'}
    if request.method == 'POST':
        data_dictionary = request.POST.dict()
        data_dictionary.pop('csrfmiddlewaretoken')
        for table_number, table_color in data_dictionary.items():
            table = cafe.tables.get(table_number=table_number)
            table.color = table_color
            table.save()
        messages.add_message(request, level=messages.INFO, message="Colors saved!")
        
    return render(request, "cafe/detail-cafe.html", context=context)


def view_home(request):
    cafes = Cafe.objects.all()
    context = {'cafes': cafes, 'title': 'Home'}
    return render(request, "cafe/list-cafe.html", context=context)


@login_required
def view_delete_cafe(request, pk):
    if not request.user.is_staff:
        messages.add_message(request, level=messages.ERROR, message="You don't have permission to delete!")
        return redirect('home')
    if request.method == "POST":
        cafe = Cafe.objects.get(pk=pk)    
        cafe.delete()
        return redirect('home')
    cafe = Cafe.objects.get(pk=pk)
    return render(request, 'cafe/delete-cafe.html', context={'cafe': cafe})


@login_required
def view_update_cafe(request, pk):
    if request.method == "POST":
        if request.FILES:

            image = request.FILES.get('image')
            cafe_name = request.POST.get('cafe_name')

            #? Creating Cafe object
            cafe = Cafe.objects.get(pk=pk)
            cafe.image = image
            cafe.name = cafe_name
            cafe.save()

        for i in list(request):
            #? Get tables positions and information from JSON
            data = json.loads(i)
            tables_distance_top = list(data['array_distance_top'])
            tables_distance_left = list(data['array_distance_left'])
            tables_label = list(data['array_labels'])
            tables_numbers = list(range(len(tables_label)))
            cafe_name = data['cafe_name']

            print(tables_numbers, tables_distance_top, tables_distance_left, cafe_name)
            print(tables_label)

            cafe = Cafe.objects.get(pk=pk)


            for table_number, table_distance_top, \
                table_distance_left, table_label in zip(
                                                    tables_numbers,
                                                    tables_distance_top,
                                                    tables_distance_left,
                                                    tables_label):
                table, created = cafe.tables.get_or_create(table_number=table_number)

                table.top = table_distance_top
                table.left = table_distance_left
                table.label = table_label
                table.cafe = cafe

                table.save()
            break

    cafe = Cafe.objects.get(pk=pk)    
    tables = cafe.tables.all()
    context = {'cafe': cafe, 'tables': tables, 'title': 'Detail Cafe'}

    return render(request, 'cafe/update-cafe.html', context=context)
    