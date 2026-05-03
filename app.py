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

# ---------- 2D DRAWING FUNCTION ----------
def draw_house_plan():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(-5, 25)
    ax.set_ylim(-5, 18)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_xlabel("Meters", fontsize=10)
    ax.set_ylabel("Meters", fontsize=10)
    ax.set_title("House Plan – Ground Floor", fontsize=14, fontweight='bold')

    # Outer walls
    walls = [((0,0), (18,0)), ((18,0), (18,12)), ((18,12), (0,12)), ((0,12), (0,0))]
    for (x1,y1), (x2,y2) in walls:
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=4, solid_capstyle='round')

    # Inner walls
    ax.plot([10, 10], [0, 7], 'k-', linewidth=4)
    ax.plot([10, 18], [7, 7], 'k-', linewidth=4)
    ax.plot([14, 18], [4, 4], 'k-', linewidth=4)
    ax.plot([14, 14], [4, 7], 'k-', linewidth=4)

    # Room labels (Simplified for brevity)
    font = FontProperties(weight='bold', size=10)
    ax.text(5, 6, "LIVING ROOM", ha='center', va='center', fontproperties=font)
    ax.text(14, 3, "KITCHEN", ha='center', va='center', fontproperties=font)
    ax.text(14, 9.5, "BEDROOM 1", ha='center', va='center', fontproperties=font)

    # Property lines
    ax.plot([-3, 21], [14, 14], 'g--', linewidth=1, alpha=0.6)
    ax.plot([-3, 21], [-2, -2], 'g--', linewidth=1, alpha=0.6)

    return fig

# ---------- 3D VIEW (Three.js) WITH BALCONY ----------
def generate_3d_house():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; overflow: hidden; background-color: #111122; }
            #info {
                position: absolute; top: 20px; left: 20px; color: white;
                background: rgba(0,0,0,0.7); padding: 12px; border-radius: 8px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                pointer-events: none; z-index: 100; border-left: 4px solid #4da6ff;
            }
        </style>
    </head>
    <body>
        <div id="info">
            <strong>🏠 Modern House + Roof Balcony</strong><br>
            • Orbit: Left Click | Pan: Right Click<br>
            • Features: Balcony, Doghouse, Porch, Parking
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

            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x1a1a2e);

            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(28, 20, 28);

            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.shadowMap.enabled = true;
            document.body.appendChild(renderer.domElement);

            const controls = new OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.target.set(9, 2, 6);

            // Lights
            const ambient = new THREE.AmbientLight(0xffffff, 0.5);
            scene.add(ambient);
            const sun = new THREE.DirectionalLight(0xffffff, 1.0);
            sun.position.set(20, 40, 20);
            sun.castShadow = true;
            scene.add(sun);

            // Ground & Yards
            const grass = new THREE.Mesh(new THREE.PlaneGeometry(60, 60), new THREE.MeshStandardMaterial({ color: 0x3d5a37 }));
            grass.rotation.x = -Math.PI/2;
            grass.receiveShadow = true;
            scene.add(grass);

            // Parking
            const drive = new THREE.Mesh(new THREE.PlaneGeometry(6, 10), new THREE.MeshStandardMaterial({ color: 0x333333 }));
            drive.rotation.x = -Math.PI/2;
            drive.position.set(21, 0.01, 5);
            scene.add(drive);

            // Walls
            const wallMat = new THREE.MeshStandardMaterial({ color: 0xeaeaea });
            function createWall(x, z, w, d, h=3) {
                const wall = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), wallMat);
                wall.position.set(x, h/2, z);
                wall.castShadow = true;
                wall.receiveShadow = true;
                scene.add(wall);
            }
            createWall(9, 0, 18, 0.3); createWall(18, 6, 0.3, 12); createWall(9, 12, 18, 0.3); createWall(0, 6, 0.3, 12);

            // --- THE BALCONY ADDITION ---
            // 1. Roof Floor
            const roofFloor = new THREE.Mesh(new THREE.BoxGeometry(18.2, 0.2, 12.2), new THREE.MeshStandardMaterial({ color: 0x777777 }));
            roofFloor.position.set(9, 3.1, 6);
            roofFloor.receiveShadow = true;
            scene.add(roofFloor);

            // 2. Balcony Railings
            const railMat = new THREE.MeshStandardMaterial({ color: 0x88ccff, transparent: true, opacity: 0.5 });
            const frameMat = new THREE.MeshStandardMaterial({ color: 0x222222 });

            function addRailing(x, z, w, d) {
                const glass = new THREE.Mesh(new THREE.BoxGeometry(w, 1.1, d), railMat);
                glass.position.set(x, 3.7, z);
                scene.add(glass);
                const frame = new THREE.Mesh(new THREE.BoxGeometry(w + 0.05, 0.1, d + 0.05), frameMat);
                frame.position.set(x, 4.2, z);
                scene.add(frame);
            }
            // Front, Back, and Left railings
            addRailing(9, 0.1, 18, 0.05); 
            addRailing(9, 11.9, 18, 0.05);
            addRailing(0.1, 6, 0.05, 12);

            // Doghouse
            const doghouse = new THREE.Mesh(new THREE.BoxGeometry(1.2, 1, 1.2), new THREE.MeshStandardMaterial({ color: 0x8b4513 }));
            doghouse.position.set(14, 0.5, 14);
            scene.add(doghouse);

            // Porch
            const porch = new THREE.Mesh(new THREE.BoxGeometry(4, 0.2, 2.5), new THREE.MeshStandardMaterial({ color: 0xbbbbbb }));
            porch.position.set(5, 0.1, -1.5);
            scene.add(porch);

            function animate() {
                requestAnimationFrame(animate);
                controls.update();
                renderer.render(scene, camera);
            }
            animate();
            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            });
        </script>
    </body>
    </html>
    """

# ---------- DISPLAY ----------
if view == "2D Blueprint":
    st.pyplot(draw_house_plan())
else:
    st.markdown("### 🏡 3D Property View – Rooftop Balcony")
    components.html(generate_3d_house(), height=700, scrolling=False)
