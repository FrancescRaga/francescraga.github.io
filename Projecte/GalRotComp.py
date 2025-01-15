# -*- coding: utf-8 -*-

# Packages
import numpy as np
from astropy import units
from galpy.potential import MiyamotoNagaiPotential, NFWPotential, calcRotcurve
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool, Whisker, Range1d, PanTool, WheelZoomTool, BoxZoomTool, ResetTool, SaveTool

# Parameters
path = 'Project/GalRotOS/' if 1 else ''
data_file = path + 'rot_curve.npy'
output_file(path + "RotCurveComponents.html")

r_0 = 1     # kpc
v_0 = 220   # km/s

vmaxplot = 300
params = {
    'BULGE':     {'mass': 1.06E+10, 'threshold_mass': 1, 'a': 0, 'threshold_a': 20, 'b': 0.3, 'threshold_b': 70},
    'THIN DISK': {'mass': 3.94E+10, 'threshold_mass': 1, 'a': 5.3, 'threshold_a': 90, 'b': 0.25, 'threshold_b': 1},
    'DARK HALO': {'mass': 8.00E+11, 'threshold_mass': 1, 'a': 14, 'threshold_a': 90}
}

r_data, v_c_data, v_c_err_data=np.load(data_file).T

# lista = np.linspace(0.00001, np.max(r_data), 10*len(r_data))
r_bins = np.linspace(0.00001, np.max(r_data) * 1.01, 10*len(r_data))

# Potentials definition using physical units (amplitude in Solar masses, scales in kpc and surface density in Solar masses / pc^2 )
MN_Bulge_p = MiyamotoNagaiPotential(
    amp = params['BULGE']['mass'] * units.Msun,
    a = params['BULGE']['a'] * units.kpc,
    b = params['BULGE']['b'] * units.kpc,
    normalize = False,
    ro = r_0 * units.kpc,
    vo = v_0 * units.km/units.s
)
MN_Bulge = calcRotcurve(MN_Bulge_p, r_bins, phi = None) * v_0
MN_Thin_Disk_p = MiyamotoNagaiPotential(
    amp = params['THIN DISK']['mass'] * units.Msun,
    a = params['THIN DISK']['a'] * units.kpc,
    b = params['THIN DISK']['b'] * units.kpc,
    normalize = False,
    ro = r_0 * units.kpc,
    vo = v_0 * units.km/units.s
)
MN_Thin_Disk = calcRotcurve(MN_Thin_Disk_p, r_bins, phi = None) * v_0
NFW_p = NFWPotential(
    amp = params['DARK HALO']['mass'] * units.Msun,
    a = params['DARK HALO']['a'] * units.kpc,
    normalize = False,
    ro = r_0 * units.kpc,
    vo = v_0 * units.km/units.s
)
NFW = calcRotcurve(NFW_p, r_bins, phi = None) * v_0
v_circ_comp = calcRotcurve([MN_Bulge_p, MN_Thin_Disk_p, NFW_p], r_bins, phi = None) * v_0

data = dict(x=r_data, y=v_c_data, error=v_c_err_data, error_u=v_c_data+v_c_err_data, error_l=v_c_data-v_c_err_data)
source = ColumnDataSource(data)
hover = HoverTool(tooltips=[("R", "@x"), ("V_phi", "@y"), ("Error", "@error")])
whisker = Whisker(source=source, base="x", upper="error_u", lower="error_l")
plot = figure(
    width = 1000, height = 400,
    title="Rotation Curve with theoretical components",
    tools=[hover, PanTool(), WheelZoomTool(), BoxZoomTool(), ResetTool(), SaveTool()]
)
plot.toolbar.autohide = True

plot.line(r_bins, v_circ_comp, line_width=2, legend_label="Total", color='black')
plot.line(r_bins, MN_Bulge, line_width=2, line_dash='dashed', color='gray', legend_label="Bulge")
plot.line(r_bins, MN_Thin_Disk, line_width=2, line_dash='dashed', color='lightblue', legend_label="Thin Disk")
plot.line(r_bins, NFW, line_width=2, line_dash='dashed', color='green', legend_label="Dark Halo")
plot.scatter("x", "y", size=6, source=source, legend_label="Data", color='black', alpha=0.5)
plot.add_layout(whisker)

plot.xaxis.axis_label = "R (kpc)"
plot.yaxis.axis_label = r"$$V_\phi$$ (km/s)"
plot.y_range = Range1d(0, 300)
plot.legend.location = "bottom_right"

show(plot)