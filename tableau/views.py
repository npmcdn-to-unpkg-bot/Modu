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
    files = Files.objects.all()
    size = {'width':200, 'height':300}
    return render(request, 'select_picture.html', {'script':script, 'files':files, 'size':size})

def result(request, pic_id):
    pic_color = Colors.objects.all().filter(file_id=pic_id)
    pic_color = pic_color.values()[0]
    pic_color = (pic_color['red'], pic_color['green'], pic_color['blue'],)


    personalities = Personality.objects.all()
    #print(personalities.values())
    colors = {}
    for personality in personalities.values():
        colors[personality['rgb']] = (personality['red'], personality['green'], personality['blue'],)

    euclidean = lambda x, y: (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2
    distances = {k: euclidean(v, pic_color) for k, v in colors.items()}
    rgb_hex = min(distances, key=distances.get)

    for val in personalities.values():
        if val['rgb'] == rgb_hex:
            result = val['description']
            break

    return render(request, 'result.html', context={'personality' : result})

