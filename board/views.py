from django.shortcuts import render

# Create your views here.
def board(request):
    print("===> board ")
    context ={"result" : "Board" }
    return render(request, 'board_index.html' ,context)