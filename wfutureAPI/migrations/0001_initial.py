# Generated by Django 5.0.6 on 2024-07-02 23:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('promocode', models.CharField(blank=True, max_length=50, null=True)),
                ('available', models.BooleanField(default=True)),
                ('points_cost', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CauseVolunteerships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.cause')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.country')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.country')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='wfutureAPI\\static\\img\\avatars')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('mission', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.location')),
            ],
        ),
        migrations.CreateModel(
            name='SkillVolunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.skill')),
            ],
        ),
        migrations.CreateModel(
            name='SkillVolunteerships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_points', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('storeitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.storeitem')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='wfutureAPI\\static\\img\\avatars')),
                ('sex', models.CharField(max_length=50)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('points', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('skills', models.ManyToManyField(through='wfutureAPI.SkillVolunteer', to='wfutureAPI.skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='skillvolunteer',
            name='volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.volunteer'),
        ),
        migrations.CreateModel(
            name='Volunteership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='wfutureAPI\\static\\img\\pictures')),
                ('description', models.TextField(blank=True, null=True)),
                ('mission_statement', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('points', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('causes', models.ManyToManyField(blank=True, through='wfutureAPI.CauseVolunteerships', to='wfutureAPI.cause')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.company')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.location')),
                ('skills', models.ManyToManyField(blank=True, through='wfutureAPI.SkillVolunteerships', to='wfutureAPI.skill')),
            ],
        ),
        migrations.AddField(
            model_name='skillvolunteerships',
            name='volunteership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.volunteership'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.company')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.volunteer')),
                ('volunteership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.volunteership')),
            ],
        ),
        migrations.AddField(
            model_name='causevolunteerships',
            name='volunteership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.volunteership'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_content', models.TextField(blank=True, null=True)),
                ('status', models.CharField(default='unchecked', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.volunteer')),
                ('volunteership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.volunteership')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteershipLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.volunteer')),
                ('volunteership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.volunteership')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerVolunteership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='active', max_length=50)),
                ('recieved_points', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.volunteer')),
                ('volunteership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wfutureAPI.volunteership')),
            ],
        ),
    ]
