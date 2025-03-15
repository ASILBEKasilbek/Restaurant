from django import template

register = template.Library()

@register.filter(name='mul')  # Agar siz mul filteridan foydalansangiz
def multiply(value, arg):
    """Qiymatni argument bilan ko‘paytiradi."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return value
