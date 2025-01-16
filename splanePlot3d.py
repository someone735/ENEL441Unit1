import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import control as ct


S = ct.tf([1, 4, 6, 4], [1, 4, 7, 7])
print(S.zeros())
print(S.poles())

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
alpha = np.arange(-5,1,0.05)
beta = np.arange(-5,5,0.05)

S_mag = np.zeros((alpha.shape[0], beta.shape[0]))
ii = 0
for aa in alpha:
    jj = 0
    for bb in beta:
        s = complex(aa,bb)
        S_mag[ii,jj] = np.abs((s**3 + 4*s**2 + 6*s + 4)/(s**3 + 4*s**2 + 7*s + 7))
        if S_mag[ii,jj] > 100:
            S_mag[ii,jj] = 100
        jj+=1
    ii+=1
        


Alpha, Beta = np.meshgrid(beta, alpha)

print(alpha.shape)
print(beta.shape)
print(S_mag.shape)
print(Alpha.shape)
print(Beta.shape)

# Plot the surface.
surf = ax.plot_surface(Alpha, Beta, S_mag, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_ylabel('Real')
ax.set_xlabel('Imaginary')

#ax.plot(beta,np.zeros(40),S_mag[20,:]+0.5,'.',linewidth=3)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

