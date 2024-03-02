# https://pypi.org/project/pixelmatch/
# Adapted by Paul Lu for CMPUT 274, October 2023
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
import sys

img_a = Image.open(sys.argv[1])
img_b = Image.open(sys.argv[2])
img_diff = Image.new("RGBA", img_a.size)

# note how there is no need to specify dimensions
mismatch = pixelmatch(img_a, img_b, img_diff, includeAA=True)
print("Diffcount:", mismatch)
img_diff.save(sys.argv[1]+".diff.png")

if mismatch < 700:      # Arbitrary threshold
    sys.exit(0)
else:
    print("Image Diff Failed for", sys.argv[1], "and", sys.argv[2])
    sys.exit(1)
