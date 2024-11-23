import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def apply_filters(image):
    low_pass = gaussian_filter(image, sigma=1)
    high_pass = image - low_pass
    high_boost = image + 1.5 * high_pass
    return low_pass, high_pass, high_boost

image_color = img.imread("c:\\Users\\Lenovo\\Downloads\\kkn.jpeg")
if image_color.ndim == 3:
    image_gray = np.mean(image_color, axis=2).astype(np.uint8)
else:
    image_gray = image_color

low_pass_color, high_pass_color, high_boost_color = apply_filters(image_color)
low_pass_gray, high_pass_gray, high_boost_gray = apply_filters(image_gray)

plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.title('Original Color Image')
plt.imshow(image_color)
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title('Low-Pass Filter (Color)')
plt.imshow(low_pass_color)
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title('High-Pass Filter (Color)')
plt.imshow(high_pass_color)
plt.axis('off')

plt.subplot(2, 3, 4)
plt.title('Original Grayscale Image')
plt.imshow(image_gray, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.title('Low-Pass Filter (Grayscale)')
plt.imshow(low_pass_gray, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.title('High-Pass Filter (Grayscale)')
plt.imshow(high_pass_gray, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()