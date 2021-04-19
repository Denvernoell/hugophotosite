import os
import shutil
import random

os.chdir('static/img')

for decade in range(10, 70, 10):
    mypath = f"./{decade} split/"
    my_folder = []

    for f in os.listdir(mypath):
        my_photo = random.choice(
            [photo for photo in os.listdir(f"{mypath}{f}")])
        # print(my_photo)
        # my_folder.append(f)
        # print(my_folder)

        my_markdown = f'''
---
title: "19{decade}s ({f})"
date: 2020-12-29T10:40:14-08:00
draft: false
image: "/img/{decade} split/{f}/{my_photo}"
Summary: ""
#   Taxonomies
categories:
    - "19{decade}s"
tags:
    - "19{decade}s"
#post type
type: "post"
HideDate: true
---

Photos from throughout the 19{decade}s ({f})
{{{{< gallery dir="/img/{decade} split/{f}" />}}}} {{{{< load-photoswipe >}}}}
'''

        with open(f"../../content/blog split/19{decade} {f}.md", 'w') as md:
            md.write(my_markdown)

        # print(my_markdown)
