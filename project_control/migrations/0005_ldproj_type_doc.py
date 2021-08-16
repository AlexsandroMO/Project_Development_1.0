# Generated by Django 3.2.6 on 2021-08-09 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_control', '0004_remove_ldproj_doc_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ldproj',
            name='type_doc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='project_control.doctype', verbose_name='TIPO DE DOCUMENTO'),
            preserve_default=False,
        ),
    ]