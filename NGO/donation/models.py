from django.db import models



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class NGO(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name




    

class VolunteerOpportunity(models.Model):
    name = models.CharField(max_length=200)       
    location = models.CharField(max_length=300)
    role = models.CharField(max_length=200)
    required_count = models.IntegerField()

    def __str__(self):
        return f"{self.role} - {self.name}"
    



class Volunteer(models.Model):
    opportunity = models.ForeignKey(
        VolunteerOpportunity,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)        # volunteer name
    phone = models.CharField(max_length=15)        # phone number

    def __str__(self):
        return f"{self.name} - {self.opportunity.role}"




class Donation(models.Model):
    DONATION_TYPE_CHOICES = [
        ('Money', 'Money'),
        ('Blood', 'Blood'),
        ('Items', 'Items'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)

    donation_type = models.CharField(
        max_length=10,
        choices=DONATION_TYPE_CHOICES,
        default='Money'
    )

    amount = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    phone = models.CharField(
        max_length=15,
        default='0000000000'   
    )

    donated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.donation_type}"


