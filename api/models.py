from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Lead(models.Model):

    name=models.CharField(max_length=100)

    mobile=models.CharField(max_length=15)

    email=models.CharField(max_length=100)

    college=models.CharField(max_length=150)

    qualification=models.CharField(max_length=150)

    passout_year=models.CharField(max_length=15)

    SOURCE_OPTIONS=(
        ("instagram","instagram"),
        ("facebook","facebook"),
        ("referral","referral"),
        ("walkin","walkin")
    )

    source=models.CharField(max_length=100,choices=SOURCE_OPTIONS,default="walkin")

    COURSE_OPTIONS=(
        ("TESTING","TESTING"),
        ("PYTHON DJANGO","PYTHON DJANGO"),
        ("MEARN","MEARN"),
        ("DATA SCIENCE","DATA SCIENCE"),
        ("JAVA SPRING","JAVA SPRING"),
        (".NET",".NET"),
    )

    course=models.CharField(max_length=25,choices=COURSE_OPTIONS,default="PYTHON DJANGO")

    COURSE_MODE_OPTIONS=(
        ("ONLINE","ONLINE"),
        ("OFFLINE","OFFLINE"),
        ("HYBRID","HYBRID")
    )

    course_mode=models.CharField(max_length=20,choices=COURSE_MODE_OPTIONS,default="OFFLINE")

    STATUS_OPTIONS=(
        ("FOLLOWUP","FOLLOW-UP"),
        ("PROCEEDTOADMISSION","PROCEED-TO-ADMISSION"),
        ("NOTINTERESTED","NOT-INTERESTED")
    )

    status=models.CharField(max_length=50,choices=STATUS_OPTIONS,default="FOLLOWUP")

    created_date=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


