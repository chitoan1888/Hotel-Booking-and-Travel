from django.shortcuts import render

# Create your views here.
def cn_hue(request):
    return render(request, 'Hue.html')

def cn_vungtau(request):
    return render(request, 'VungTau.html')



