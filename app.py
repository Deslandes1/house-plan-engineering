import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties
import numpy as np

st.set_page_config(
    page_title="House Plan | 2D Blueprint & 3D Model",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Architectural House Plan")
st.markdown("Switch between **2D engineering drawing** and **3D interactive model**.")

# ---------- SIDEBAR TOGGLE ----------
view = st.sidebar.radio("Select view:", ["2D Blueprint", "3D Model"])

# ---------- 2D DRAWING FUNCTION (The Engineer's Master Plan) ----------
def draw_house_plan():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(-5, 25)
    ax.set_ylim(-5, 18)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_xlabel("Meters", fontsize=10)
    ax.set_ylabel("Meters", fontsize=10)
    ax.set_title("House Plan – Ground Floor (Engineer Drawing)", fontsize=14, fontweight='bold')

    # Outer walls (house footprint) - EXACT same coordinates used in 3D
    walls = [((0,0), (18,0)), ((18,0), (18,12)), ((18,12), (0,12)), ((0,12), (0,0))]
    for (x1,y1), (x2,y2) in walls:
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=4, solid_capstyle='round')

    # Inner walls
    ax.plot([10, 10], [0, 7], 'k-', linewidth=4)
    ax.plot([10, 18], [7, 7], 'k-', linewidth=4)
    ax.plot([14, 18], [4, 4], 'k-', linewidth=4)
    ax.plot([14, 14], [4, 7], 'k-', linewidth=4)

    # Doors (arcs)
    doors = [(10, 3, 270, 360, 10, 10.6, 3, 3), (14, 7, 0, 90, 14, 14, 7, 7.6), 
             (10, 8.5, 270, 360, 10, 10.6, 8.5, 8.5), (16, 7, 0, 90, 16, 16, 7, 7.6),
             (14, 4, 90, 180, 14, 14, 4, 3.4)]
    
    for cx, cy, t1, t2, x1, x2, y1, y2 in doors:
        ax.add_patch(patches.Arc((cx, cy), 1.2, 1.2, theta1=t1, theta2=t2, linewidth=2, color='blue'))
        ax.plot([x1, x2], [y1, y2], 'b-', linewidth=2)

    # Windows
    ax.plot([0, 0], [4, 6], 'b-', linewidth=3)
    ax.plot([11, 13], [0, 0], 'b-', linewidth=3)
    ax.plot([12, 14], [12, 12], 'b-', linewidth=3)
    ax.plot([18, 18], [9, 11], 'b-', linewidth=3)

    # Labels
    font = FontProperties(weight='bold', size=10)
    ax.text(5, 6, "LIVING ROOM", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(14, 3, "KITCHEN", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(14, 9.5, "BEDROOM 1", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(6, 9.5, "BEDROOM 2", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(16, 5.5, "BATH", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(2, 0.8, "ENTRY", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))

    # Yard boundaries
    ax.plot([-3, -3], [-2, 14], 'g--', linewidth=1, alpha=0.6)
    ax.plot([21, 21], [-2, 14], 'g--', linewidth=1, alpha=0.6)
    ax.plot([-3, 21], [14, 14], 'g--', linewidth=1, alpha=0.6)
    ax.plot([-3, 21], [-2, -2], 'g--', linewidth=1, alpha=0.6)

    return fig

# ---------- 3D VIEW (Three.js) SYNCHRONIZED WITH 2D PLAN ----------
def generate_3d_house():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; overflow: hidden; }
            #info {
                position: absolute; top: 20px; left: 20px; color: white;
                background: rgba(0,0,0,0.7); padding: 15px; border-radius: 8px;
                font-family: 'Segoe UI', sans-serif; pointer-events: none; z-index: 100;
                border-left: 5px solid #4da6ff;
            }
        </style>
    </head>
    <body>
        <div id="info">
            <strong>🏠 Synchronized 3D Model</strong><br>
            Matched to 2D Blueprint Specifications<br>
            ✅ Same Room Layout | ✅ Added Roof Balcony | ✅ All Assets Kept
        </div>
        <script type="importmap">
            {
                "imports": {
                    "three": "https://unpkg.com/three@0.128.0/build/three.module.js",
                    "three/addons/": "https://unpkg.com/three@0.128.0/examples/jsm/"
                }
            }
        </script>
        <script type="module">
            import * as THREE from 'three';
            import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
            import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';

            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x111122);

            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(28, 22, 28);

            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.shadowMap.enabled = true;
            document.body.appendChild(renderer.domElement);

            const labelRenderer = new CSS2DRenderer();
            labelRenderer.setSize(window.innerWidth, window.innerHeight);
            labelRenderer.domElement.style.position = 'absolute';
            labelRenderer.domElement.style.top = '0px';
            labelRenderer.domElement.style.pointerEvents = 'none';
            document.body.appendChild(labelRenderer.domElement);

            const controls = new OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.target.set(9, 2, 6);

            // Lighting
            scene.add(new THREE.AmbientLight(0x606080));
            const sun = new THREE.DirectionalLight(0xffffff, 1.2);
            sun.position.set(20, 30, 10);
            sun.castShadow = true;
            scene.add(sun);

            // Ground / Yards (Matching Blueprint boundaries)
            const grassMat = new THREE.MeshStandardMaterial({ color: 0x3d5a37 });
            const ground = new THREE.Mesh(new THREE.PlaneGeometry(24, 16), grassMat);
            ground.rotation.x = -Math.PI/2;
            ground.position.set(9, -0.05, 6); // Centered to match 2D coord system
            ground.receiveShadow = true;
            scene.add(ground);

            // Parking Asphalt
            const parking = new THREE.Mesh(new THREE.PlaneGeometry(5, 8), new THREE.MeshStandardMaterial({ color: 0x333333 }));
            parking.rotation.x = -Math.PI/2;
            parking.position.set(20.5, -0.04, 4);
            scene.add(parking);

            // Fence (Property Line)
            const fenceMat = new THREE.MeshStandardMaterial({ color: 0x8b5a2b });
            function addFencePost(x, z) {
                const post = new THREE.Mesh(new THREE.BoxGeometry(0.2, 1.2, 0.2), fenceMat);
                post.position.set(x, 0.6, z); scene.add(post);
            }
            // Corners of the property
            [[-3,-2], [21,-2], [21,14], [-3,14]].forEach(p => addFencePost(p[0], p[1]));

            // --- HOUSE WALLS (Direct mapping from 2D coordinates) ---
            const wallMat = new THREE.MeshStandardMaterial({ color: 0xcdc9c9 });
            const h = 3.0; // Wall height
            function wall(x, z, w, d, ry=0) {
                const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), wallMat);
                m.position.set(x, h/2, z); m.rotation.y = ry;
                m.castShadow = true; m.receiveShadow = true; scene.add(m);
            }
            // Outer Footprint
            wall(9, 0, 18, 0.3); wall(18, 6, 0.3, 12); wall(9, 12, 18, 0.3); wall(0, 6, 0.3, 12);
            // Inner Partitions
            wall(10, 3.5, 0.3, 7); wall(14, 7, 8, 0.3); wall(16, 4, 4, 0.3); wall(14, 5.5, 0.3, 3);

            // Doors
            const doorMat = new THREE.MeshStandardMaterial({ color: 0x8B5A2B });
            const entryDoor = new THREE.Mesh(new THREE.BoxGeometry(1.2, 2.2, 0.1), doorMat);
            entryDoor.position.set(5, 1.1, 0); scene.add(entryDoor);

            // --- BALCONY ADDITION ---
            // The Roof / Balcony Floor
            const balconyFloor = new THREE.Mesh(new THREE.BoxGeometry(18.4, 0.2, 12.4), new THREE.MeshStandardMaterial({ color: 0x777777 }));
            balconyFloor.position.set(9, 3.1, 6);
            scene.add(balconyFloor);

            // Perimeter Railings (Glass + Metal Frame)
            const glassMat = new THREE.MeshStandardMaterial({ color: 0x88ccff, transparent: true, opacity: 0.5 });
            function addRail(x, z, w, d) {
                const g = new THREE.Mesh(new THREE.BoxGeometry(w, 1.1, d), glassMat);
                g.position.set(x, 3.7, z); scene.add(g);
                const frame = new THREE.Mesh(new THREE.BoxGeometry(w, 0.05, d+0.05), new THREE.MeshStandardMaterial({color: 0x222222}));
                frame.position.set(x, 4.25, z); scene.add(frame);
            }
            addRail(9, 0, 18.4, 0.1); addRail(18.2, 6, 0.1, 12.4); addRail(9, 12.2, 18.4, 0.1); addRail(-0.2, 6, 0.1, 12.4);

            // Porch & Doghouse
            const porch = new THREE.Mesh(new THREE.BoxGeometry(4, 0.2, 2.5), new THREE.MeshStandardMaterial({ color: 0xc2b280 }));
            porch.position.set(5, 0.1, -1.2); scene.add(porch);

            const doghouse = new THREE.Mesh(new THREE.BoxGeometry(1.2, 1, 1.2), new THREE.MeshStandardMaterial({ color: 0x8b4513 }));
            doghouse.position.set(14, 0.5, 14); scene.add(doghouse);

            // Synchronized Labels
            function label(text, x, z, y=0.5) {
                const div = document.createElement('div'); div.textContent = text;
                div.style.color = '#fff'; div.style.background = 'rgba(0,0,0,0.6)';
                div.style.padding = '2px 10px'; div.style.borderRadius = '10px';
                const obj = new CSS2DObject(div); obj.position.set(x, y, z); scene.add(obj);
            }
            label('LIVING ROOM', 5, 6); label('KITCHEN', 14, 3); label('BEDROOM 1', 14, 9.5);
            label('BEDROOM 2', 6, 9.5); label('BALCONY (ROOF)', 9, 6, 4.5);

            function animate() {
                requestAnimationFrame(animate);
                controls.update();
                renderer.render(scene, camera);
                labelRenderer.render(scene, camera);
            }
            animate();
            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
                labelRenderer.setSize(window.innerWidth, window.innerHeight);
            });
        </script>
    </body>
    </html>
    """

# ---------- RENDER ----------
if view == "2D Blueprint":
    st.pyplot(draw_house_plan())
    st.info("💡 This blueprint serves as the exact coordinate map for the 3D model.")
else:
    st.markdown("### 🏡 Interactive 3D Model (Sync with Blueprint)")
    components.html(generate_3d_house(), height=750, scrolling=False)
