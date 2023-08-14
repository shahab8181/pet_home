from django import template
from jalali_date import date2jalali

register: template = template.Library()

@register.filter(name='ctj')
def convert_to_jalali(value):
    return date2jalali(value)

@register.filter(name='td')
def three_digits(value):
    return '{:,}'.format(value)

