import numpy as np
import matplotlib.pyplot as plt
import csv

# ============================================================
# NACA 6412 — 2D Direct Foil Analysis (XFoil, via XFLR5)
# Polar: T1_Re1.000_M0.00_N9.0
# Re = 1,000,000 | Mach = 0.000 | Ncrit = 9.0 | alpha = -5 to 18 deg
# ============================================================

# --- Load data ---
alpha, cl, cd, cdp, cm = [], [], [], [], []
with open('naca6412_polar.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        alpha.append(float(row['alpha']))
        cl.append(float(row['CL']))
        cd.append(float(row['CD']))
        cdp.append(float(row['CDp']))
        cm.append(float(row['Cm']))

alpha = np.array(alpha)
cl = np.array(cl)
cd = np.array(cd)
cdp = np.array(cdp)
cm = np.array(cm)
cl_cd = cl / cd

NAVY  = "#1A3A5C"
GOLD  = "#E6A817"
TEAL  = "#2E8B8B"
RED   = "#C0392B"

plt.rcParams.update({'font.family': 'DejaVu Sans', 'axes.spines.top': False,
                      'axes.spines.right': False})

# ------------------------------------------------------------
# GRAPH 1 — Cl vs Alpha
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(alpha, cl, 'o-', color=NAVY, linewidth=2, markersize=4, zorder=3)

# Mark Cl_max
idx_max = np.argmax(cl)
ax.plot(alpha[idx_max], cl[idx_max], 'o', color=RED, markersize=10, zorder=4)
ax.annotate(f'$C_{{L,max}}$ = {cl[idx_max]:.3f}\nat $\\alpha$ = {alpha[idx_max]:.1f}°',
            (alpha[idx_max], cl[idx_max]), textcoords='offset points', xytext=(-90, -10),
            fontsize=9, fontweight='bold', color=RED)

ax.axhline(0, color='gray', linewidth=0.6)
ax.axvline(0, color='gray', linewidth=0.6)
ax.set_xlabel('Angle of Attack, $\\alpha$ (deg)', fontsize=11)
ax.set_ylabel('Lift Coefficient, $C_L$', fontsize=11)
ax.set_title('NACA 6412 — $C_L$ vs $\\alpha$\nXFoil | Re = 1,000,000 | Ncrit = 9.0',
             fontsize=11, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('cl_vs_alpha.png', dpi=150, bbox_inches='tight')
plt.close()

# ------------------------------------------------------------
# GRAPH 2 — Cd vs Alpha
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(alpha, cd, 's-', color=RED, linewidth=2, markersize=4, zorder=3)

idx_min = np.argmin(cd)
ax.plot(alpha[idx_min], cd[idx_min], 'o', color=NAVY, markersize=10, zorder=4)
ax.annotate(f'$C_{{D,min}}$ = {cd[idx_min]:.5f}\nat $\\alpha$ = {alpha[idx_min]:.1f}°',
            (alpha[idx_min], cd[idx_min]), textcoords='offset points', xytext=(10, 15),
            fontsize=9, fontweight='bold', color=NAVY)

ax.set_xlabel('Angle of Attack, $\\alpha$ (deg)', fontsize=11)
ax.set_ylabel('Drag Coefficient, $C_D$', fontsize=11)
ax.set_title('NACA 6412 — $C_D$ vs $\\alpha$\nXFoil | Re = 1,000,000 | Ncrit = 9.0',
             fontsize=11, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('cd_vs_alpha.png', dpi=150, bbox_inches='tight')
plt.close()

# ------------------------------------------------------------
# GRAPH 3 — Drag Polar (Cl vs Cd) — the classic XFoil plot
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 6))
ax.plot(cd, cl, 'o-', color=TEAL, linewidth=2, markersize=4, zorder=3)
ax.set_xlabel('Drag Coefficient, $C_D$', fontsize=11)
ax.set_ylabel('Lift Coefficient, $C_L$', fontsize=11)
ax.set_title('NACA 6412 — Drag Polar ($C_L$ vs $C_D$)\nXFoil | Re = 1,000,000',
             fontsize=11, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('drag_polar_2d.png', dpi=150, bbox_inches='tight')
plt.close()

# ------------------------------------------------------------
# GRAPH 4 — Cl/Cd (efficiency) vs Alpha
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(alpha, cl_cd, '^-', color=GOLD, linewidth=2, markersize=4, zorder=3)

idx_eff = np.argmax(cl_cd)
ax.plot(alpha[idx_eff], cl_cd[idx_eff], 'o', color=NAVY, markersize=10, zorder=4)
ax.annotate(f'Max $C_L/C_D$ = {cl_cd[idx_eff]:.1f}\nat $\\alpha$ = {alpha[idx_eff]:.1f}°',
            (alpha[idx_eff], cl_cd[idx_eff]), textcoords='offset points', xytext=(10, -25),
            fontsize=9, fontweight='bold', color=NAVY)

ax.set_xlabel('Angle of Attack, $\\alpha$ (deg)', fontsize=11)
ax.set_ylabel('Aerodynamic Efficiency, $C_L/C_D$', fontsize=11)
ax.set_title('NACA 6412 — Aerodynamic Efficiency vs $\\alpha$\nXFoil | Re = 1,000,000',
             fontsize=11, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('clcd_vs_alpha_2d.png', dpi=150, bbox_inches='tight')
plt.close()

# ------------------------------------------------------------
# GRAPH 5 — Cm vs Alpha (pitching moment)
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(alpha, cm, 'd-', color=NAVY, linewidth=2, markersize=4, zorder=3)
ax.axhline(0, color='gray', linewidth=0.6)
ax.set_xlabel('Angle of Attack, $\\alpha$ (deg)', fontsize=11)
ax.set_ylabel('Pitching Moment Coefficient, $C_m$', fontsize=11)
ax.set_title('NACA 6412 — $C_m$ vs $\\alpha$ (about quarter-chord)\nXFoil | Re = 1,000,000',
             fontsize=11, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('cm_vs_alpha.png', dpi=150, bbox_inches='tight')
plt.close()

# ------------------------------------------------------------
# GRAPH 6 — Combined 2x2 dashboard
# ------------------------------------------------------------
fig, axs = plt.subplots(2, 2, figsize=(12, 9))

axs[0,0].plot(alpha, cl, 'o-', color=NAVY, linewidth=2, markersize=3)
axs[0,0].set_xlabel('$\\alpha$ (deg)'); axs[0,0].set_ylabel('$C_L$')
axs[0,0].set_title('$C_L$ vs $\\alpha$', fontweight='bold')
axs[0,0].grid(True, linestyle='--', alpha=0.4)

axs[0,1].plot(alpha, cd, 's-', color=RED, linewidth=2, markersize=3)
axs[0,1].set_xlabel('$\\alpha$ (deg)'); axs[0,1].set_ylabel('$C_D$')
axs[0,1].set_title('$C_D$ vs $\\alpha$', fontweight='bold')
axs[0,1].grid(True, linestyle='--', alpha=0.4)

axs[1,0].plot(alpha, cl_cd, '^-', color=GOLD, linewidth=2, markersize=3)
axs[1,0].set_xlabel('$\\alpha$ (deg)'); axs[1,0].set_ylabel('$C_L/C_D$')
axs[1,0].set_title('Efficiency vs $\\alpha$', fontweight='bold')
axs[1,0].grid(True, linestyle='--', alpha=0.4)

axs[1,1].plot(cd, cl, 'o-', color=TEAL, linewidth=2, markersize=3)
axs[1,1].set_xlabel('$C_D$'); axs[1,1].set_ylabel('$C_L$')
axs[1,1].set_title('Drag Polar', fontweight='bold')
axs[1,1].grid(True, linestyle='--', alpha=0.4)

fig.suptitle('NACA 6412 — 2D Foil Analysis Summary\nXFoil | Re = 1,000,000 | Ncrit = 9.0',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig('foil2d_dashboard.png', dpi=150, bbox_inches='tight')
plt.close()

print("All 6 graphs generated:")
print("1. cl_vs_alpha.png")
print("2. cd_vs_alpha.png")
print("3. drag_polar_2d.png")
print("4. clcd_vs_alpha_2d.png")
print("5. cm_vs_alpha.png")
print("6. foil2d_dashboard.png")
print()
print(f"Key results:")
print(f"  Cl_max = {cl[idx_max]:.3f} at alpha = {alpha[idx_max]:.1f} deg")
print(f"  Cd_min = {cd[idx_min]:.5f} at alpha = {alpha[idx_min]:.1f} deg")
print(f"  Max Cl/Cd = {cl_cd[idx_eff]:.1f} at alpha = {alpha[idx_eff]:.1f} deg")
