import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# NACA 6412 F1 Front Wing — Ground Effect Study
# XFLR5 v6.62 | VLM2 | Inviscid | Re = 1,000,000 | alpha = 5 deg
# ============================================================

hc = np.array([1.0, 0.5, 0.3, 0.2, 0.1])
cl = np.array([0.940864, 1.037412, 1.171277, 1.331610, 1.734936])
cd = np.array([0.024658, 0.021031, 0.019436, 0.018794, 0.018030])
cl_cd = cl / cd

NAVY  = "#1A3A5C"
GOLD  = "#E6A817"
TEAL  = "#2E8B8B"
RED   = "#C0392B"

plt.rcParams.update({'font.family': 'DejaVu Sans', 'axes.spines.top': False,
                      'axes.spines.right': False})

# Note: h/c decreases as wing approaches ground, so we invert x-axis
# to visually read left-to-right as "approaching ground"

# ------------------------------------------------------------
# GRAPH 1 — Cl vs h/c
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(hc, cl, 'o-', color=NAVY, linewidth=2.5, markersize=9, zorder=3)
for x, y in zip(hc, cl):
    ax.annotate(f'{y:.3f}', (x, y), textcoords='offset points', xytext=(0, 10),
                ha='center', fontsize=9, fontweight='bold', color=NAVY)
ax.invert_xaxis()
ax.set_xlabel('Ground Clearance Ratio, h/c', fontsize=11)
ax.set_ylabel('Lift Coefficient, $C_L$', fontsize=11)
ax.set_title('Lift Coefficient vs Ground Clearance\nNACA 6412 F1 Front Wing | $\\alpha$ = 5°, Re = 1,000,000',
             fontsize=11, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.4)
ax.axvspan(0, 0.3, alpha=0.06, color='orange')
ax.text(0.15, cl.min()-0.03, 'Real F1 ride-height\nrange', fontsize=8, color='gray', ha='center')
plt.tight_layout()
plt.savefig('cl_vs_hc.png', dpi=150, bbox_inches='tight')
plt.close()

# ------------------------------------------------------------
# GRAPH 2 — Cd vs h/c
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(hc, cd, 's-', color=RED, linewidth=2.5, markersize=9, zorder=3)
for x, y in zip(hc, cd):
    ax.annotate(f'{y:.4f}', (x, y), textcoords='offset points', xytext=(0, 10),
                ha='center', fontsize=9, fontweight='bold', color=RED)
ax.invert_xaxis()
ax.set_xlabel('Ground Clearance Ratio, h/c', fontsize=11)
ax.set_ylabel('Drag Coefficient, $C_D$', fontsize=11)
ax.set_title('Drag Coefficient vs Ground Clearance\nNACA 6412 F1 Front Wing | $\\alpha$ = 5°, Re = 1,000,000',
             fontsize=11, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('cd_vs_hc.png', dpi=150, bbox_inches='tight')
plt.close()

# ------------------------------------------------------------
# GRAPH 3 — Cl/Cd (efficiency) vs h/c
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(hc, cl_cd, '^-', color=TEAL, linewidth=2.5, markersize=9, zorder=3)
for x, y in zip(hc, cl_cd):
    ax.annotate(f'{y:.1f}', (x, y), textcoords='offset points', xytext=(0, 10),
                ha='center', fontsize=9, fontweight='bold', color=TEAL)
ax.invert_xaxis()
ax.set_xlabel('Ground Clearance Ratio, h/c', fontsize=11)
ax.set_ylabel('Aerodynamic Efficiency, $C_L/C_D$', fontsize=11)
ax.set_title('Aerodynamic Efficiency vs Ground Clearance\nNACA 6412 F1 Front Wing | $\\alpha$ = 5°, Re = 1,000,000',
             fontsize=11, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('clcd_vs_hc.png', dpi=150, bbox_inches='tight')
plt.close()

# ------------------------------------------------------------
# GRAPH 4 — Combined Cl and Cd on dual axis
# ------------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(8.5, 5.5))
ax2 = ax1.twinx()

l1, = ax1.plot(hc, cl, 'o-', color=NAVY, linewidth=2.5, markersize=9, label='$C_L$')
l2, = ax2.plot(hc, cd, 's--', color=RED, linewidth=2.5, markersize=9, label='$C_D$')

ax1.set_xlabel('Ground Clearance Ratio, h/c', fontsize=11)
ax1.set_ylabel('Lift Coefficient, $C_L$', fontsize=11, color=NAVY)
ax2.set_ylabel('Drag Coefficient, $C_D$', fontsize=11, color=RED)
ax1.tick_params(axis='y', labelcolor=NAVY)
ax2.tick_params(axis='y', labelcolor=RED)
ax1.invert_xaxis()
ax1.set_title('Lift and Drag Coefficient vs Ground Clearance (Dual Axis)\nNACA 6412 F1 Front Wing | $\\alpha$ = 5°',
              fontsize=11, fontweight='bold')
ax1.legend(handles=[l1, l2], loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('cl_cd_dual_axis.png', dpi=150, bbox_inches='tight')
plt.close()

# ------------------------------------------------------------
# GRAPH 5 — Drag Polar (Cd vs Cl) colored by h/c
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
sc = ax.scatter(cd, cl, c=hc, cmap='viridis_r', s=140, edgecolors=NAVY, linewidths=1.5, zorder=3)
ax.plot(cd, cl, '-', color='gray', alpha=0.5, linewidth=1.5, zorder=2)
for x, y, h in zip(cd, cl, hc):
    ax.annotate(f'h/c={h}', (x, y), textcoords='offset points', xytext=(8, 5),
                fontsize=8, color=NAVY)
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label('h/c', fontsize=10)
ax.set_xlabel('Drag Coefficient, $C_D$', fontsize=11)
ax.set_ylabel('Lift Coefficient, $C_L$', fontsize=11)
ax.set_title('Drag Polar Across Ground Clearance Sweep\nNACA 6412 F1 Front Wing | $\\alpha$ = 5°',
             fontsize=11, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('drag_polar_hc.png', dpi=150, bbox_inches='tight')
plt.close()

# ------------------------------------------------------------
# GRAPH 6 — Percentage change in Cl and Cd relative to h/c=1.0 baseline
# ------------------------------------------------------------
cl_pct = (cl / cl[0] - 1) * 100
cd_pct = (cd / cd[0] - 1) * 100

fig, ax = plt.subplots(figsize=(8, 5))
w = 0.06
x_pos = hc
ax.bar(x_pos - 0.012, cl_pct, width=0.022, color=NAVY, label='$C_L$ % change', zorder=3)
ax.bar(x_pos + 0.012, cd_pct, width=0.022, color=RED, label='$C_D$ % change', zorder=3)
ax.axhline(0, color='black', linewidth=0.8)
ax.invert_xaxis()
ax.set_xlabel('Ground Clearance Ratio, h/c', fontsize=11)
ax.set_ylabel('% Change from h/c = 1.0 Baseline', fontsize=11)
ax.set_title('Relative Change in $C_L$ and $C_D$ vs Ground Clearance\nNACA 6412 F1 Front Wing | $\\alpha$ = 5°',
             fontsize=11, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, linestyle='--', alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('percent_change_vs_hc.png', dpi=150, bbox_inches='tight')
plt.close()

# ------------------------------------------------------------
# GRAPH 7 — Rate of change (slope) of Cl between consecutive h/c points
# ------------------------------------------------------------
dCl = np.diff(cl)
dhc = np.diff(hc)
slope = dCl / dhc  # will be negative since hc decreases; take -slope for "Cl gain per unit h/c reduction"
gain_per_step = -slope
midpoints = (hc[:-1] + hc[1:]) / 2

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar([f'{hc[i]:.1f}→{hc[i+1]:.1f}' for i in range(len(hc)-1)], gain_per_step,
       color=GOLD, edgecolor=NAVY, zorder=3)
for i, v in enumerate(gain_per_step):
    ax.text(i, v + 0.03, f'{v:.2f}', ha='center', fontsize=9, fontweight='bold', color=NAVY)
ax.set_xlabel('h/c Transition', fontsize=11)
ax.set_ylabel('$\\Delta C_L$ per unit reduction in h/c', fontsize=11)
ax.set_title('Sensitivity of Lift to Ground Clearance Reduction\nNACA 6412 F1 Front Wing | $\\alpha$ = 5°',
             fontsize=11, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('cl_sensitivity_vs_hc.png', dpi=150, bbox_inches='tight')
plt.close()

# ------------------------------------------------------------
# GRAPH 8 — Combined dashboard (2x2)
# ------------------------------------------------------------
fig, axs = plt.subplots(2, 2, figsize=(12, 9))

axs[0,0].plot(hc, cl, 'o-', color=NAVY, linewidth=2.5, markersize=8)
axs[0,0].invert_xaxis()
axs[0,0].set_xlabel('h/c'); axs[0,0].set_ylabel('$C_L$')
axs[0,0].set_title('Lift Coefficient vs h/c', fontweight='bold')
axs[0,0].grid(True, linestyle='--', alpha=0.4)

axs[0,1].plot(hc, cd, 's-', color=RED, linewidth=2.5, markersize=8)
axs[0,1].invert_xaxis()
axs[0,1].set_xlabel('h/c'); axs[0,1].set_ylabel('$C_D$')
axs[0,1].set_title('Drag Coefficient vs h/c', fontweight='bold')
axs[0,1].grid(True, linestyle='--', alpha=0.4)

axs[1,0].plot(hc, cl_cd, '^-', color=TEAL, linewidth=2.5, markersize=8)
axs[1,0].invert_xaxis()
axs[1,0].set_xlabel('h/c'); axs[1,0].set_ylabel('$C_L/C_D$')
axs[1,0].set_title('Efficiency vs h/c', fontweight='bold')
axs[1,0].grid(True, linestyle='--', alpha=0.4)

sc = axs[1,1].scatter(cd, cl, c=hc, cmap='viridis_r', s=120, edgecolors=NAVY, linewidths=1.2)
axs[1,1].plot(cd, cl, '-', color='gray', alpha=0.5)
axs[1,1].set_xlabel('$C_D$'); axs[1,1].set_ylabel('$C_L$')
axs[1,1].set_title('Drag Polar', fontweight='bold')
axs[1,1].grid(True, linestyle='--', alpha=0.4)
plt.colorbar(sc, ax=axs[1,1], label='h/c')

fig.suptitle('NACA 6412 F1 Front Wing — Ground Effect Study Summary\nXFLR5 VLM2 | Re = 1,000,000 | $\\alpha$ = 5°',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig('ground_effect_dashboard.png', dpi=150, bbox_inches='tight')
plt.close()

print("All 8 graphs generated successfully:")
print("1. cl_vs_hc.png")
print("2. cd_vs_hc.png")
print("3. clcd_vs_hc.png")
print("4. cl_cd_dual_axis.png")
print("5. drag_polar_hc.png")
print("6. percent_change_vs_hc.png")
print("7. cl_sensitivity_vs_hc.png")
print("8. ground_effect_dashboard.png")
