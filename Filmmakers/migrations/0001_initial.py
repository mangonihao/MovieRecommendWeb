# Generated by Django 2.2.3 on 2020-04-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('celebrity_id', models.AutoField(primary_key=True, serialize=False, verbose_name='明星id')),
                ('celebrity_name', models.CharField(max_length=20, verbose_name='明星名字')),
                ('celebrity_gender', models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], default='男', max_length=10, null=True, verbose_name='明星性别')),
                ('celebrity_cover', models.CharField(blank=True, max_length=150, null=True, verbose_name='明星封面图片路径')),
                ('celebrity_doubanID', models.IntegerField(blank=True, null=True, verbose_name='豆瓣id')),
            ],
        ),
    ]
