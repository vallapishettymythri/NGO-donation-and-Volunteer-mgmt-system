from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, NGO, Donation, Volunteer, VolunteerOpportunity



# home
def index(request):
    return render(request, "index.html")


# admin login
def admin_login(request):
    if request.method == "POST":
        if request.POST['username'] == "admin" and request.POST['password'] == "admin123":
            request.session['admin'] = True
            return redirect('/admin_dashboard/')
        else:
            messages.error(request, "Invalid Admin Credentials")
    return render(request, "admin_login.html")


# admin dashboard
def admin_dashboard(request):
    if not request.session.get('admin'):
        return redirect('/admin_login/')
    return render(request, "admin_dashboard.html")


# add ngo
def add_ngo(request):
    if not request.session.get('admin'):
        return redirect('/admin_login/')

    if request.method == "POST":
        NGO.objects.create(
            name=request.POST['name'],
            address=request.POST['address'],
            contact_email=request.POST['email']
        )
        messages.success(request, "NGO Added Successfully")
        return redirect('/view_ngos/')
    return render(request, "add_ngo.html")


# view ngos-admin
def view_ngos(request):
    if not request.session.get('admin'):
        return redirect('/admin_login/')
    ngos = NGO.objects.all()
    return render(request, "view_ngos.html", {"ngos": ngos})


# view donations-admin
def view_donations(request):
    if not request.session.get('admin'):
        return redirect('/admin_login/')
    donations = Donation.objects.all()
    return render(request, "view_donations.html", {"donations": donations})


# user register
def register(request):
    if request.method == "POST":
        User.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        messages.success(request, "Registration Successful")
        return redirect('/user_login/')
    return render(request, "register.html")


# user login
def user_login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(
                email=request.POST['email'],
                password=request.POST['password']
            )
            request.session['user'] = user.id
            return redirect('/user_dashboard/')
        except:
            messages.error(request, "Invalid Credentials")
    return render(request, "user_login.html")


#user dashboard
def user_dashboard(request):
    if not request.session.get('user'):
        return redirect('/user_login/')
    return render(request, "user_dashboard.html")


#user views ngo
def user_ngos(request):
    if not request.session.get('user'):
        return redirect('/user_login/')
    ngos = NGO.objects.all()
    return render(request, "user_ngos.html", {"ngos": ngos})


#donate
def donate(request, ngo_id):
    if not request.session.get('user'):
        return redirect('/user_login/')

    user = User.objects.get(id=request.session['user'])
    ngo = NGO.objects.get(id=ngo_id)

    if request.method == "POST":
        donation_type = request.POST['donation_type']

        amount = None
        description = None

        if donation_type == "Money":
            amount = request.POST.get('amount')
        else:
            description = request.POST.get('description')

        Donation.objects.create(
            user=user,
            ngo=ngo,
            donation_type=donation_type,
            amount=amount,
            description=description,
            phone=request.POST['phone']
        )

        messages.success(request, "Donation request submitted. NGO will contact you.")
        return redirect('/user_dashboard/')

    return render(request, "donate.html", {"ngo": ngo})


# volunteer registration-user
def volunteer(request):
    if not request.session.get('user'):
        return redirect('/user_login/')

    user = User.objects.get(id=request.session['user'])

    if request.method == "POST":
        Volunteer.objects.create(
            user=user,
            skills=request.POST['skills'],
            availability=request.POST['availability']
        )
        messages.success(request, "Volunteer Registered Successfully")
        return redirect('/user_dashboard/')

    return render(request, "volunteer.html")

# ADD VOLUNTEER OPPORTUNITY (ADMIN) 
def add_volunteer(request):
    if not request.session.get('admin'):
        return redirect('/admin_login/')

    if request.method == "POST":
        VolunteerOpportunity.objects.create(
            name=request.POST['name'],
            location=request.POST['location'],
            role=request.POST['role'],
            required_count=request.POST['count']
        )
        messages.success(request, "Volunteer Opportunity Added")
        return redirect('/view_volunteer_opportunities/')

    return render(request, "add_volunteer.html")


# VIEW VOLUNTEER OPPORTUNITIES (ADMIN)
def view_volunteer_opportunities(request):
    if not request.session.get('admin'):
        return redirect('/admin_login/')

    opportunities = VolunteerOpportunity.objects.all()
    return render(
        request,
        "view_volunteer_opportunities.html",
        {"opportunities": opportunities}
    )


# USER VIEW VOLUNTEER OPPORTUNITIES 
def user_volunteer_opportunities(request):
    if not request.session.get('user'):
        return redirect('/user_login/')

    opportunities = VolunteerOpportunity.objects.all()
    return render(
        request,
        "user_volunteer_opportunities.html",
        {"opportunities": opportunities}
    )


#  USER ENROLL VOLUNTEER 
def enroll_volunteer(request, opp_id):
    if not request.session.get('user'):
        return redirect('/user_login/')

    opportunity = VolunteerOpportunity.objects.get(id=opp_id)

    if request.method == "POST":
        Volunteer.objects.create(
            opportunity=opportunity,
            name=request.POST['name'],
            phone=request.POST['phone']
        )
        messages.success(request, "Enrollment Successful")
        return redirect('/user_dashboard/')

    return render(
        request,
        "enroll_volunteer.html",
        {"opportunity": opportunity}
    )


# VIEW VOLUNTEER APPLICATIONS (ADMIN)
def view_volunteers(request):
    if not request.session.get('admin'):
        return redirect('/admin_login/')

    volunteers = Volunteer.objects.all()
    return render(
        request,
        "view_volunteers.html",
        {"volunteers": volunteers}
    )



#logout
def logout(request):
    request.session.flush()
    return redirect('/')
