# Generated by Django 2.0.6 on 2018-07-09 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_ip', models.GenericIPAddressField(verbose_name='内外IP')),
                ('out_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='外外IP')),
                ('hostname', models.CharField(max_length=30, verbose_name='主机名')),
                ('cpu', models.CharField(max_length=30, verbose_name='CPU')),
                ('disk', models.IntegerField(verbose_name='磁盘')),
                ('memory', models.IntegerField(verbose_name='内存')),
                ('network', models.IntegerField(verbose_name='带宽')),
                ('ssh_port', models.IntegerField(verbose_name='远程端口')),
                ('root_ssh', models.BooleanField(default=True, verbose_name='是否允许 root 远程')),
                ('admin_user', models.CharField(max_length=20, verbose_name='管理员用户')),
                ('admin_pass', models.CharField(max_length=20, verbose_name='管理员密码')),
                ('normal_user', models.CharField(max_length=20, verbose_name='普通用户')),
                ('normal_pass', models.CharField(max_length=20, verbose_name='普通用户密码')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '正常'), (2, '停用')], verbose_name='状态')),
            ],
            options={
                'verbose_name': '主机信息',
                'verbose_name_plural': '主机信息',
            },
        ),
        migrations.CreateModel(
            name='IdcInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='机房名称')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='描述')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '正常'), (2, '停用')], verbose_name='状态')),
                ('add_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idc_add_user', to=settings.AUTH_USER_MODEL, verbose_name='添加人')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idc_update_user', to=settings.AUTH_USER_MODEL, verbose_name='修改人')),
            ],
            options={
                'verbose_name': '机房',
                'verbose_name_plural': '机房',
            },
        ),
        migrations.CreateModel(
            name='OperatingEnvironmentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='环境名称')),
                ('desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='描述')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '正常'), (2, '停用')], verbose_name='状态')),
                ('add_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='env_add_user', to=settings.AUTH_USER_MODEL, verbose_name='添加人')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='env_update_user', to=settings.AUTH_USER_MODEL, verbose_name='修改人')),
            ],
            options={
                'verbose_name': '服务环境',
                'verbose_name_plural': '服务环境',
            },
        ),
        migrations.CreateModel(
            name='OperatingSystemInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='系统名称')),
                ('version', models.CharField(max_length=10, verbose_name='系统版本')),
                ('desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='描述')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '正常'), (2, '停用')], verbose_name='状态')),
                ('add_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='os_add_user', to=settings.AUTH_USER_MODEL, verbose_name='添加人')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='os_update_user', to=settings.AUTH_USER_MODEL, verbose_name='修改人')),
            ],
            options={
                'verbose_name': '操作系统',
                'verbose_name_plural': '操作系统',
            },
        ),
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='项目名称')),
                ('pro_user', models.CharField(max_length=30, verbose_name='开发人员')),
                ('op_user', models.CharField(max_length=30, verbose_name='运维人员')),
                ('run_env', models.CharField(max_length=100, verbose_name='运行环境')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '正常'), (2, '停用')], verbose_name='状态')),
                ('add_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_add_user', to=settings.AUTH_USER_MODEL, verbose_name='添加人')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_update_user', to=settings.AUTH_USER_MODEL, verbose_name='修改人')),
            ],
            options={
                'verbose_name': '用途',
                'verbose_name_plural': '用途',
            },
        ),
        migrations.CreateModel(
            name='UseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='用途')),
                ('desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='描述')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '正常'), (2, '停用')], verbose_name='状态')),
                ('add_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='use_add_user', to=settings.AUTH_USER_MODEL, verbose_name='添加人')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='use_update_user', to=settings.AUTH_USER_MODEL, verbose_name='修改人')),
            ],
            options={
                'verbose_name': '用途',
                'verbose_name_plural': '用途',
            },
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host_management.IdcInfo', verbose_name='机房'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='op_env',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host_management.OperatingEnvironmentInfo', verbose_name='服务环境'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='op_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_op_user', to=settings.AUTH_USER_MODEL, verbose_name='负责人'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host_management.ProjectInfo', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host_management.OperatingSystemInfo', verbose_name='操作系统'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_update_user', to=settings.AUTH_USER_MODEL, verbose_name='修改人'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='use',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host_management.UseInfo', verbose_name='用途'),
        ),
    ]