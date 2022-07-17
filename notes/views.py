from django.shortcuts import render, HttpResponse
from .models import NoteModel

def index(request):
  return render(request,'notes/index.html')


def notes_view(request):
  if request.method == 'POST' :
    # print(request.POST)
    note_id = request.POST.get('id')
    note = NoteModel.objects.get(id=note_id)
    note.title = request.POST.get('title')
    note.text = request.POST.get('text')
    note.save()

    return HttpResponse()

  user = request.user
  if not user.is_anonymous :
    l_notes = NoteModel.objects.filter(user_obj=user)
    context = { 'notes' : l_notes}
  else:
    context = {}
  
  return render(request,'notes/notes.html',context)
