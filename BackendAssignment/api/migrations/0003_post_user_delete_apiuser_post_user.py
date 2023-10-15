# Generated by Django 4.2.6 on 2023-10-15 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_apiuser_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('post_content', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('email_id', models.EmailField(db_index=True, max_length=256, unique=True)),
                ('pwd_hash', models.CharField(max_length=256)),
                ('full_name', models.CharField(max_length=256)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='ApiUser',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]