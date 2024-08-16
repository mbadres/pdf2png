#!/usr/bin/env python3

from pdf2image import convert_from_path

filename = 'file'

pages = convert_from_path(filename + '.pdf', 500)
for page in pages:
    page.save(filename + '.png', 'PNG')
