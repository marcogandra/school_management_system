# Generated by Django 2.2.3 on 2019-08-07 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0019_auto_20190807_0728'),
        ('student', '0011_auto_20190807_0657'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='academicinfo',
            unique_together={('class_info', 'roll')},
        ),
    ]