import os

from django.shortcuts import render
from .analyze import colorz as cz
from django.http import *
from tableau.models import Files, Colors, Personality

def update(request):
    img_dir = 'static/img/'
    for file in os.listdir(img_dir):
        db_file = Files(filename=file)
        db_file.save()
        rgbs = cz(img_dir+file)
        rgb_str = ''
        for rgb in rgbs:
            rgb_str = '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])
        colors = Colors(rgb=rgb_str, red=rgb[0], green=rgb[1], blue=rgb[2])
        colors.file_id = db_file.id
        colors.save()

def index(request):
    script = '''<script src="https://npmcdn.com/masonry-layout@4.0/dist/masonry.pkgd.min.js"></script>'''
    files = Files.objects.values('filename')
    size = {'width':200, 'height':300}
    return render(request, 'select_picture.html', {'script':script, 'files':files, 'size':size})

def result(request):
    return render(request, 'result.html')

