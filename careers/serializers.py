from rest_framework import serializers

from .models import Vacancies, RequestForPractice, Resume, Practice

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ("id_graduate", "title", "target", "experience", "skills")

class VacanciesListSerializer(serializers.ModelSerializer):
    resume = ResumeSerializer(many=True)
    class Meta:
        model = Vacancies
        fields = ("title", "description", "image", "resume")


class VacanciesDetailSerializer(serializers.ModelSerializer):
    id_employer = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Vacancies
        exclude = ("")

class CreateRequestForPracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestForPractice
        fields = "__all__" 

class CreatePracticeSerializer(serializers.ModelSerializer):
    # Создание или изменение новой оценки#
    class Meta:
        model = Practice
        fields = ("title", "description", "status", "start", "end", "id_employer")

    def create(self, validated_data):
        practice = Practice.objects.update_or_create(
            id_employer=validated_data.get('id_employer', None),
            title=validated_data.get('title', None),
            start=validated_data.get('start', None),
            defaults={'end': validated_data.get('end')}
        )
        return practice

class DeletePracticeSerializer(serializers.ModelSerializer):
    # Создание или изменение новой оценки#
    class Meta:
        model = Practice
        fields = ("title", "description", "status", "start", "end", "id_employer")

    def delete(self, pk):
        practice = Practice.objects.filter(id=pk).delete()
        return practice
