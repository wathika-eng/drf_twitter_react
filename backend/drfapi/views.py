from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer
from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.views import APIView


@api_view(["GET", "POST", "DELETE"])
# @permission_classes([IsAuthenticated])
def advocates_list(request):
    if request.method == "GET":

        # /?query
        query = request.GET.get("query")
        print(query)  # check if we have a query in the url

        if query == None:
            query = ""

        # use Q to search for multiple fields, take care not to use &
        advocates = Advocate.objects.filter(
            Q(username__icontains=query) | Q(bio__icontains=query)
        )  # find a username incase it contains at least one letter
        # advocates = Advocate.objects.all()
        serialized = AdvocateSerializer(advocates, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        Advocate.objects.create(
            username=request.data["username"], bio=request.data["bio"]
        )
        serializer = AdvocateSerializer(Advocate, many=False)
        return Response("added")


@api_view(["GET", "PUT", "DELETE"])
def advocate_details(request, username=None):
    if request.method == "GET":
        if username:
            advocate = get_object_or_404(Advocate, username=username)
            serialized = AdvocateSerializer(advocate)
            return Response(serialized.data)
        else:
            advocates = Advocate.objects.all()
            serialized = AdvocateSerializer(advocates, many=True)
            return Response(serialized.data)

    if request.method == "PUT":
        advocate = get_object_or_404(Advocate, pk=pk)
        serializer = AdvocateSerializer(advocate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        advocate = get_object_or_404(Advocate, pk=pk)
        advocate.delete()


@api_view(["GET", "PUT", "DELETE"])
def company_details(request, pk=None):
    if request.method == "GET":
        if pk:
            company = get_object_or_404(Company, pk=pk)
            serialized = CompanySerializer(company)
            return Response(serialized.data)
        else:
            company = Company.objects.all()
            serialized = CompanySerializer(company, many=True)
            return Response(serialized.data)

    if request.method == "PUT":
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        company = get_object_or_404(Company, pk=pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class AdvocateDetails(APIView):
#     def get(self, request):
#         advocates = Advocate.objects.all()
#         serialized = AdvocateSerializer(advocates, many=True)
#         return Response(serialized.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = AdvocateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         advocate = get_object_or_404(Advocate, pk=id)
#         serializer = AdvocateSerializer(advocate, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         advocate = get_object_or_404(Advocate, pk=pk)
#         advocate.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
