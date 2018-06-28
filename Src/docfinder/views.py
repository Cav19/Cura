from django.shortcuts import render
from django.http import HttpResponse
from .models import Preference, User, Doctor, Specialty, Insurance
import csv
import os
from django.conf import settings


def index(request):
    context = {'all_specialties': Specialty.objects.all()}
    return render(request, 'docfinder/index.html', context=context)


def submit(request):
    post = request.POST
    user = create_user_from_post_request(post)
    if not user:
        raise Exception("User could not be created.")
    create_preferences_with_user(user, post)
    return results(request, user)


def results(request, user=None):
    if not user:
        return render(request, 'docfinder/results.html', context={'doctor_list': Doctor.objects.all()})
    filtered_doctors = filter_doctors_by_user_preferences(Preference.objects.filter(user=user))
    for doctor in filtered_doctors:
        doctor.phone_number = number_format_frontend(doctor.phone_number)
    if len(filtered_doctors) == 1:
        context = {'doctor_list1': filtered_doctors, 'doctor_list2': [], 'user': user}
    else:
        context = {'doctor_list1': filtered_doctors[:int(len(filtered_doctors) / 2)], 'doctor_list2': filtered_doctors[int(len(filtered_doctors) / 2):], 'user': user}
    return render(request, 'docfinder/results.html', context=context)


def filter_doctors_by_user_preferences(preferences):
    matching_doctors = []
    for preference in preferences:
        if preference.key == "preferredDoctorGender":
            matching_gender_doctors = get_doctors_of_gender(preference.value)
            matching_doctors += list(set(matching_gender_doctors) - set(matching_doctors))
        if preference.key == "specialty":
            doctors_with_specialty = get_doctors_with_specialty(preference.value)
            matching_doctors += list(set(doctors_with_specialty) - set(matching_doctors))
    return matching_doctors


def get_doctors_with_specialty(specialty_id):
    specialty_object = Specialty.objects.get(id=specialty_id)
    doctors_with_specialty = []
    for doctor in Doctor.objects.all():
        if doctor in specialty_object.doctor_set.all():
            doctors_with_specialty.append(doctor)
    return doctors_with_specialty


def get_doctors_of_gender(gender):
    return Doctor.objects.filter(gender=gender)


def import_data(request):
    file_to_import = os.path.join(settings.PROJECT_ROOT, 'doctor_database.csv')
    file = open(file_to_import, 'rt', encoding="utf-8")
    reader = csv.reader(file)
    for row in reader:
        create_doctor_from_row(row)
    return HttpResponse("All data imported successfully!")


def create_doctor_from_row(row):
    full_name = row[0]
    if len(full_name.split(' ')) > 2:
        return None
    first_name = full_name.split(' ')[0]
    last_name = full_name.split(' ')[1]
    title = row[1]
    specializations = row[2]
    address = row[3]
    insurances = row[4]
    gender = row[6]
    phone_number = row[7]
    doctor = Doctor(first_name=first_name, last_name=last_name, title=title, address=address,
                    gender=convert_to_single_letter(gender), phone_number=number_format_db(phone_number))
    try:
        doctor.save()
    except Exception as e:
        print(str(e))
        raise Exception("Doctor could not be created. See error log.")
    create_specializations_for_doctor(doctor, specializations)
    create_insurances_for_doctor(doctor, insurances)
    return doctor


def create_user_from_post_request(post):
    first_name = post["firstName"] if post["firstName"] else None
    last_name = post["lastName"] if post["lastName"] else None
    email = post["email"] if post["email"] else None
    age = post["age"] if post["age"] else None
    gender = post["userGender"] if post["userGender"] else None
    user = User(first_name=first_name, last_name=last_name, email=email, age=age, gender=gender)
    try:
        user.save()
        return user
    except Exception as e:
        print(str(e))
        return None


def create_preferences_with_user(user, post):
    print(post)
    preferences = {}
    preferences["preferredDoctorGender"] = post.get("preferredDoctorGender", None)
    preferences["preferredDoctorAge"] = post.get("preferredDoctorAge", None)
    for preference in preferences:
        Preference(user=user, key=preference, value=preferences[preference]).save()
    for specialty in post.getlist("specialties"):
        Preference(user=user, key="specialty", value=specialty).save()
    return None


def convert_to_single_letter(gender):
    if gender == 'Male':
        return 'M'
    elif gender == 'Female':
        return 'F'
    return 'O'


def number_format_db(phone_number):
    phone_number = phone_number.replace('(', '')
    phone_number = phone_number.replace(')', '')
    phone_number = phone_number.replace('-', '')
    phone_number = phone_number.replace(' ', '')
    return phone_number


def number_format_frontend(number):
    return number[:3] + "-" + number[3:6] + "-" + number[6:]


def create_specializations_for_doctor(doctor, specializations):
    specializations = specializations.split(',')
    for specialty in specializations:
        specialty = specialty.lower()
        if len(Specialty.objects.filter(name=specialty)) > 0:
            doctor.specialties.add(Specialty.objects.get(name=specialty))
        else:
            new_specialty = Specialty.objects.create(name=specialty)
            doctor.specialties.add(new_specialty)
    return None


def create_insurances_for_doctor(doctor, insurances):
    insurances = insurances.split(',')
    for insurance in insurances:
        insurance = insurance.lower()
        if len(Insurance.objects.filter(name=insurance)) > 0:
            doctor.insurances.add(Insurance.objects.get(name=insurance))
        else:
            new_insurance = Insurance.objects.create(name=insurance)
            doctor.insurances.add(new_insurance)
    return None

