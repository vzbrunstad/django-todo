from django.shortcuts import render, redirect
from django.forms import ModelForm

from lists.models import List

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ['title', 'description']

# def get_book(book_id):
#   return Book.objects.get(id=book_id)

def list_list(request):
    lists = List.objects.all()
    data = {'all_lists': lists}
    return render(request, 'lists/list_list.html', data)

def list_create(request):
    form = ListForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lists:list_list')
    return render(request, 'lists/list_form.html', {'form': form, 'new_or_edit': 'New'})