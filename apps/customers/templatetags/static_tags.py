from django import template
from django.utils.html import format_html

register = template.Library()


def get_label_and_value(obj, field_name):
    # noinspection PyProtectedMember
    field = obj._meta.get_field(field_name)
    label = field.verbose_name

    if field.choices:
        # returns human readable value of field if choices are used
        # noinspection PyProtectedMember
        value = obj._get_FIELD_display(field)
    elif field.many_to_many:
        # returns m2m values  as a  string
        m2m_field = getattr(obj, field_name)
        value = ", ".join([str(t) for t in m2m_field.all()])
    else:
        value = getattr(obj, field_name)

    return label, value


@register.simple_tag
def static_field(obj, field_name):
    h = """
        <div class="form-group">
            <label class="control-label">{0}</label>
            <div class="control-data">
                <p class="form-control-static">{1}</p>
            </div>
        </div>
    """

    label, value = get_label_and_value(obj, field_name)
    if value:
        snippet = format_html(h, label, value)
        return snippet
    else:
        return ''
