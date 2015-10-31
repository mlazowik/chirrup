from django import template
from chirp.forms import ChirpForm

register = template.Library()


@register.inclusion_tag('chirp/chirp.html')
def chirp(chirp):
    return {'chirp': chirp}


@register.inclusion_tag('chirp/chirp-list.html', takes_context=True)
def chirps(context, chirps, with_form=False):
    return {'chirps': chirps, 'with_form': with_form, 'form': ChirpForm}


@register.inclusion_tag('chirp/chirp-form.html', takes_context=True)
def chirp_form(context):
    return {'form': ChirpForm, 'request': context.request}
