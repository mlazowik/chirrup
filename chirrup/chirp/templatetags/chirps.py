from django import template
from chirp.forms import ChirpForm

register = template.Library()


@register.inclusion_tag('chirp/chirp.html')
def chirp(chirp):
    return {'chirp': chirp}


@register.inclusion_tag('chirp/chirp_list.html')
def chirps(chirps):
    return {'chirps': chirps}


@register.inclusion_tag('chirp/chirp_form.html', takes_context=True)
def chirp_form(context):
    return {'form': ChirpForm, 'request': context.request}
