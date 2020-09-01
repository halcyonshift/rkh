from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.blocks import (ListBlock, RichTextBlock)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

from .blocks import CTABlock


class HomePage(Page):
    body = StreamField([
        # A rich text field, so that the user can type in text and apply basic formatting
        ('text', RichTextBlock(required=False)),
        # A single image upload
        ('image', ImageChooserBlock(required=False)),
        # An image gallery (multiple images)
        ('gallery', ListBlock(ImageChooserBlock(), required=False)),
        # A structural block that contains...
        ('cta', CTABlock(required=False)),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
