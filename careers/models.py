from django.db import models
from datetime import date


class DiplomaThesis(models.Model):
    title = models.CharField("Название", max_length=150)
    file = models.FileField("Пояснительная записка", upload_to="uploads/", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Диплом"
        verbose_name_plural = "Данные о дипломе"


class Profession(models.Model):
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"


class Employer(models.Model):
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    activities = models.TextField("Сфера деятельности")
    login = models.CharField("Логин", max_length=150)
    password = models.CharField("Пароль", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Работодатель"
        verbose_name_plural = "Работодатели"


class Vacancies(models.Model):
    image = models.ImageField("Изображение", upload_to="media/", null=True)
    title = models.CharField("Название", max_length=150)
    requirements = models.TextField("Требования", null=True)
    description = models.TextField("Описание")
    status = models.BooleanField("Статус", default=True)
    id_employer = models.ForeignKey(Employer, verbose_name="Работодатель", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Graduate(models.Model):
    name = models.CharField("Имя", max_length=150)
    patronymic = models.CharField("Отчество", max_length=150)
    surname = models.CharField("Фамилия", max_length=150)
    year_of_issue = models.PositiveSmallIntegerField("Год выпуска", default=0)
    login = models.CharField("Логин", max_length=150)
    password = models.CharField("Пароль", max_length=150)

    id_profession = models.ForeignKey(Profession, verbose_name="Профессия", on_delete=models.SET_NULL, null=True)
    id_diploma = models.ForeignKey(DiplomaThesis, verbose_name="Диплом", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Выпускник"
        verbose_name_plural = "Выпускники"


class Resume(models.Model):
    title = models.CharField("Название", max_length=150)
    target = models.TextField("Цель")
    experience = models.TextField("Опыт")
    skills = models.TextField("Навыки")
    date = models.DateTimeField

    id_graduate = models.ForeignKey(Graduate, verbose_name="Выпускник", on_delete=models.SET_NULL, null=True)
    id_vacancy = models.ForeignKey(Vacancies, verbose_name="Вакансия", on_delete=models.SET_NULL, null=True, related_name="resume")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"


class Events(models.Model):
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    date = models.DateTimeField

    id_employer = models.ForeignKey(Employer, verbose_name="Работодатель", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class Practice(models.Model):
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    status = models.BooleanField("Статус", default=True)
    start = models.DateField("Дата начала", default=date.today)
    end = models.DateField("Дата окончания", default=date.today)
    id_employer = models.ForeignKey(Employer, verbose_name="Работодатель", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Практика"
        verbose_name_plural = "Данные о практиках"


class Students(models.Model):
    surname = models.CharField("Фамилия", max_length=150)
    name = models.CharField("Имя", max_length=150)
    patronymic = models.CharField("Отчество", max_length=150)
    year_of_issue = models.PositiveSmallIntegerField("Год выпуска", default=0)
    login = models.CharField("Логин", max_length=150)
    password = models.CharField("Пароль", max_length=150)

    id_profession = models.ForeignKey(Profession, verbose_name="Профессия", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class RequestForPractice(models.Model):
    id_practice = models.ForeignKey(Practice, verbose_name="Практика", on_delete=models.SET_NULL, null=True)
    id_student = models.ForeignKey(Students, verbose_name="Студент", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки на практику"
