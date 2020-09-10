"""
TARGET LINE PLOT
Version: 0
Author: S Kerstetter
Last Update: 09/09/2020

Plot target line for directional drilling from input target line data and calculate
distance above/below line from input survey data.
"""

# *** IMPORT LIBRARIES ***
import math

# *** DEFINE VARIABLES ***

# Target Line Inputs
tvd_0vs = 8811 # feet KB TVD
inc_degrees = 90.3 # degrees
inc_radians = math.radians(90.0 - inc_degrees)

# Survey Inputs
svy_tvd = 8760 # feet TVD
svy_vs = 8150 # feet VS

# Lateral Length
lat_len = 10000 # feet VS

# *** MAIN SCRIPT ***

tvd_target = math.tan(inc_radians) * svy_vs + tvd_0vs
dtvd = tvd_target - svy_tvd

if dtvd > 0:
	location = 'above'
elif dtvd < 0:
	location = 'below'
else:
	location = 'on the'

print(f"Target line: {tvd_0vs}' KB TVD @ 0' VS")
print(f"Survey: {svy_tvd}' TVD @ {svy_vs}' VS")
print(f"Target line depth at {svy_vs}' VS is {tvd_target:.2f}' TVD.")
print(f"Survey is {dtvd:.2f}' TVD {location} target line.")

# calculate target line TVD every 100' VS
tl_vs = []
tl_tvd = []
vs = 0
while vs <= lat_len:
	tl_vs.append(vs)
	tl_tvd.append(math.tan(inc_radians) * vs + tvd_0vs)
	vs += 100

print("Target Line\nVS   TVD")
for i in range(0,len(tl_vs)):
	print(tl_vs[i], round(tl_tvd[i]))