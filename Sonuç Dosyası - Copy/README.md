Bu dosya ExpressionPoints excelleri için açıklama içindir.
- Satır boyunca dizilen duygular yüzlerin durumunu, sütun boyunca dizilen duygular arka plandaki ilişkili duyguyu temsil etmektedir.
- Her bir hücredeki dizi sırasıyla (intact sayısı, rearranged sayısı, new sayısı) olarak belirlenmiştir.import matplotlib.pyplot as plt
import numpy as np

# Create the figure and axes
fig, ax = plt.subplots(1, 2, figsize=(8, 4))

# Define colors
gray_circle = 0.5  # Same gray for both circles
dark_bg = 0.2  # Dark background
light_bg = 0.8  # Light background

# Create backgrounds
ax[0].set_facecolor(str(dark_bg))
ax[1].set_facecolor(str(light_bg))

# Hide axes
for a in ax:
    a.set_xticks([])
    a.set_yticks([])
    a.set_xlim(0, 1)
    a.set_ylim(0, 1)
    a.set_frame_on(False)

# Add gray circles
circle1 = plt.Circle((0.5, 0.5), 0.2, color=str(gray_circle), ec="black", lw=2)
circle2 = plt.Circle((0.5, 0.5), 0.2, color=str(gray_circle), ec="black", lw=2)

ax[0].add_patch(circle1)
ax[1].add_patch(circle2)

# Add labels
ax[0].set_title("Sensation: Identical Circles", fontsize=10)
ax[1].set_title("Perception: Different Brightness", fontsize=10)

# Show plot
plt.tight_layout()
plt.show()

