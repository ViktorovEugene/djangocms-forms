# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from contextlib import contextmanager

from django.forms import widgets
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from djangocms_text_ckeditor import widgets as ckeditor_widgets_module

if render_to_string is not ckeditor_widgets_module.render_to_string:
    render_to_string = ckeditor_widgets_module.render_to_string

CUSTOM_TEMPLATE = 'cms/plugins/widgets/ckeditor_form_field_init.html'


def monkey_render_to_string(template_name, *args, **kwargs):
    return render_to_string(CUSTOM_TEMPLATE, *args, **kwargs)


@contextmanager
def mock_render_to_string():
    ckeditor_widgets_module.render_to_string = monkey_render_to_string
    yield
    ckeditor_widgets_module.render_to_string = render_to_string


class TextEditorWidgetFormField(ckeditor_widgets_module.TextEditorWidget):

    def __init__(self, attrs=None, installed_plugins=None, pk=None,
                 placeholder=None, plugin_language=None, configuration=None,
                 cancel_url=None, render_plugin_url=None, action_token=None,
                 delete_on_cancel=False, no_additions=False):
        self.no_additions = no_additions
        super().__init__(attrs, installed_plugins, pk, placeholder,
                         plugin_language, configuration, cancel_url,
                         render_plugin_url, action_token, delete_on_cancel)

    def render_additions(self, name, value, attrs=None):
        if self.no_additions:
            return ''
        with mock_render_to_string():
            return super().render_additions(name, value, attrs)


class TelephoneInput(widgets.TextInput):
    input_type = 'tel'


class SearchInput(widgets.TextInput):
    input_type = 'search'


class DateInput(widgets.TextInput):
    input_type = 'date'


class TimeInput(widgets.TextInput):
    input_type = 'time'


class ReCaptchaWidget(widgets.Widget):

    def render(self, name, value, attrs=None):
        template = '<div class="g-recaptcha" id="%(widget_id)s"></div>'
        return mark_safe(template % {'widget_id': 'id_%s' % name})

    def value_from_datadict(self, data, files, name):
        return (data.get('g-recaptcha-response', None), )
