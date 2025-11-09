"""_summary_

Returns:
    _type_: _description_
"""
from django.shortcuts import render


def home(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, 'home.html')
