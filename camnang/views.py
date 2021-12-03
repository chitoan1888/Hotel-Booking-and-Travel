from django.shortcuts import render

# Create your views here.
def cn_hue(request):
    return render(request, 'Hue.html')

def cn_vungtau(request):
    return render(request, 'VungTau.html')

def cn_laocai(request):
    return render(request, 'LaoCai.html')

def cn_hanoi(request):
    return render(request, 'HaNoi.html')

def cn_detail(request):
    return render(request, 'camnang.html')

def cn_mienbac(request):
    return render(request, 'TopMienBac.html')

def cn_miennam(request):
    return render(request, 'TopMienNam.html')

def cn_mientrung(request):
    return render(request, 'TopMienTrung.html')