# Generated by Django 4.1.4 on 2022-12-06 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChoreoStyles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'choreo_styles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DanceGroups',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=50, unique=True)),
                ('vacant_place', models.IntegerField()),
            ],
            options={
                'db_table': 'dance_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DancerVisits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'dancer_visits',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('log_date', models.DateTimeField()),
                ('log_info', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'logs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Memberships',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('amount_of_lessons', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'memberships',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('permission_id', models.AutoField(primary_key=True, serialize=False)),
                ('permission_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RolePermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'role_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'roles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('lesson_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_length', models.FloatField()),
                ('is_completed', models.BooleanField()),
                ('date_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'schedule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Styles',
            fields=[
                ('style_id', models.AutoField(primary_key=True, serialize=False)),
                ('style_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'styles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=50, unique=True)),
                ('user_password', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128, unique=True)),
                ('user_name', models.CharField(max_length=50)),
                ('user_surname', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Choreographers',
            fields=[
                ('choreo', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dance_school.users')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('salary', models.FloatField()),
            ],
            options={
                'db_table': 'choreographers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dancers',
            fields=[
                ('dancer', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dance_school.users')),
                ('amount_of_lessons_left', models.IntegerField()),
            ],
            options={
                'db_table': 'dancers',
                'managed': False,
            },
        ),
    ]
