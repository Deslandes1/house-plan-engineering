import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties
import numpy as np

st.set_page_config(
    page_title="House Plan Generator | Engineering Drawing",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Architectural House Plan")
st.markdown("Engineer‑style drawing with walls, doors, windows & dimensions.")

# ---------- DRAWING FUNCTION ----------
def draw_house_plan():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(-1, 20)
    ax.set_ylim(-1, 15)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_xlabel("Meters (or feet)", fontsize=10)
    ax.set_ylabel("Meters (or feet)", fontsize=10)
    ax.set_title("House Plan – Ground Floor", fontsize=14, fontweight='bold')

    # ---------- OUTER WALLS (thick lines) ----------
    # Outer rectangle: from (0,0) to (18,12)
    walls = [((0,0), (18,0)), ((18,0), (18,12)), ((18,12), (0,12)), ((0,12), (0,0))]
    for (x1,y1), (x2,y2) in walls:
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=4, solid_capstyle='round')

    # ---------- INNER WALLS (partitions) ----------
    # Vertical wall at x=10 from y=0 to y=7 (separates living & kitchen)
    ax.plot([10, 10], [0, 7], 'k-', linewidth=4)
    # Horizontal wall from x=10 to x=18 at y=7 (separates bedrooms)
    ax.plot([10, 18], [7, 7], 'k-', linewidth=4)
    # Bathroom walls (small room bottom‑right)
    ax.plot([14, 18], [4, 4], 'k-', linewidth=4)   # bottom wall of bathroom
    ax.plot([14, 14], [4, 7], 'k-', linewidth=4)   # left wall of bathroom

    # ---------- DOORS (arcs) ----------
    # Door from living to kitchen (at x=10, y=3, opening to the right)
    door1 = patches.Arc((10, 3), 1.2, 1.2, theta1=270, theta2=360, linewidth=2, color='blue')
    ax.add_patch(door1)
    ax.plot([10, 10.6], [3, 3], 'b-', linewidth=2)  # door line

    # Door from kitchen to hallway (at x=14, y=7, opening up)
    door2 = patches.Arc((14, 7), 1.2, 1.2, theta1=0, theta2=90, linewidth=2, color='blue')
    ax.add_patch(door2)
    ax.plot([14, 14], [7, 7.6], 'b-', linewidth=2)

    # Door to bedroom 1 (at x=10, y=8.5, opening right)
    door3 = patches.Arc((10, 8.5), 1.2, 1.2, theta1=270, theta2=360, linewidth=2, color='blue')
    ax.add_patch(door3)
    ax.plot([10, 10.6], [8.5, 8.5], 'b-', linewidth=2)

    # Door to bedroom 2 (at x=16, y=7, opening up)
    door4 = patches.Arc((16, 7), 1.2, 1.2, theta1=0, theta2=90, linewidth=2, color='blue')
    ax.add_patch(door4)
    ax.plot([16, 16], [7, 7.6], 'b-', linewidth=2)

    # Door to bathroom (at x=14, y=4, opening down)
    door5 = patches.Arc((14, 4), 1.2, 1.2, theta1=90, theta2=180, linewidth=2, color='blue')
    ax.add_patch(door5)
    ax.plot([14, 14], [4, 3.4], 'b-', linewidth=2)

    # ---------- WINDOWS (thin rectangles on walls) ----------
    # Window on left wall (living room) – from y=4 to y=6
    ax.plot([0, 0], [4, 6], 'b-', linewidth=3)
    # Window on bottom wall (kitchen) – from x=11 to x=13
    ax.plot([11, 13], [0, 0], 'b-', linewidth=3)
    # Window on top wall (bedroom 2) – from x=12 to x=14
    ax.plot([12, 14], [12, 12], 'b-', linewidth=3)
    # Window on right wall (bedroom 1) – from y=9 to y=11
    ax.plot([18, 18], [9, 11], 'b-', linewidth=3)

    # ---------- ROOM LABELS ----------
    font = FontProperties(weight='bold', size=10)
    ax.text(5, 6, "LIVING ROOM", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(14, 3, "KITCHEN", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(14, 9.5, "BEDROOM 1", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(6, 9.5, "BEDROOM 2", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(16, 5.5, "BATH", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(2, 0.8, "ENTRY", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))

    # ---------- DIMENSIONS (simple with arrows) ----------
    # Overall width (0 to 18) at y = -1
    ax.annotate('', xy=(0, -1), xytext=(18, -1), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(9, -1.5, "18.0 m", ha='center', va='center', color='red', fontsize=9)
    # Overall height (0 to 12) at x = 19
    ax.annotate('', xy=(19, 0), xytext=(19, 12), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(19.5, 6, "12.0 m", ha='center', va='center', color='red', fontsize=9, rotation=90)

    # Additional dimension: width of living room (to x=10) at y = -1.2
    ax.annotate('', xy=(0, -1.2), xytext=(10, -1.2), arrowprops=dict(arrowstyle='<->', color='red', lw=1))
    ax.text(5, -1.7, "10.0 m", ha='center', color='red', fontsize=8)

    return fig

# ---------- STREAMLIT OUTPUT ----------
fig = draw_house_plan()
st.pyplot(fig)

st.markdown("""
---
### 📐 Legend
- **Black thick lines** = Walls  
- **Blue arcs & lines** = Doors (arc shows swing direction)  
- **Blue thick segments** = Windows  
- **Red arrows** = Dimensions  
- **Dashed grid** = 1‑meter reference  
""")

with st.expander("ℹ️ How to interpret this drawing"):
    st.markdown("""
    - This is a **2D top‑down view** (architectural plan).  
    - All measurements are in **meters** (you can mentally convert to feet by multiplying by 3.28).  
    - Doors are shown as quarter‑circles indicating the swing direction.  
    - Windows are drawn as thickened segments on the wall lines.  
    - The grid helps estimate distances.  
    - Engineers use similar conventions for preliminary floor plans.
    """)
