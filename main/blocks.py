import re

from django import forms
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from django.utils.html import strip_tags

from wagtail.core.blocks import (CharBlock, ChoiceBlock, PageChooserBlock, RichTextBlock, StructBlock, URLBlock)

from .validators import validate_the_not_in_title


class ButtonBlock(StructBlock):
    url = URLBlock(required=False)
    page = PageChooserBlock(required=False)
    target = ChoiceBlock([('_self', 'Current tab'), ('_blank', 'New tab')], widget=forms.RadioSelect, default='_self')

    def clean(self, value):
        data = super().clean(value)

        if value.get('url') and value.get('page'):
            raise ValidationError('Button links error', params={
                'url': ErrorList(['Please choose a page OR enter a URL.']),
                'page': ErrorList(['Please choose a page OR enter a URL.'])
            })

        return data

    class Meta:
        icon = 'placeholder'


class CTABlock(StructBlock):
    # a title field
    # The title field (4.1) cannot contain the word "the"
    title = CharBlock(required=False, validators=[validate_the_not_in_title, ])
    # a rich text field
    # The rich text field (4.2) only allows paragraphs, bold text, and numbered lists
    text = RichTextBlock(required=False, features=['bold', 'ol'])
    # two buttons that can be configured to link to other internal Wagtail pages, or external URLs
    button_1 = ButtonBlock(required=False)
    button_2 = ButtonBlock(required=False)

    # The rich text field (4.2) cannot contain any of the words used in the title field (4.1)
    def clean(self, value):
        data = super().clean(value)

        if data.get('title') and data.get('text') and data.get('text').source:
            text = strip_tags(data.get('text').source)
            words = [word for word in data.get('title').split(" ")
                     if re.search(r'\b{}\b'.format(word), text, flags=re.IGNORECASE)]

            if words:
                raise ValidationError('The text field cannot contain any of the words used in the title field', params={
                    'text': ErrorList(['Please remove the following words: {}.'.format(", ".join(words))])
                })

        return data

    class Meta:
        label = "CTA"
        icon = 'pick'
