# Generated by Django 3.1 on 2020-09-01 14:34

from django.db import migrations, models
import django.db.models.deletion
import main.validators
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('gallery', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), required=False)), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False, validators=[main.validators.validate_the_not_in_title])), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'ol'], required=False)), ('button_1', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('target', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current tab'), ('_blank', 'New tab')]))], required=False)), ('button_2', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('target', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current tab'), ('_blank', 'New tab')]))], required=False))], required=False))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
