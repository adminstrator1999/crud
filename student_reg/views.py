from django.shortcuts import render, redirect
from .models import Table, University
from django.contrib.auth.decorators import login_required
from .forms import TableForm


def table(request):
    students = Table.objects.all()
    universities = University.objects.all()
    context = {'students': students,
               'universities': universities}
    return render(request, 'home.html', context)


def reg(request):
    universities = University.objects.all()
    context = {'universities': universities}
    return render(request, "creating_page.html", context)


@login_required
def add(request):
    st = Table()
    st.full_name = request.POST['fullName']
    st.university = University.objects.get(pk=request.POST['University'])
    st.phone = request.POST['phone']
    st.level = request.POST['lvl']
    st.owner = request.user
    Table.save(st)
    return redirect('table')


@login_required
def delete(request, id):
    Table.objects.filter(id=id).delete()
    return redirect('table')


def view(request, id):
    incs = Table.objects.get(id=id)
    return render(request, 'view.html', {'incs': incs})


@login_required
def edit(request, id):
    universities = University.objects.all()
    editor = Table.objects.get(id=id)
    context = {'editor': editor,
               'universities': universities}
    return render(request, 'edit.html', context)


def edition(request):
    st = Table()
    st.id = request.POST['id']
    st.full_name = request.POST['fn']
    st.owner = request.user
    st.university = University.objects.get(pk=request.POST['University'])
    st.phone = request.POST['pe']
    st.level = request.POST['ll']
    Table.save(st)
    return redirect('table')


def search(request):
    item = request.POST["fullName"]
    universities = University.objects.all()
    if request.POST['chosen_university'] == '%':
        students = Table.objects.filter(full_name__contains=item)
    else:
        students = Table.objects.filter(full_name__contains=item, university_id=request.POST['chosen_university'])
    context = {'students': students,
               'universities': universities}
    return render(request, 'home.html', context)


def university(request):
    universities = University.objects.all()
    context = {'universities': universities}
    return render(request, 'university.html', context)


def add_university_page(request):
    return render(request, 'adding_university.html')


def add_university(request):
    new_one = University()
    new_one.name = request.POST['new_university']
    University.save(new_one)
    return redirect('university')


def tabl(request):
    form = TableForm()
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table')
    context = {'form': form}
    return render(request, 'another_form.html', context)


def update_student(request, pk):
    student = Table.objects.get(id=pk)
    form = TableForm(instance=student)
    if request.method == 'POST':
        form = TableForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('table')
    context = {'form': form}
    return render(request, 'another_form.html', context)
