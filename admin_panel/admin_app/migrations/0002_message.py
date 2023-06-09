# Generated by Django 4.2 on 2023-04-03 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.TextField(verbose_name='message text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='receiving time')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.profile', verbose_name='profile')),
            ],
            options={
                'verbose_name': 'message',
            },
        ),
    ]
