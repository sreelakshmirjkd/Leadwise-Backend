from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView

from rest_framework.response import Response

from api.models import Lead

from api.serializers import LeadSerializer

from django.utils import timezone

from rest_framework import authentication, permissions

from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class GoodMorningView(APIView):

    def get(self, request, *args, **kwargs):

        context = {"message": "Good Morning"}

        return Response(data=context) # data - predefined
    
class GoodAfterNoonView(APIView):

    def get(self, request, *args, **kwargs):  

        context = {"message": "Good Afternoon"}

        return Response(data=context)

class GoodEveningView(APIView):

    def get(self, request, *args, **kwargs):  

        context = {"message": "Good Evening"}

        return Response(data=context)
    
class GoodNightView(APIView):

    def get(self, request, *args, **kwargs):  

        context = {"message": "Good Night"}

        return Response(data=context)
    
class AdditionView(APIView):

    def post(self, request, *args, **kwargs): 

        # django - requst.POST
        # rest - request.data

        n1 = request.data.get("num1")

        n2 = request.data.get("num2")

        result = int(n1)+int(n2)

        context = {"output": result}

        return Response(data=context)

class SubtractionView(APIView):

    def post(self, request, *args, **kwargs): 

        n1 = request.data.get("num1")

        n2 = request.data.get("num2")

        result = int(n1)-int(n2)

        context = {"output": result}

        return Response(data=context)
        
class MultiplicationView(APIView):

    def post(self, request, *args, **kwargs): 

        n1 = request.data.get("num1")

        n2 = request.data.get("num2")

        result = int(n1)*int(n2)

        context = {"output": result}

        return Response(data=context)

class FactorialView(APIView):

    def post(self, request, *args, **kwargs): 

        n = int(request.data.get("num"))

        result = 1

        for i in range(1,n+1):
            
            if i==0:

                result = 1
            
            elif i==1:

                result = 1
            
            elif i>1:

                result *=i

            else:

                print("Please enter a positive integer")


        context = {"output": result}

        return Response(data=context)


class PrimeView(APIView):

    def post(self, request, *args, **kwargs):

        n = int(request.data.get("num"))


        if n==0 or n==1:

            result = "n is not a prime"

        
        elif n>2:

            for i in range(2,int(n)):

                if n%i == 0:

                    break

                result = "n is not prime"
        
        else:

            result = "n is prime"

        
        context = {"output":result}

        return Response(data=context)



class BmiView(APIView):

    def post(self, request, *args, **kwargs):

        height_in_cm = int(request.data.get("height"))

        weight_in_kg = int(request.data.get("weight"))

        # bmi=weight_in_kg/height_in_meter**2

        height_in_meter = height_in_cm/100

        bmi = weight_in_kg/height_in_meter**2

        context = {"bmi_value": bmi}

        return Response(data=context)





# ================================================================================================== 

# Serializer -- Instead of forms.py
# ==========

class LeadListCreateView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = LeadSerializer

    def get(self, request, *args, **kwargs):

        qs = Lead.objects.all() # serialization -- queryset ==> python native type, while saving, deserialization --  python native==> queryset 

        serializer_instance = self.serializer_class(qs, many=True) # serialization. no data. many=true -- we need to add more than one leads.

        return Response(data=serializer_instance.data)


    def post(self, request, *args, **kwargs):

        serializer_instance = self.serializer_class(data=request.data) # deserialization. data is present

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors) # errors -- predefined keyword

# -----------------------------------------------

# patient_blood_test_booking
# name, phone, email, age, test, status, gender

# -----------------------------------------------

class LeadRetriveUpdateDestroyView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        qs = get_object_or_404(Lead, id=id)

        serializer_instance = LeadSerializer(qs)

        return Response(data=serializer_instance.data)
    
    def put(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        lead_instance = Lead.objects.get(id=id)

        serializer_instance = LeadSerializer(data=request.data, instance=lead_instance) # taking data given by the client -- instance -- update

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)

    def delete(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        Lead.objects.get(id=id).delete()

        return Response(data={"message": "Deleted"})

class CourseListView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAdminUser]


    def get(self, request, *args, **kwargs):

        all_courses = [i[0] for i in Lead.COURSE_OPTIONS] 

        return Response(data=all_courses)
        
        # no serializer needed, since we are taking only the tuple(python native type)
        # but we don't need two times like ("TESTING","TESTING"). We need to extract it only once. 

        # COURSE_OPTIONS=(
        #     ("TESTING","TESTING"),
        #     ("PYTHON DJANGO","PYTHON DJANGO"),
        #     ("MEARN","MEARN"),
        #     ("DATA SCIENCE","DATA SCIENCE"),
        #     ("JAVA SPRING","JAVA SPRING"),
        #     (".NET",".NET"),
        # )

        # To take only one entry, we can use loop and take 0th index.

# ------------------------------------------------------------------------------------------------------

class CourseSourceView(APIView):

    def get(self, request, *args, **kwargs):

        all_sources = [i[0] for i in Lead.SOURCE_OPTIONS]

        return Response(data=all_sources)

class CourseModesView(APIView):

    def get(self, request, *args, **kwargs):

        all_modes =[i[0] for i in Lead.COURSE_MODE_OPTIONS] 

        return Response(data=all_modes)


from django.db.models import Count

class LeadSummaryView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAdminUser]


    def get(self, request, *args, **kwargs):

        current_month = timezone.now().month # now - method, month - attribute

        current_year = timezone.now().year

        qs = Lead.objects.filter(created_date__month=current_month,created_date__year=current_year)

        current_month_lead_count = qs.count()

        # created_date__month=current_month -- to extract only month from complete date, use double underscore month.

        status_summary = qs.values("status").annotate(count=Count("status")) # annotate -- grouping based on the field "status", 
        
        # "aggregate" -- no grouping, just Sum, Max, Min, Avg, Count. When I need the summary belongs to a specific category. 

        # print(status_summary) # we store Count("status") to a variable count. else we will get 'status__count'.

        course_summary = qs.values("course").annotate(count=Count("course")) # annotate -- grouping based on the field "status", 

        course_mode_summary = qs.values("course_mode").annotate(count=Count("course_mode")) # annotate -- grouping based on the field "status", 

        source_summary = qs.values("source").annotate(count=Count("source")) # annotate -- grouping based on the field "status", 


        context = {

            "lead_count": current_month_lead_count,
            "status_summary": status_summary,
            "course_summary": course_summary,
            "course_mode_summary": course_mode_summary,
            "source_summary": source_summary,
        }

        return Response(data=context)
    










