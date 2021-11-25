# Generated by Django 3.2.8 on 2021-11-25 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alluniv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('univname', models.CharField(blank=True, max_length=100, null=True)),
                ('unicity', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'alluniv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GradStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(blank=True, max_length=100, null=True)),
                ('gpass', models.CharField(blank=True, max_length=100, null=True)),
                ('gemail', models.CharField(blank=True, max_length=100, null=True)),
                ('gmajor', models.CharField(blank=True, max_length=100, null=True)),
                ('guniv', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'grad_student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('univid', models.CharField(blank=True, max_length=100, null=True)),
                ('sid', models.CharField(blank=True, max_length=100, null=True)),
                ('question', models.CharField(blank=True, max_length=100, null=True)),
                ('answer', models.CharField(blank=True, max_length=100, null=True)),
                ('gid', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(blank=True, max_length=40, null=True)),
                ('semail', models.CharField(blank=True, max_length=40, null=True)),
                ('spass', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usersv2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Usersv2',
                'managed': False,
            },
        ),
    ]
