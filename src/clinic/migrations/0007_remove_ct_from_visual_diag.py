from django.db import migrations

OLD_SHORT_DESCRIPTION = 'УЗД, рентген, КТ'
NEW_SHORT_DESCRIPTION = 'УЗД, рентген'


def remove_ct(apps, schema_editor):
    Service = apps.get_model('clinic', 'Service')
    Service.objects.filter(slug='visual-diag').update(short_description=NEW_SHORT_DESCRIPTION)


def restore_ct(apps, schema_editor):
    Service = apps.get_model('clinic', 'Service')
    Service.objects.filter(slug='visual-diag').update(short_description=OLD_SHORT_DESCRIPTION)


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0006_phoenix_content'),
    ]

    operations = [
        migrations.RunPython(remove_ct, restore_ct),
    ]
