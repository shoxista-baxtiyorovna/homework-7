from django.shortcuts import render, redirect
from .models import ProgrammingLanguage


def program_list(request):
    programs = ProgrammingLanguage.objects.all
    ctx ={'programs': programs}
    return render(request, 'programs/program_list.html', ctx)

def program_add(request):
    language_name = request.POST.get('language_name')
    description = request.POST.get('description')
    if language_name and description:
        ProgrammingLanguage.objects.create(
            language_name=language_name,
            description=description,
        )
        return redirect('programs:list')

    return render(request, 'programs/program_add.html')