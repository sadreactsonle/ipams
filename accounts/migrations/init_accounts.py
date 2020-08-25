from django.db import migrations


def insert_data(apps, schema_editor):
    UserRole = apps.get_model("accounts", "UserRole")
    UserRole.objects.bulk_create([
        UserRole(name='Guest'),
        UserRole(name='Student'),
        UserRole(name='Adviser'),
        UserRole(name='KTTO'),
        UserRole(name='RDCO'),
    ])


def delete_data(apps, schema_editor):
    UserRole = apps.get_model('accounts', 'UserRole')
    UserRole.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_data, delete_data)
    ]
