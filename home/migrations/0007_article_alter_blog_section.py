# Generated by Django 5.0.7 on 2025-03-15 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_comment_blog_id_alter_blog_section_alter_blog_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='articles/')),
                ('link', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='section',
            field=models.CharField(choices=[('Trending', 'Trending'), ('Recent', 'Recent'), ('Popular', 'Popular')], max_length=100),
        ),
    ]
