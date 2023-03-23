from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_account_picture"),
        ('user', '0002_alter_account_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name="UserPreferedScreenMode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mode",
                    models.CharField(
                        blank=True,
                        choices=[("Dark", "Dark"), ("Light", "Light")],
                        default="Dark",
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]