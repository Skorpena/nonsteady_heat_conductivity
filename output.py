from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import geometryProperties as gP
import main


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data.
Y = main.timeArray
X = gP.gM
X, Y = np.meshgrid(X, Y)
Z = main.T_output

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.jet,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(max(main.T_bulk), min(main.T_bulk))
ax.zaxis.set_major_locator(LinearLocator(5))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#ax.invert_xaxis()
#ax.invert_yaxis()
ax.invert_zaxis()

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
