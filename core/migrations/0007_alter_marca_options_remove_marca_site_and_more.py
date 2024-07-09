# Generated by Django 5.0.6 on 2024-07-09 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_marca"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="marca",
            options={"verbose_name": "Marca", "verbose_name_plural": "Marcas"},
        ),
        migrations.RemoveField(
            model_name="marca",
            name="site",
        ),
        migrations.AddField(
            model_name="marca",
            name="nacionalidade",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="marca",
            name="nome",
            field=models.CharField(max_length=50),
        ),
    ]