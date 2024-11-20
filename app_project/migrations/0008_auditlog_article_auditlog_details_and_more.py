# Generated by Django 4.2.15 on 2024-11-11 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_project', '0007_remove_auditlog_article_remove_auditlog_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditlog',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audit_logs', to='app_project.article'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auditlog',
            name='action',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='auditlog',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='auditlog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_project.customuser'),
        ),
    ]