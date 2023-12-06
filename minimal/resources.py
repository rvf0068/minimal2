"""test resources"""


import pkg_resources

imagen = pkg_resources.resource_filename('minimal', '/data/bomba.jpg')
texto = pkg_resources.resource_filename('minimal', '/data/texto.txt')
