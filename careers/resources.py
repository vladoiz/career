from import_export import resources
from careers.models import Vacancies


class VacanciesResources(resources.ModelResource):
    class Meta:
        model = Vacancies
