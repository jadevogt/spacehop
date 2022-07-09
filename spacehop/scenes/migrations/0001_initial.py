# Generated by Django 4.0.6 on 2022-07-09 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('character_one', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scenes_used_in_by_default_as_char_one', to='characters.character')),
                ('character_one_expression', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scenes_used_in_by_default_as_char_expression_one', to='characters.expression')),
                ('character_two', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scenes_used_in_by_default_as_char_two', to='characters.character')),
                ('character_two_expression', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scenes_used_in_by_default_as_char_expression_two', to='characters.expression')),
            ],
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('scene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scenes.scene')),
                ('textbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
        migrations.AddField(
            model_name='scene',
            name='events',
            field=models.ManyToManyField(through='scenes.Sequence', to='events.event'),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scenes.chapter')),
                ('scene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scenes.scene')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='scenes',
            field=models.ManyToManyField(through='scenes.Page', to='scenes.scene'),
        ),
    ]
