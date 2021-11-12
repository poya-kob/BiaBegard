from django.db import models


class Ostan(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام استان")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "استان ها"
        verbose_name = "استان"


class Shahrestan(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام شهرستان")
    ostan = models.ForeignKey(Ostan, on_delete=models.CASCADE, verbose_name="استان مربوطه")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "شهرستان ها"
        verbose_name = "شهرستان"


class Shahr(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام شهر")
    ostan = models.ForeignKey(Ostan, on_delete=models.CASCADE, verbose_name="استان مربوطه")
    shahrestan = models.ForeignKey(Shahrestan, on_delete=models.CASCADE, verbose_name="شهرستان مربوطه")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "شهر ها"
        verbose_name = "شهر"


class Dehestan(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دهستان")
    ostan = models.ForeignKey(Ostan, on_delete=models.CASCADE, verbose_name="استان مربوطه")
    shahrestan = models.ForeignKey(Shahrestan, on_delete=models.CASCADE, verbose_name="شهرستان مربوطه")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "دهستان ها"
        verbose_name = "دهستان"
