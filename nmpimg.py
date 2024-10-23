import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


pic = Image.open('/home/lbj2/Desktop/Video_screenshot_21.09.2024.png')

# pic.show()

pic_arr = np.asarray(pic)

print(type(pic_arr))

print(pic_arr.shape)

# plt.show()

# red channel values
pic_red = pic_arr.copy()

plt.imshow(pic_red)
# plt.show()

plt.imshow(pic_red[:,:,0], cmap='gray')
plt.show()
print(pic_red[:,:,0])

plt.imshow(pic_red[:,:,1], cmap='gray')
plt.show()

plt.imshow(pic_red[:,:,2], cmap='gray')
plt.show()

pic_red[:,:,1] = 0
plt.imshow(pic_red)
plt.show()

pic_red[:,:,2] = 0
plt.imshow(pic_red)
plt.show()