# coding: utf-8

#%%
# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

path = "Project/" if 1 else ""

#%%
# Reading data
fname = path + "RAVEDR5_UCAC5_McM_B_all.dat"
print(f"Reading {fname}")
Z, Vr, Vphi, eVphi, R = np.loadtxt(fname, usecols=(35, 39, 40, 43, 47), unpack=True)
print(f"Read {len(Z)} stars")
print()

#%%
# Filtering stars
Zmax = 0.5
mask1 = abs(Z) <= Zmax
R = R[mask1]
Vphi = Vphi[mask1]
eVphi = eVphi[mask1]
Z = Z[mask1]
Vr = Vr[mask1]
print(f"Stars with less Z than {Zmax}: {len(R)}")

eVphimax = 30
mask2 = abs(eVphi) <= eVphimax
R = R[mask2]
Vphi = Vphi[mask2]
eVphi = eVphi[mask2]
Z = Z[mask2]
Vr = Vr[mask2]
print(f"Stars with less Z than {Zmax} and less error than {eVphimax}: {len(R)}")

print()

# In[6]:
# Creating ID to group stars by radius
Rstep = 0.1
ID = np.array(R/Rstep, dtype=int)
print(f"ID created (Radius step = {Rstep})")

IDmin = np.amin(ID)
IDmax = np.amax(ID)
print(f"Minimum ID: {IDmin}")
print(f"Maximum ID: {IDmax}")
rng = range(IDmin, IDmax+1)
print(f"Range: {rng}")
print()

#%%
# Calculating rotation curve
Rar  = np.arange(IDmin, IDmax+1) * Rstep
Nbin = len(Rar)

Vphiar  = np.zeros(Nbin)
Vphiar2 = np.zeros(Nbin)
Nar     = np.zeros(Nbin, dtype=int)
Erar    = np.zeros(Nbin)
Va      = np.zeros(Nbin)
nn      = 0
print("Radius", "Vphi", "Vphi2", "Error", "Stars", "Va")
for x in rng:
    Vrbin       = Vr[np.where(ID==x)]
    Va[nn]      = (np.std(Vrbin)**2)/80
    Vphibin     = Vphi[np.where(ID==x)]
    Vphiar[nn]  = np.mean(Vphibin)
    Vphiar2[nn] = np.mean(Vphibin)+Va[nn]
    Nar[nn]     = len(Vphibin)
    Erar[nn]    = np.std(Vphibin)/np.sqrt(Nar[nn])
    print(Rar[nn], Vphiar[nn], Vphiar2[nn], Erar[nn], Nar[nn], Va[nn], np.std(Vphibin))
    nn += 1
print()

# In[8]:
# Plotting rotation curve
print("Grups:", len(Vphiar))
Narmin = 50
mask3 = Nar > Narmin
Vphiar = Vphiar[mask3]
Vphiar2 = Vphiar2[mask3]
Rar = Rar[mask3]
Erar = Erar[mask3]
print(f"Groups with more than {Narmin} stars: {len(Vphiar)}")

Erarmax=20
mask4 = Erar < Erarmax
Vphiar = Vphiar[mask4]
Vphiar2 = Vphiar2[mask4]
Rar = Rar[mask4]
Erar = Erar[mask4]
print(f"Groups with more than {Narmin} stars and less error than {Erarmax}: {len(Vphiar)}")

print()

# %%
# Plotting rotation curve with limits
plt.plot(Rar, Vphiar2)
plt.errorbar(Rar, Vphiar2, yerr = Erar, ecolor = "g")
plt.xlabel("R (kpc)")
plt.ylabel(r"V$\phi$ (km/s)")
plt.xlim()
plt.ylim([220,270])
# plt.savefig("RotCurve_2")
plt.show()


# %%
# Plotting rotation curve from 0
plt.plot(Rar, Vphiar2, color = "b")
plt.errorbar(Rar, Vphiar2, yerr = Erar, ecolor = "k")
plt.xlabel("R (kpc)")
plt.ylabel(r"V$\phi$ (km/s)")
plt.xlim()
plt.ylim([0,300])
# plt.savefig(path + "RotCurve.png")
plt.show()

# %%
# Plotting rotation curve from 0 with bokeh
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool, Whisker, Range1d, PanTool, WheelZoomTool, BoxZoomTool, ResetTool, SaveTool

data = dict(x=Rar, y=Vphiar2, error=Erar, error_u=Vphiar2+Erar, error_l=Vphiar2-Erar)
output_file(path + "RotCurve.html")

source = ColumnDataSource(data)
hover = HoverTool(tooltips=[("R", "@x"), ("V_phi", "@y"), ("Error", "@error")])
whisker = Whisker(source=source, base="x", upper="error_u", lower="error_l")
plot = figure(
    width = 1000, height = 400,
    title="Rotation Curve",
    tools=[hover, PanTool(), WheelZoomTool(), BoxZoomTool(), ResetTool(), SaveTool()]
)
plot.toolbar.autohide = True

plot.line("x", "y", line_width=2, source=source)
plot.scatter("x", "y", size=6, source=source)
plot.add_layout(whisker)

plot.xaxis.axis_label = "R (kpc)"
plot.yaxis.axis_label = r"$$V_\phi$$ (km/s)"
plot.y_range = Range1d(0, 300)

show(plot)

# %%
# Saving data to txt file
print("Creating file")
fname = path + "GalRotOS/rot_curve.npy"
np.save(fname, np.column_stack([Rar, Vphiar2, Erar]))
print("Numpy file created")
