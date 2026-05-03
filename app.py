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

    # Outer walls (house footprint)
    walls = [((0,0), (18,0)), ((18,0), (18,12)), ((18,12), (0,12)), ((0,12), (0,0))]
    for (x1,y1), (x2,y2) in walls:
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=4, solid_capstyle='round')

    # Inner walls
    ax.plot([10, 10], [0, 7], 'k-', linewidth=4)
    ax.plot([10, 18], [7, 7], 'k-', linewidth=4)
    ax.plot([14, 18], [4, 4], 'k-', linewidth=4)
    ax.plot([14, 14], [4, 7], 'k-', linewidth=4)

    # Doors (arcs)
    door1 = patches.Arc((10, 3), 1.2, 1.2, theta1=270, theta2=360, linewidth=2, color='blue')
    ax.add_patch(door1)
    ax.plot([10, 10.6], [3, 3], 'b-', linewidth=2)

    door2 = patches.Arc((14, 7), 1.2, 1.2, theta1=0, theta2=90, linewidth=2, color='blue')
    ax.add_patch(door2)
    ax.plot([14, 14], [7, 7.6], 'b-', linewidth=2)

    door3 = patches.Arc((10, 8.5), 1.2, 1.2, theta1=270, theta2=360, linewidth=2, color='blue')
    ax.add_patch(door3)
    ax.plot([10, 10.6], [8.5, 8.5], 'b-', linewidth=2)

    door4 = patches.Arc((16, 7), 1.2, 1.2, theta1=0, theta2=90, linewidth=2, color='blue')
    ax.add_patch(door4)
    ax.plot([16, 16], [7, 7.6], 'b-', linewidth=2)

    door5 = patches.Arc((14, 4), 1.2, 1.2, theta1=90, theta2=180, linewidth=2, color='blue')
    ax.add_patch(door5)
    ax.plot([14, 14], [4, 3.4], 'b-', linewidth=2)

    # Windows
    ax.plot([0, 0], [4, 6], 'b-', linewidth=3)
    ax.plot([11, 13], [0, 0], 'b-', linewidth=3)
    ax.plot([12, 14], [12, 12], 'b-', linewidth=3)
    ax.plot([18, 18], [9, 11], 'b-', linewidth=3)

    # Room labels
    font = FontProperties(weight='bold', size=10)
    ax.text(5, 6, "LIVING ROOM", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(14, 3, "KITCHEN", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(14, 9.5, "BEDROOM 1", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(6, 9.5, "BEDROOM 2", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(16, 5.5, "BATH", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(2, 0.8, "ENTRY", ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))

    # Dimensions
    ax.annotate('', xy=(0, -1), xytext=(18, -1), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(9, -1.5, "18.0 m", ha='center', va='center', color='red', fontsize=9)
    ax.annotate('', xy=(19, 0), xytext=(19, 12), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(19.5, 6, "12.0 m", ha='center', va='center', color='red', fontsize=9, rotation=90)
    ax.annotate('', xy=(0, -1.2), xytext=(10, -1.2), arrowprops=dict(arrowstyle='<->', color='red', lw=1))
    ax.text(5, -1.7, "10.0 m", ha='center', color='red', fontsize=8)

    # Add yard and parking boundaries
    ax.plot([-3, -3], [-2, 14], 'g--', linewidth=1, alpha=0.6)
    ax.plot([21, 21], [-2, 14], 'g--', linewidth=1, alpha=0.6)
    ax.plot([-3, 21], [14, 14], 'g--', linewidth=1, alpha=0.6)
    ax.plot([-3, 21], [-2, -2], 'g--', linewidth=1, alpha=0.6)

    return fig

# ---------- 3D VIEW (Three.js) ----------
def generate_3d_house():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; overflow: hidden; }
            #info {
                position: absolute; top: 20px; left: 20px; color: white;
                background: rgba(0,0,0,0.6); padding: 10px; border-radius: 8px;
                font-family: Arial, sans-serif; pointer-events: none; z-index: 100;
            }
        </style>
    </head>
    <body>
        <div id="info">
            <strong>3D House Model with Roof Balcony</strong><br>
            Drag to rotate | Right-click to pan | Scroll to zoom<br>
            ✅ Roof Balcony | ✅ Porch | ✅ Yards | ✅ Doghouse
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
            scene.fog = new THREE.FogExp2(0x111122, 0.008);

            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(25, 18, 25);

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

            const ambientLight = new THREE.AmbientLight(0x404060);
            scene.add(ambientLight);
            const dirLight = new THREE.DirectionalLight(0xffffff, 1.2);
            dirLight.position.set(15, 25, 10);
            dirLight.castShadow = true;
            scene.add(dirLight);

            // Ground
            const grassMat = new THREE.MeshStandardMaterial({ color: 0x5a9e4e });
            const ground = new THREE.Mesh(new THREE.PlaneGeometry(60, 60), grassMat);
            ground.rotation.x = -Math.PI/2;
            ground.position.y = -0.2;
            ground.receiveShadow = true;
            scene.add(ground);

            // Parking
            const parking = new THREE.Mesh(new THREE.PlaneGeometry(5, 8), new THREE.MeshStandardMaterial({ color: 0x333333 }));
            parking.rotation.x = -Math.PI/2;
            parking.position.set(20.5, -0.15, 4);
            scene.add(parking);

            // Walls logic
            const wallMat = new THREE.MeshStandardMaterial({ color: 0xcdc9c9 });
            function addWall(x, z, w, d, h=3) {
                const mesh = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), wallMat);
                mesh.position.set(x, h/2, z);
                mesh.castShadow = true;
                mesh.receiveShadow = true;
                scene.add(mesh);
            }
            addWall(9, 0, 18, 0.3); addWall(18, 6, 0.3, 12); addWall(9, 12, 18, 0.3); addWall(0, 6, 0.3, 12);

            // --- ROOF & BALCONY ---
            // Main Roof Slab
            const roofSlabMat = new THREE.MeshStandardMaterial({ color: 0x888888 });
            const roofSlab = new THREE.Mesh(new THREE.BoxGeometry(18.4, 0.3, 12.4), roofSlabMat);
            roofSlab.position.set(9, 3.15, 6);
            roofSlab.receiveShadow = true;
            scene.add(roofSlab);

            // Balcony Railing (Glass/Metal look)
            const railMat = new THREE.MeshStandardMaterial({ color: 0xaaaaff, transparent: true, opacity: 0.4 });
            const postMat = new THREE.MeshStandardMaterial({ color: 0x333333 });
            
            function addRail(x, z, w, d) {
                const rail = new THREE.Mesh(new THREE.BoxGeometry(w, 0.8, d), railMat);
                rail.position.set(x, 3.7, z);
                scene.add(rail);
                const post = new THREE.Mesh(new THREE.BoxGeometry(0.1, 1.1, 0.1), postMat);
                post.position.set(x, 3.7, z);
                scene.add(post);
            }
            // Add rails around the left half of the roof
            for(let i=0; i<=9; i+=3) { addRail(i, 0, 0.1, 0.1); addRail(i, 12, 0.1, 0.1); }
            addRail(0, 6, 0.1, 12); // Left side rail

            // Doghouse
            const dogBase = new THREE.Mesh(new THREE.BoxGeometry(1, 0.8, 1), new THREE.MeshStandardMaterial({color: 0x8b4513}));
            dogBase.position.set(14, 0.4, 14);
            scene.add(dogBase);

            // Porch
            const porch = new THREE.Mesh(new THREE.BoxGeometry(4, 0.2, 2), new THREE.MeshStandardMaterial({color: 0x999999}));
            porch.position.set(5, 0.1, -1);
            scene.add(porch);

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

# ---------- DISPLAY ----------
if view == "2D Blueprint":
    st.pyplot(draw_house_plan())
else:
    st.markdown("### 🏡 3D Interactive Model – Roof Balcony Active")
    components.html(generate_3d_house(), height=700, scrolling=False)
