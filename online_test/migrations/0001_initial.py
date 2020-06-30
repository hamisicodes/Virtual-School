# Generated by Django 3.0.6 on 2020-06-30 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content_management_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=70)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content_management_system.Course')),
            ],
            options={
                'verbose_name_plural': 'Quizzes',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='QuizTaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('date_finished', models.DateTimeField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_test.Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='UsersAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='online_test.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_test.Question')),
                ('quiz_taker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='online_test.QuizTaker')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_test.Quiz'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_test.Question'),
        ),
    ]
