# Generated by Django 4.0 on 2022-01-08 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0007_alter_post_options_post_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('tags', models.ManyToManyField(to='blog.Post')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
