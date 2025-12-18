from django.db import models

class CertificateExpiry(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    department = models.CharField(max_length=100, verbose_name="ОТДЕЛ")
    expiry_date = models.DateField(verbose_name="ДАТА ОКОНЧАНИЯ")

    def __str__(self):
        return f"{self.full_name} - {self.department}"

class CertificateUser(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    computer_number = models.CharField(max_length=50, verbose_name="Номер компьютера")
    installed_certificate = models.CharField(max_length=100, verbose_name="Какой сертификат установлен")

    def __str__(self):
        return f"{self.full_name} - {self.computer_number}"