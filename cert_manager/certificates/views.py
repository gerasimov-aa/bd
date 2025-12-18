from django.shortcuts import render, redirect
from django.db.models import Q
from django.utils import timezone
from .models import CertificateExpiry, CertificateUser
from .forms import CertificateExpiryForm, CertificateUserForm, CertificateExpiryFilterForm, CertificateUserFilterForm



def home(request):
    return render(request, 'certificates/home.html')


def certificate_expiry_list(request):
    # Обработка формы добавления
    if request.method == 'POST':
        if 'add' in request.POST:
            form = CertificateExpiryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('certificate_expiry_list')
        elif 'delete' in request.POST:
            selected_ids = request.POST.getlist('selected')
            CertificateExpiry.objects.filter(id__in=selected_ids).delete()
            return redirect('certificate_expiry_list')
    else:
        form = CertificateExpiryForm()

    # Фильтрация
    filter_form = CertificateExpiryFilterForm(request.GET)
    expiries = CertificateExpiry.objects.all()
    if filter_form.is_valid():
        full_name = filter_form.cleaned_data.get('full_name')
        department = filter_form.cleaned_data.get('department')
        expiry_date_from = filter_form.cleaned_data.get('expiry_date_from')
        expiry_date_to = filter_form.cleaned_data.get('expiry_date_to')
        if full_name:
            expiries = expiries.filter(full_name__icontains=full_name)
        if department:
            expiries = expiries.filter(department__icontains=department)
        if expiry_date_from:
            expiries = expiries.filter(expiry_date__gte=expiry_date_from)
        if expiry_date_to:
            expiries = expiries.filter(expiry_date__lte=expiry_date_to)

    # Сортировка
    sort_by = request.GET.get('sort', 'full_name')
    if sort_by.startswith('-'):
        direction = 'desc'
        sort_field = sort_by[1:]
    else:
        direction = 'asc'
        sort_field = sort_by
    expiries = expiries.order_by(sort_by)

    today = timezone.now().date()
    return render(request, 'certificates/certificate_expiry_list.html', {
        'expiries': expiries,
        'form': form,
        'filter_form': filter_form,
        'today': today,
        'sort_by': sort_by,
        'direction': direction,
        'sort_field': sort_field,
    })


def certificate_user_list(request):
    # Обработка формы добавления
    if request.method == 'POST':
        if 'add' in request.POST:
            form = CertificateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('certificate_user_list')
        elif 'delete' in request.POST:
            selected_ids = request.POST.getlist('selected')
            CertificateUser.objects.filter(id__in=selected_ids).delete()
            return redirect('certificate_user_list')
    else:
        form = CertificateUserForm()

    # Фильтрация
    filter_form = CertificateUserFilterForm(request.GET)
    users = CertificateUser.objects.all()
    if filter_form.is_valid():
        full_name = filter_form.cleaned_data.get('full_name')
        computer_number = filter_form.cleaned_data.get('computer_number')
        installed_certificate = filter_form.cleaned_data.get('installed_certificate')
        if full_name:
            users = users.filter(full_name__icontains=full_name)
        if computer_number:
            users = users.filter(computer_number__icontains=computer_number)
        if installed_certificate:
            users = users.filter(installed_certificate__icontains=installed_certificate)

    # Сортировка
    sort_by = request.GET.get('sort', 'full_name')
    if sort_by.startswith('-'):
        direction = 'desc'
        sort_field = sort_by[1:]
    else:
        direction = 'asc'
        sort_field = sort_by
    users = users.order_by(sort_by)

    return render(request, 'certificates/certificate_user_list.html', {
        'users': users,
        'form': form,
        'filter_form': filter_form,
        'sort_by': sort_by,
        'direction': direction,
        'sort_field': sort_field,
    })