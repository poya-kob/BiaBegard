

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'اسلایدر', 'verbose_name_plural': 'اسلایدرها'},
        ),
    ]
