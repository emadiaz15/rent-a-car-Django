from django.shortcuts import render

def home_view(request):
    theme = request.COOKIES.get('theme', 'light')
    context = {
        'theme': theme,
        # otros contextos
    }
    return render(request, 'core/home.html', context)
