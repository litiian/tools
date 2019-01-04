# Generated by Django 2.0.6 on 2018-07-13 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('host_management', '0012_databaseuserinfo_grant_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHostOperationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.PositiveSmallIntegerField(choices=[(1, '添加'), (2, '修改'), (3, '启用'), (4, '停用')], verbose_name='操作')),
                ('action', models.CharField(max_length=100, verbose_name='操作详情')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('op_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_op_record_user', to=settings.AUTH_USER_MODEL, verbose_name='操作用户')),
            ],
            options={
                'verbose_name': '用户主机操作表',
                'verbose_name_plural': '用户主机操作表',
            },
        ),
    ]