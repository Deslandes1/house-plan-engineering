import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties
import numpy as np

st.set_page_config(
    page_title="Architectural House Plan",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Architectural House Plan")
st.markdown("Switch between the **Engineering Blueprint** and the **3D Interactive Model**.")

# ---------- SIDEBAR TOGGLE ----------
view = st.sidebar.radio("Select view:", ["2D Blueprint", "3D Model"])

# ---------- 2D DRAWING FUNCTION ----------
def draw_house_plan():
    fig, ax = plt.subplots(figsize=(14, 11), facecolor='white')
    ax.set_facecolor('white')
    
    ax.set_xlim(-5, 25)
    ax.set_ylim(-5, 18)
    ax.set_aspect('equal')
    ax.grid(True, which='both', color='#E0E0E0', linestyle='-', linewidth=0.5)
    
    # 1. LAND & EXTERIOR
    ax.plot([-3, 21, 21, -3, -3], [-2, -2, 14, 14, -2], color='black', linestyle='-.', linewidth=1)
    ax.add_patch(patches.Rectangle((18, 0), 5, 8, fill=False, hatch='///', color='#666666', alpha=0.4))

    # Porch & Doghouse
    ax.add_patch(patches.Rectangle((3, -2), 4, 2, facecolor='#F5F5DC', edgecolor='black', linewidth=1.5))
    ax.add_patch(patches.Rectangle((13.5, 13.5), 1.0, 1.2, facecolor='none', edgecolor='black'))

    # 2. THE HOUSE STRUCTURE (Fixed Capstyle Error)
    outer_walls = [((0,0), (18,0)), ((18,0), (18,12)), ((18,12), (0,12)), ((0,12), (0,0))]
    for (x1,y1), (x2,y2) in outer_walls:
        # Changed 'square' to CapStyle.projecting or simply removed to avoid Enum issues
        ax.plot([x1, x2], [y1, y2], color='black', linewidth=5)

    # Balcony Outline in 2D
    ax.plot([-0.5, 18.5, 18.5, -0.5, -0.5], [-0.5, -0.5, 12.5, 12.5, -0.5], 
            color='red', linestyle='--', linewidth=1, alpha=0.6)

    # Inner walls
    ax.plot([10, 10], [0, 7], 'k-', linewidth=4)
    ax.plot([10, 18], [7, 7], 'k-', linewidth=4)
    ax.plot([14, 18], [4, 4], 'k-', linewidth=4)
    ax.plot([14, 14], [4, 7], 'k-', linewidth=4)

    # 3. ANNOTATIONS
    font_rooms = FontProperties(weight='bold', size=10)
    ax.text(5, 6, "LIVING ROOM", ha='center', fontproperties=font_rooms)
    ax.text(14, 3, "KITCHEN", ha='center', fontproperties=font_rooms)
    ax.text(14, 9.5, "BEDROOM 1", ha='center', fontproperties=font_rooms)
    ax.text(6, 9.5, "BEDROOM 2", ha='center', fontproperties=font_rooms)
    
    ax.axis('off')
    return fig

# ---------- 3D VIEW (With Balcony Restored) ----------
def generate_3d_house():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>body { margin: 0; overflow: hidden; } #info { position: absolute; top: 10px; left: 10px; color: white; background: rgba(0,0,0,0.5); padding: 8px; font-family: sans-serif; z-index:10; }</style>
    </head>
    <body>
        <div id="info">3D Model: House + Balcony Terrace</div>
        <script type="importmap">
            { "imports": { "three": "https://unpkg.com/three@0.128.0/build/three.module.js", "three/addons/": "https://unpkg.com/three@0.128.0/examples/jsm/" } }
        </script>
        <script type="module">
            import * as THREE from 'three';
            import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x222233);
            const camera = new THREE.PerspectiveCamera(45, window.innerWidth/window.innerHeight, 0.1, 1000);
            camera.position.set(25, 20, 25);

            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.body.appendChild(renderer.domElement);

            const controls = new OrbitControls(camera, renderer.domElement);
            const ambient = new THREE.AmbientLight(0xffffff, 0.6); scene.add(ambient);
            const sun = new THREE.DirectionalLight(0xffffff, 0.8); sun.position.set(10,20,10); scene.add(sun);

            // Ground
            const grass = new THREE.Mesh(new THREE.PlaneGeometry(50, 50), new THREE.MeshStandardMaterial({color: 0x335533}));
            grass.rotation.x = -Math.PI/2; scene.add(grass);

            // Walls (Ground Floor)
            const wallMat = new THREE.MeshStandardMaterial({color: 0xdddddd});
            function wall(x, z, w, d, h=3) {
                const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), wallMat);
                m.position.set(x, h/2, z); scene.add(m);
            }
            wall(9, 0, 18, 0.2); wall(9, 12, 18, 0.2); wall(0, 6, 0.2, 12); wall(18, 6, 0.2, 12);

            // --- THE BALCONY (Second Level) ---
            const balconyMat = new THREE.MeshStandardMaterial({color: 0x8899aa, transparent: true, opacity: 0.8});
            const balconyFloor = new THREE.Mesh(new THREE.BoxGeometry(19, 0.2, 13), balconyMat);
            balconyFloor.position.set(9, 3.1, 6); // Placed on top of walls
            scene.add(balconyFloor);

            // Balcony Railings
            const railMat = new THREE.MeshStandardMaterial({color: 0x333333});
            function rail(x, z, w, d) {
                const m = new THREE.Mesh(new THREE.BoxGeometry(w, 1, d), railMat);
                m.position.set(x, 3.6, z); scene.add(m);
            }
            rail(9, -0.5, 19, 0.05); rail(9, 12.5, 19, 0.05); rail(-0.5, 6, 0.05, 13); rail(18.5, 6, 0.05, 13);

            // Parking
            const parking = new THREE.Mesh(new THREE.PlaneGeometry(5, 8), new THREE.MeshStandardMaterial({color: 0x444444}));
            parking.rotation.x = -Math.PI/2; parking.position.set(20.5, 0.01, 4); scene.add(parking);

            function animate() { requestAnimationFrame(animate); controls.update(); renderer.render(scene, camera); }
            animate();
        </script>
    </body>
    </html>
    """

if view == "2D Blueprint":
    st.pyplot(draw_house_plan())
else:
    components.html(generate_3d_house(), height=700)
