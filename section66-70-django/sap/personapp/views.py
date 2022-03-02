from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from personapp.models import Person
from django.views.decorators.csrf import csrf_exempt
from personapp.forms import PersonForm

# Create your views here.

# SELECT
def select_person(request, id):
    person = get_object_or_404(Person, pk=id)
    return render(request, 'person/select.html', { 'person': person })

# INSERT
# FormPerson = modelform_factory(Person, exclude=[])
@csrf_exempt
def insert_person(request):
    if request.method == 'POST':
        form_person = PersonForm(request.POST)
        if form_person.is_valid():
            form_person.save()
            return redirect('index')
    else:
        form_person = PersonForm()
    return render(request, 'person/insert.html',{ 'form_person': form_person})

# UPDATE
@csrf_exempt
def update_person(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == 'POST':
        form_person = PersonForm(request.POST, instance=person)
        if form_person.is_valid():
            form_person.save()
            return redirect('index')
    else:
        form_person = PersonForm(instance=person)
    return render(request, 'person/update.html',{ 'form_person': form_person, 'person': person })


# DELETE
@csrf_exempt
def delete_person(request, id):
    person = get_object_or_404(Person, pk=id)
    if person:
        person.delete()
    return redirect('index')
