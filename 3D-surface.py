# 3D Surface Plot with Custom Colormap and Shading

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Surface plot with custom colormap and shading
surf = ax.plot_surface(
    x, y, z, 
    cmap='plasma',         # Try 'viridis', 'coolwarm', 'inferno', etc.
    edgecolor='k', 
    linewidth=0.5, 
    antialiased=True, 
    shade=True              # Enable shading for lighting effect
)

ax.set_title('3D Surface Plot with Custom Colormap & Shading')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
