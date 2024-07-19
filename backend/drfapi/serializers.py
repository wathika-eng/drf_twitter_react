from rest_framework import serializers
from .models import Advocate, Company
from urllib.parse import unquote


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

    def get_count(self, obj):
        # county = None
        count = obj.advocate.set.count()
        return count


class AdvocateSerializer(serializers.ModelSerializer):
    # pass
    company = CompanySerializer()  # nested serializer

    # https://stackoverflow.com/questions/26379849/return-image-url-in-django-rest-framework
    profile_pic = serializers.SerializerMethodField("get_profile_pic_url")

    class Meta:
        model = Advocate
        fields = ["username", "bio", "company", "profile_pic"]

    def get_profile_pic_url(self, obj):
        return unquote(obj.profile_pic.url.lstrip("/"))

    # def create(self, validated_data):
    #     company_data = validated_data.pop('company')
    #     company = Company.objects.create(**company_data)
    #     advocate = Advocate.objects.create(company=company, **validated_data)
    #     return advocate

    # def update(self, instance, validated_data):
    #     company_data = validated_data.pop('company')
    #     company = instance.company

    #     instance.username = validated_data.get('username', instance.username)
    #     instance.bio = validated_data.get('bio', instance.bio)
    #     instance.save()

    #     company.name = company_data.get('name', company.name)
    #     company.address = company_data.get('address', company.address)
    #     company.save()

    #     return instance
