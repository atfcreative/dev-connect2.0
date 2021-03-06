# Generated by Django 2.1.2 on 2018-12-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev_connect', '0009_merge_20181031_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_link',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='hosted_link',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.ImageField(blank=True, upload_to='projects'),
        ),
        migrations.AlterField(
            model_name='project',
            name='teammates',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='tech',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
