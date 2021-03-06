# Generated by Django 4.0.1 on 2022-02-13 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categoryType',
            field=models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], default='AR', max_length=2, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='dateCreation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания новости'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(through='news.PostCategory', to='news.Category', verbose_name='Тематика'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Заголовок'),
        ),
    ]
