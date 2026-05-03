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

# ---------- 2D DRAWING FUNCTION (unchanged) ----------
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

    ax.text(-2, 6, "FRONT YARD", rotation=90, fontsize=8, color='green', alpha=0.7)
    ax.text(10, 13, "BACKYARD", fontsize=8, color='green', alpha=0.7, ha='center')
    ax.text(19.5, 4, "PARKING", rotation=90, fontsize=8, color='blue', alpha=0.7)

    return fig

# ---------- 3D VIEW (Three.js) UPDATED WITH BALCONY ----------
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
            <strong>3D House Model</strong><br>
            Drag to rotate | Right-click to pan | Scroll to zoom<br>
            ✅ Balcony | ✅ Porch | ✅ Yards | ✅ Fence | ✅ Parking | ✅ Doghouse
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
            camera.position.set(25, 20, 25);

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
            const ambientLight = new THREE.AmbientLight(0x404060);
            scene.add(ambientLight);
            const dirLight = new THREE.DirectionalLight(0xffffff, 1);
            dirLight.position.set(10, 25, 5);
            dirLight.castShadow = true;
            scene.add(dirLight);

            // Ground & Yards
            const grassMaterial = new THREE.MeshStandardMaterial({ color: 0x5a9e4e, roughness: 0.8 });
            const frontYard = new THREE.Mesh(new THREE.PlaneGeometry(24, 6), grassMaterial);
            frontYard.rotation.x = -Math.PI/2;
            frontYard.position.set(9, -0.1, -3);
            frontYard.receiveShadow = true;
            scene.add(frontYard);
            
            const backYard = new THREE.Mesh(new THREE.PlaneGeometry(24, 6), grassMaterial);
            backYard.rotation.x = -Math.PI/2;
            backYard.position.set(9, -0.1, 15);
            backYard.receiveShadow = true;
            scene.add(backYard);

            // Parking
            const asphalt = new THREE.MeshStandardMaterial({ color: 0x444444 });
            const parking = new THREE.Mesh(new THREE.PlaneGeometry(5, 8), asphalt);
            parking.rotation.x = -Math.PI/2;
            parking.position.set(20.5, -0.08, 4);
            parking.receiveShadow = true;
            scene.add(parking);
            const lineMat = new THREE.MeshStandardMaterial({ color: 0xffffff });
            for (let i = 0; i < 3; i++) {
                const line = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.05, 1.5), lineMat);
                line.position.set(20.5, -0.02, 2 + i*2.5);
                scene.add(line);
            }

            // Fence
            const postMat = new THREE.MeshStandardMaterial({ color: 0x8b5a2b });
            const fencePoints = [[-3, -2], [21, -2], [21, 14], [-3, 14], [-3, -2]];
            for (let i = 0; i < fencePoints.length - 1; i++) {
                const p1 = fencePoints[i]; const p2 = fencePoints[i+1];
                const dx = p2[0]-p1[0]; const dz = p2[1]-p1[1];
                const length = Math.hypot(dx, dz); const angle = Math.atan2(dz, dx);
                const rail = new THREE.Mesh(new THREE.BoxGeometry(length, 0.1, 0.2), new THREE.MeshStandardMaterial({color: 0xbc9a6c}));
                rail.position.set(p1[0]+dx/2, 0.8, p1[1]+dz/2); rail.rotation.y = angle;
                scene.add(rail);
                const numPosts = Math.floor(length/2);
                for(let j=0; j<=numPosts; j++) {
                    const post = new THREE.Mesh(new THREE.BoxGeometry(0.2, 1.2, 0.2), postMat);
                    post.position.set(p1[0]+dx*(j/numPosts), 0.6, p1[1]+dz*(j/numPosts));
                    scene.add(post);
                }
            }

            // Walls
            const wallMaterial = new THREE.MeshStandardMaterial({ color: 0xcdc9c9 });
            const wallHeight = 3.0;
            function addWall(x, z, w, d, ry=0) {
                const m = new THREE.Mesh(new THREE.BoxGeometry(w, wallHeight, d), wallMaterial);
                m.position.set(x, wallHeight/2, z); m.rotation.y = ry;
                m.castShadow = true; m.receiveShadow = true; scene.add(m);
            }
            addWall(9, 0, 18, 0.3); addWall(18, 6, 0.3, 12); addWall(9, 12, 18, 0.3); addWall(0, 6, 0.3, 12);
            addWall(10, 3.5, 0.3, 7); addWall(14, 7, 8, 0.3); addWall(16, 4, 4, 0.3); addWall(14, 5.5, 0.3, 3);

            // Doors
            const doorMat = new THREE.MeshStandardMaterial({ color: 0x8B5A2B });
            const door = new THREE.Mesh(new THREE.BoxGeometry(1.0, 2.0, 0.1), doorMat);
            door.position.set(5, 1.0, 0.05); scene.add(door);

            // --- THE BALCONY ADDITION ---
            // Roof Slab (Floor of the balcony)
            const roofFloor = new THREE.Mesh(new THREE.BoxGeometry(18.2, 0.2, 12.2), new THREE.MeshStandardMaterial({ color: 0x888888 }));
            roofFloor.position.set(9, 3.1, 6);
            roofFloor.receiveShadow = true;
            scene.add(roofFloor);

            // Glass Railings
            const glassMat = new THREE.MeshStandardMaterial({ color: 0x88ccff, transparent: true, opacity: 0.4 });
            const handrailMat = new THREE.MeshStandardMaterial({ color: 0x333333 });
            function addBalconyRail(x, z, w, d) {
                const glass = new THREE.Mesh(new THREE.BoxGeometry(w, 1.0, d), glassMat);
                glass.position.set(x, 3.7, z); scene.add(glass);
                const bar = new THREE.Mesh(new THREE.BoxGeometry(w, 0.05, d+0.05), handrailMat);
                bar.position.set(x, 4.2, z); scene.add(bar);
            }
            addBalconyRail(9, 0, 18.2, 0.1); // front
            addBalconyRail(18.1, 6, 0.1, 12.2); // right
            addBalconyRail(9, 12, 18.2, 0.1); // back
            addBalconyRail(-0.1, 6, 0.1, 12.2); // left

            // Stairwell Access Housing
            const hatch = new THREE.Mesh(new THREE.BoxGeometry(2, 2, 2), wallMaterial);
            hatch.position.set(2, 4, 2); scene.add(hatch);

            // Porch
            const porchBase = new THREE.Mesh(new THREE.BoxGeometry(4, 0.2, 2.5), new THREE.MeshStandardMaterial({ color: 0xc2b280 }));
            porchBase.position.set(5, 0, -1.2); scene.add(porchBase);

            // Doghouse
            const dogBase = new THREE.Mesh(new THREE.BoxGeometry(1.0, 0.5, 1.2), new THREE.MeshStandardMaterial({ color: 0xaa8c5e }));
            dogBase.position.set(14, 0.25, 14); scene.add(dogBase);

            // Labels
            function makeLabel(t, x, z, y=0.2) {
                const d = document.createElement('div'); d.textContent = t;
                d.style.color = '#ffdd99'; d.style.background = 'rgba(0,0,0,0.5)';
                d.style.padding = '2px 8px'; d.style.borderRadius = '16px';
                const l = new CSS2DObject(d); l.position.set(x, y, z); scene.add(l);
            }
            makeLabel('LIVING ROOM', 5, 6); makeLabel('KITCHEN', 14, 3);
            makeLabel('BACKYARD', 9, 16, 0.5); makeLabel('DOGHOUSE', 14, 14.8, 0.5);
            makeLabel('BALCONY', 9, 6, 4);

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

# ---------- DISPLAY SELECTED VIEW ----------
if view == "2D Blueprint":
    fig = draw_house_plan()
    st.pyplot(fig)
    with st.expander("📐 Legend & Instructions"):
        st.markdown("""
        - **Black thick lines**: Walls  
        - **Blue arcs & lines**: Doors  
        - **Red arrows**: Dimensions (meters)  
        - **Green dashed lines**: Property boundaries  
        """)
else:
    st.markdown("### 🏡 3D Interactive Model – Full Property View with Balcony")
    components.html(generate_3d_house(), height=700, scrolling=False)
