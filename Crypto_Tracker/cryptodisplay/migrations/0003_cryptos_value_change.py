
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptodisplay', '0002_cryptos_crypto_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptos',
            name='value_change',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
