import re

from django.core.exceptions import ValidationError


def validate_the_not_in_title(value):
    if re.search(r'\bthe\b', value, flags=re.IGNORECASE):
        raise ValidationError("The title field cannot contain the word 'the'")
