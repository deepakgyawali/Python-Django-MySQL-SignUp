import pymysql.cursors
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse
from django.template import Context, loader
from passlib.hash import pbkdf2_sha256

from .forms import ContactForm, ContactForm1, ContactForm2, ContactForm3

def _form_view_one(request, template_name='index.html', form_class=ContactForm):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            # Open database connection
            db = pymysql.connect("localhost", "root", "", "djangoproject")

            # prepare a cursor object using cursor() method
            cursor = db.cursor()

            # catch form field data
            username = request.POST.get('username')
            password = request.POST.get('password1')
            hashpassword = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)

            # Prepare SQL query to INSERT a record into the database.
            sql = "insert into users VALUES('', '%s', '%s')" % \
                  (username, hashpassword)
            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

            # disconnect from server
            db.close()
            pass  # does nothing, just trigger the validation
    else:
        form = form_class()
    return render(request, template_name, {'form': form})


def index(request):
    return _form_view_one(request, template_name='index.html', form_class=UserCreationForm)


def _form_view_two(request, template_name='login.html', form_class=ContactForm1):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            #return redirect("https://www.djangoproject.com")
            # Open database connection
            db = pymysql.connect("localhost", "root", "", "djangoproject")

            # catch form field data
            username = request.POST.get('username')
            password = request.POST.get('password')
            cursor = db.cursor()

            # Prepare SQL query to select a data from database
            sql = ("Select * from customer where username ='%s'" % (username))
            cursor.execute(sql)
            for row in cursor:
                dbhashpass = row[4]
                firstname = row[1]
                surname = row[2]


                #https: // passlib.readthedocs.io / en / stable /  # getting-started
                if (pbkdf2_sha256.verify(password, dbhashpass)):
                    return render(request, 'thankyou.html', {
                        'firstname': firstname,
                        'surname': surname
                    })

                else:
                    form = form_class()
                    return render(request, template_name, {'form': form})
            pass  # does nothing, just trigger the validation

    else:
        form = form_class()
    return render(request, template_name, {'form': form})


def login(request):
    return _form_view_two(request, template_name='login.html', form_class=ContactForm1)

def _form_view_three(request, template_name='customer.html', form_class=ContactForm2):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            #return redirect("https://www.djangoproject.com")
            # Open database connection
            db = pymysql.connect("localhost", "root", "", "djangoproject")

            # catch form field data
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            hashpassword = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
            email = request.POST.get('email')
            contact_no = request.POST.get('contact_no')
            address = request.POST.get('address')
            postcode = request.POST.get('postcode')
            cursor = db.cursor()

            # Prepare SQL query to INSERT a record into the database.
            sql = "insert into customer VALUES('', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','1')" % \
                  (first_name, last_name, username, hashpassword, email, contact_no, address, postcode)
            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

            # disconnect from server
            db.close()
            pass  # does nothing, just trigger the validation

    else:
        form = form_class()
    return render(request, template_name, {'form': form})


def customer(request):
    return _form_view_three(request, template_name='customer.html', form_class=ContactForm2)



def _form_view_four(request, template_name='search.html', form_class=ContactForm3):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            #return redirect("https://www.djangoproject.com")
            # Open database connection
            db = pymysql.connect("localhost", "root", "", "djangoproject")

            # catch form field data
            username = request.POST.get('username')
            cursor = db.cursor()

            # Prepare SQL query to select a data from database
            sql = ("Select * from customer where username ='%s'" % (username))
            cursor.execute(sql)
            fields = cursor.fetchall()
            counter = 0
            for field in fields:
                counter = counter + 1
                username = field[3]

                firstname = field[1]
                surname = field[2]
                email = field[5]
                contact_no = field[6]
                address = field[7]
                postcode = field[8]

                return render(request, 'success.html', {
                    'firstname': firstname,
                    'surname': surname,
                    'email': email,
                    'contact_no': contact_no,
                    'address': address,
                    'postcode': postcode
                })

                cursor.close()
                db.close()
    else:

        form = form_class()
    return render(request, template_name, {'form': form})


def search(request):
    return _form_view_four(request, template_name='search.html', form_class=ContactForm3)

