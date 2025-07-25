# Generated by Django 4.2.23 on 2025-06-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_employee',
            name='company_name',
            field=models.CharField(blank=True, db_collation='latin1_general_ci', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_intern',
            name='company_name',
            field=models.CharField(blank=True, db_collation='latin1_general_ci', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_users2',
            name='company_name',
            field=models.CharField(blank=True, db_collation='latin1_general_ci', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_users2',
            name='email',
            field=models.CharField(blank=True, db_collation='latin1_general_ci', max_length=250, null=True),
        ),
    ]
