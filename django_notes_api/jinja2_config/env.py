from jinja2 import Environment

from django.templatetags.static import static
from django.urls import reverse
from django.contrib.messages import get_messages


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "reverse": reverse,
            "get_messages": get_messages,
        }
    )

    return env
