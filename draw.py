# Newton fractals
# FB - 201003291
import math

from PIL import Image
imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))

# drawing area
xa = -1.0
xb = 1.0
ya = -1.0
yb = 1.0

maxIt = 20 # max iterations allowed
h = 1e-6 # step size for numerical derivative
eps = 1e-3 # max error allowed

# put any complex function here to generate a fractal for it!
def f(z):
    return z * z * z - 1.0

def dv(z):
    return 3*z*z

roots = [1.0, complex(-0.5, math.sqrt(3)/2), complex(-0.5, (-1)*math.sqrt(3)/2)]
colors = [(0,191,255),(255,140,0),(220,20,60)]

# draw the fractal
for y in range(imgy):
    zy = y * (yb - ya) / (imgy - 1) + ya
    for x in range(imgx):
        k=0
        zx = x * (xb - xa) / (imgx - 1) + xa
        z = complex(zx, zy)
        for i in range(maxIt):
            # complex numerical derivative
            dz = (f(z + complex(h, h)) - f(z)) / complex(h, h)
            z0 = z - f(z) / dz # Newton iteration
            for w, r in enumerate(roots):
                if abs(z0 - r) < eps: # stop when close enough to any root
                    image.putpixel((x, y), colors[w])
                    k=1
                    break
            z = z0
        if(k==0):
            image.putpixel((x, y), (128,0,0))

image.save("newtonFr.png", "PNG")