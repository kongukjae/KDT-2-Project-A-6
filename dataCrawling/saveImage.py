from urllib import request
from io import BytesIO
from PIL import Image
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 다운받을 이미지 url
url = "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/352149381_190211370301838_2984010991133471420_n.jpg?stp=dst-jpg_e35&_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=102&_nc_ohc=_YIf-bMkcOUAX_uZ1xM&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=MzEyMDIyNzA1MDMzNTIzMzUxMA%3D%3D.2-ccb7-5&oh=00_AfDl_d5AdgqNwrJXvrJjDFGU3zd28n_tmGpjshenCPgV9w&oe=648575CE&_nc_sid=79e58c"

# request.urlopen()
res = request.urlopen(url).read()

# Image open
img = Image.open(BytesIO(res))
print(img)
