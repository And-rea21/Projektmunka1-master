# Generated by Django 3.2.6 on 2021-08-02 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_libs.models
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='Start date')),
                ('end', models.DateTimeField(verbose_name='End date')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('description', models.TextField(blank=True, max_length=2048, verbose_name='Description')),
                ('end_recurring_period', models.DateTimeField(blank=True, null=True, verbose_name='End of recurring')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('frequency', models.CharField(choices=[('YEARLY', 'Yearly'), ('MONTHLY', 'Monthly'), ('WEEKLY', 'Weekly'), ('DAILY', 'Daily')], max_length=10, verbose_name='frequency')),
                ('params', models.TextField(blank=True, null=True, verbose_name='params')),
            ],
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='Start date')),
                ('end', models.DateTimeField(verbose_name='End date')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('description', models.TextField(blank=True, max_length=2048, verbose_name='Description')),
                ('original_start', models.DateTimeField(verbose_name='Original start')),
                ('original_end', models.DateTimeField(verbose_name='Original end')),
                ('cancelled', models.BooleanField(default=False, verbose_name='Cancelled')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='Title')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='occurrences', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='occurrences', to='calendarium.event', verbose_name='Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField()),
                ('relation_type', models.CharField(blank=True, max_length=32, null=True, verbose_name='Relation type')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarium.event', verbose_name='Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, max_length=256, verbose_name='Slug')),
                ('color', django_libs.models.ColorField(max_length=6, verbose_name='Color')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parents', to='calendarium.eventcategory', verbose_name='Parent')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='calendarium.eventcategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calendarium_event_images', to=settings.FILER_IMAGE_MODEL, verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='event',
            name='rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='calendarium.rule', verbose_name='Rule'),
        ),
    ]
