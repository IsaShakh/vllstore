# Generated by Django 5.0.6 on 2024-05-21 12:13

import django.contrib.postgres.search
import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('order', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('icon', models.URLField(blank=True, null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True, null=True)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('condition', models.CharField(choices=[('NEW', 'New'), ('GU', 'Gently used'), ('U', 'Used'), ('VU', 'Very used'), ('NS', 'Not specified')], default='NS', max_length=3)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('NS', 'Not specified')], default='NS', max_length=2)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('is_modification', models.BooleanField(default=False)),
                ('moderation_status', models.CharField(choices=[('DR', 'Draft'), ('MD', 'On moderation'), ('AP', 'Approved'), ('RJ', 'Declined')], default='DR', max_length=2)),
                ('moderator_review', models.TextField(blank=True, null=True)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.city')),
                ('modification', models.OneToOneField(blank=True, help_text='при редактировании товара создается модификация, она будет отправлятьсяна модерацию, после одобрения будет заменять оригинал', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='original', to='products.product')),
            ],
        ),
    ]
