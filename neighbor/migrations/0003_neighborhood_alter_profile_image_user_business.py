# Generated by Django 4.0.5 on 2022-06-21 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbor', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeighborHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('occupants', models.IntegerField(default=0)),
                ('description', models.TextField(default='')),
                ('police_number', models.IntegerField(default=0)),
                ('health_number', models.IntegerField(default=0)),
                ('image', models.ImageField(default='nt.jpg', upload_to='neighborhood_pics')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='nt.jpg', upload_to='profile_pics'),
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='nt.jpg', upload_to='user_pics')),
                ('bio', models.TextField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('NeighborHood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbor.neighborhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('location', models.CharField(max_length=100)),
                ('occupants', models.IntegerField(default=0)),
                ('image', models.ImageField(default='nt.jpg', upload_to='business_pics')),
                ('email', models.EmailField(default='', max_length=254)),
                ('NeighborHood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbor.neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
