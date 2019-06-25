# Generated by Django 2.2.2 on 2019-06-25 09:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pic', models.ImageField(default='default.png', upload_to='developer/')),
                ('designation', models.CharField(choices=[('D', 'Developer'), ('HD', 'Head of Web Development')], default='D', max_length=2)),
                ('github_url', models.URLField(blank=True)),
                ('linkedin_url', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('bio', models.CharField(max_length=600)),
                ('slug', models.SlugField(blank=True, max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pic', models.ImageField(default='default.png', upload_to='editor/')),
                ('designation', models.CharField(choices=[('E', 'Editor'), ('EC', 'Editor-in-Chief'), ('STE', 'Section Editor: Science & Technology Editor'), ('EFE', 'Section Editor: Economics & Finance Editor'), ('WAE', 'Section Editor: World Affairs Editor'), ('EE', 'Section Editor: Editorial Editor')], default='E', max_length=3)),
                ('linkedin_url', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('bio', models.CharField(max_length=600)),
                ('slug', models.SlugField(blank=True, max_length=30, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('synopsis', models.CharField(max_length=640)),
                ('content', models.TextField()),
                ('section', models.CharField(choices=[('EF', 'Economics & Finance'), ('E', 'Editorial'), ('ST', 'Science & Technology'), ('WA', 'World Affairs')], max_length=2)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='post_cover/')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
            ],
            options={
                'ordering': ('-published_date',),
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pic', models.ImageField(default='default.png', upload_to='author/')),
                ('designation', models.CharField(choices=[('A', 'Author'), ('F', 'Founder'), ('CF', 'Co-Founder'), ('GA', 'Guest Author')], default='A', max_length=2)),
                ('linkedin_url', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('bio', models.CharField(max_length=600)),
                ('slug', models.SlugField(blank=True, max_length=30, unique=True)),
                ('posts', models.ManyToManyField(blank=True, to='flapp.Post')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='flapp.Writer'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editor', to='flapp.Editor'),
        ),
        migrations.AddField(
            model_name='editor',
            name='edited_posts',
            field=models.ManyToManyField(blank=True, to='flapp.Post'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_approved', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='flapp.Post')),
            ],
        ),
    ]
