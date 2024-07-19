from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer
from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework.pagination import PageNumberPagination


class AdvocatePagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = "page_size"
    max_page_size = 10


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def advocates_list(request):
    if request.method == "GET":
        query = request.GET.get("query", "")
        advocates = Advocate.objects.filter(
            Q(username__icontains=query) | Q(bio__icontains=query)
        )

        # Apply pagination
        paginator = AdvocatePagination()
        paginated_advocates = paginator.paginate_queryset(advocates, request)
        serialized = AdvocateSerializer(paginated_advocates, many=True)

        # Get the paginated response
        return paginator.get_paginated_response(serialized.data)

    if request.method == "POST":
        Advocate.objects.create(
            profile_pic=request.data["profile_pic"],
            username=request.data["username"],
            bio=request.data["bio"],
        )
        return Response("Added", status=status.HTTP_201_CREATED)


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
        advocate = get_object_or_404(Advocate, username=username)
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
#     pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

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
