import ckeditor.fields
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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('tanks', 'Танки'), ('healers', 'Хилы'), ('damage_dealers', 'ДД'), ('dealers', 'Торговцы'), ('gildmasters', 'Гилдмастеры'), ('quest_givers', 'Квестгиверы'), ('blacksmiths', 'Кузнецы'), ('tanners', 'Кожевники'), ('potion_makers', 'Зельевары'), ('spell_masters', 'Мастера заклинаний')], max_length=15, verbose_name='Категория')),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('text', ckeditor.fields.RichTextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('status', models.BooleanField(default=False)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.post')),
            ],
        ),
    ]
