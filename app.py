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

    # Add yard and parking boundaries (simple)
    ax.plot([-3, -3], [-2, 14], 'g--', linewidth=1, alpha=0.6)  # left property line
    ax.plot([21, 21], [-2, 14], 'g--', linewidth=1, alpha=0.6)  # right
    ax.plot([-3, 21], [14, 14], 'g--', linewidth=1, alpha=0.6)  # back
    ax.plot([-3, 21], [-2, -2], 'g--', linewidth=1, alpha=0.6)  # front

    ax.text(-2, 6, "FRONT YARD", rotation=90, fontsize=8, color='green', alpha=0.7)
    ax.text(10, 13, "BACKYARD", fontsize=8, color='green', alpha=0.7, ha='center')
    ax.text(19.5, 4, "PARKING", rotation=90, fontsize=8, color='blue', alpha=0.7)

    return fig

# ---------- 3D VIEW (Three.js) with all requested features ----------
def generate_3d_house():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; overflow: hidden; }
            #info {
                position: absolute;
                top: 20px;
                left: 20px;
                color: white;
                background: rgba(0,0,0,0.6);
                padding: 10px;
                border-radius: 8px;
                font-family: Arial, sans-serif;
                pointer-events: none;
                z-index: 100;
            }
        </style>
    </head>
    <body>
        <div id="info">
            <strong>3D House Model</strong><br>
            Drag to rotate | Right-click to pan | Scroll to zoom<br>
            ✅ Porch | ✅ Front/Back yards | ✅ Fence | ✅ Parking | ✅ Doghouse | ✅ Doors
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

            // --- Setup Scene, Camera, Renderers ---
            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x111122);
            scene.fog = new THREE.FogExp2(0x111122, 0.008);

            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(22, 14, 18);
            camera.lookAt(9, 0, 6);

            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.shadowMap.enabled = true;
            document.body.appendChild(renderer.domElement);

            const labelRenderer = new CSS2DRenderer();
            labelRenderer.setSize(window.innerWidth, window.innerHeight);
            labelRenderer.domElement.style.position = 'absolute';
            labelRenderer.domElement.style.top = '0px';
            labelRenderer.domElement.style.left = '0px';
            labelRenderer.domElement.style.pointerEvents = 'none';
            document.body.appendChild(labelRenderer.domElement);

            // --- Controls ---
            const controls = new OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.rotateSpeed = 0.5;
            controls.zoomSpeed = 1.2;
            controls.panSpeed = 0.8;
            controls.target.set(9, 2, 6);

            // --- Lighting ---
            const ambientLight = new THREE.AmbientLight(0x404060);
            scene.add(ambientLight);
            const dirLight = new THREE.DirectionalLight(0xffffff, 1);
            dirLight.position.set(10, 20, 5);
            dirLight.castShadow = true;
            dirLight.shadow.mapSize.width = 1024;
            dirLight.shadow.mapSize.height = 1024;
            scene.add(dirLight);
            const fillLight = new THREE.PointLight(0xccaa88, 0.3);
            fillLight.position.set(9, -1, 6);
            scene.add(fillLight);
            const rimLight = new THREE.PointLight(0xffaa66, 0.4);
            rimLight.position.set(0, 5, 15);
            scene.add(rimLight);

            // --- Ground / Yards ---
            // Grass (front yard): from z=-5 to 0, x=-3 to 21
            const grassMaterial = new THREE.MeshStandardMaterial({ color: 0x5a9e4e, roughness: 0.8 });
            const frontYard = new THREE.Mesh(new THREE.PlaneGeometry(24, 6), grassMaterial);
            frontYard.rotation.x = -Math.PI/2;
            frontYard.position.set(9, -0.1, -3);
            frontYard.receiveShadow = true;
            scene.add(frontYard);
            
            // Backyard: from z=12 to 17, x=-3 to 21
            const backYard = new THREE.Mesh(new THREE.PlaneGeometry(24, 6), grassMaterial);
            backYard.rotation.x = -Math.PI/2;
            backYard.position.set(9, -0.1, 15);
            backYard.receiveShadow = true;
            scene.add(backYard);

            // Parking lot (asphalt) on right side: x=18 to 23, z=0 to 8
            const asphalt = new THREE.MeshStandardMaterial({ color: 0x444444, roughness: 0.7 });
            const parking = new THREE.Mesh(new THREE.PlaneGeometry(5, 8), asphalt);
            parking.rotation.x = -Math.PI/2;
            parking.position.set(20.5, -0.08, 4);
            parking.receiveShadow = true;
            scene.add(parking);
            // Parking lines (simple white strips)
            const lineMat = new THREE.MeshStandardMaterial({ color: 0xffffff });
            for (let i = 0; i < 3; i++) {
                const line = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.05, 1.5), lineMat);
                line.position.set(20.5, -0.02, 2 + i*2.5);
                line.castShadow = false;
                scene.add(line);
            }

            // --- Fence (simple posts and horizontal rails) around property boundary ---
            const fenceMaterial = new THREE.MeshStandardMaterial({ color: 0xbc9a6c });
            const postMat = new THREE.MeshStandardMaterial({ color: 0x8b5a2b });
            // Property corners: (-3, -2) to (21, 14) but we'll go around
            const fencePoints = [
                [-3, -2], [21, -2], [21, 14], [-3, 14], [-3, -2]
            ];
            for (let i = 0; i < fencePoints.length - 1; i++) {
                const p1 = fencePoints[i];
                const p2 = fencePoints[i+1];
                const dx = p2[0] - p1[0];
                const dz = p2[1] - p1[1];
                const length = Math.hypot(dx, dz);
                const angle = Math.atan2(dz, dx);
                // horizontal rail
                const rail = new THREE.Mesh(new THREE.BoxGeometry(length, 0.1, 0.2), fenceMaterial);
                rail.position.set(p1[0] + dx/2, 0.8, p1[1] + dz/2);
                rail.rotation.y = angle;
                rail.castShadow = true;
                scene.add(rail);
                // posts every 2 meters
                const numPosts = Math.floor(length / 2);
                for (let j = 0; j <= numPosts; j++) {
                    const t = j / numPosts;
                    const px = p1[0] + dx * t;
                    const pz = p1[1] + dz * t;
                    const post = new THREE.Mesh(new THREE.BoxGeometry(0.2, 1.2, 0.2), postMat);
                    post.position.set(px, 0.6, pz);
                    post.castShadow = true;
                    scene.add(post);
                }
            }

            // --- House walls (reused from previous) ---
            const wallMaterial = new THREE.MeshStandardMaterial({ color: 0xcdc9c9, roughness: 0.4 });
            const thickness = 0.3;
            const wallHeight = 3.0;

            function addWall(x, z, width, depth, rotationY = 0) {
                const box = new THREE.BoxGeometry(width, wallHeight, depth);
                const mesh = new THREE.Mesh(box, wallMaterial);
                mesh.position.set(x, wallHeight/2, z);
                mesh.rotation.y = rotationY;
                mesh.castShadow = true;
                mesh.receiveShadow = true;
                scene.add(mesh);
            }
            // Outer walls
            addWall(9, 0, 18, thickness);
            addWall(18, 6, thickness, 12);
            addWall(9, 12, 18, thickness);
            addWall(0, 6, thickness, 12);
            // Inner walls
            addWall(10, 3.5, thickness, 7);
            addWall(14, 7, 8, thickness);
            addWall(16, 4, 4, thickness);
            addWall(14, 5.5, thickness, 3);

            // --- Doors (3D representation) ---
            const doorMaterial = new THREE.MeshStandardMaterial({ color: 0x8B5A2B });
            const knobMat = new THREE.MeshStandardMaterial({ color: 0xFFD700 });
            // Door at front entrance (x~5, z=0) - we'll add at (5,0) facing out
            const doorFront = new THREE.Mesh(new THREE.BoxGeometry(1.0, 2.0, 0.1), doorMaterial);
            doorFront.position.set(5, 1.0, 0.05);
            doorFront.castShadow = true;
            scene.add(doorFront);
            const knobFront = new THREE.Mesh(new THREE.SphereGeometry(0.08), knobMat);
            knobFront.position.set(5, 1.0, 0.12);
            scene.add(knobFront);
            
            // Door between living and kitchen (x=10, z=3) (interior)
            const doorInt = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.0, 1.0), doorMaterial);
            doorInt.position.set(10.05, 1.0, 3);
            doorInt.castShadow = true;
            scene.add(doorInt);
            const knobInt = new THREE.Mesh(new THREE.SphereGeometry(0.08), knobMat);
            knobInt.position.set(10.12, 1.0, 3);
            scene.add(knobInt);
            
            // Bathroom door (x=14, z=4)
            const doorBath = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.0, 0.8), doorMaterial);
            doorBath.position.set(14.05, 1.0, 4);
            doorBath.castShadow = true;
            scene.add(doorBath);
            const knobBath = new THREE.Mesh(new THREE.SphereGeometry(0.08), knobMat);
            knobBath.position.set(14.12, 1.0, 4);
            scene.add(knobBath);

            // --- Porch (platform with roof at front) ---
            const porchMaterial = new THREE.MeshStandardMaterial({ color: 0xc2b280 });
            const porchBase = new THREE.Mesh(new THREE.BoxGeometry(4, 0.2, 2.5), porchMaterial);
            porchBase.position.set(5, 0, -1.2);
            porchBase.castShadow = true;
            scene.add(porchBase);
            const porchRoof = new THREE.Mesh(new THREE.BoxGeometry(4.2, 0.1, 2.7), new THREE.MeshStandardMaterial({ color: 0xaa7c4a }));
            porchRoof.position.set(5, 2.4, -1.2);
            porchRoof.castShadow = true;
            scene.add(porchRoof);
            // porch posts
            const postPositions = [[3, -1.2], [7, -1.2]];
            postPositions.forEach(pos => {
                const post = new THREE.Mesh(new THREE.BoxGeometry(0.2, 2.2, 0.2), new THREE.MeshStandardMaterial({ color: 0x8B5A2B }));
                post.position.set(pos[0], 1.1, pos[1]);
                post.castShadow = true;
                scene.add(post);
            });

            // --- Doghouse (in backyard near x=14, z=14) ---
            const dogMat = new THREE.MeshStandardMaterial({ color: 0xaa8c5e });
            const dogBase = new THREE.Mesh(new THREE.BoxGeometry(1.0, 0.5, 1.2), dogMat);
            dogBase.position.set(14, 0.25, 14);
            dogBase.castShadow = true;
            scene.add(dogBase);
            const dogRoof = new THREE.Mesh(new THREE.CylinderGeometry(0.9, 0.9, 0.5, 4), dogMat);
            dogRoof.rotation.y = Math.PI/4;
            dogRoof.position.set(14, 0.7, 14);
            dogRoof.castShadow = true;
            scene.add(dogRoof);
            const dogDoor = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.4, 0.05), new THREE.MeshStandardMaterial({ color: 0xffaa66 }));
            dogDoor.position.set(14.3, 0.3, 14);
            scene.add(dogDoor);

            // --- Floor (semi-transparent) ---
            const floorMat = new THREE.MeshStandardMaterial({ color: 0xbc9a6c, roughness: 0.6, metalness: 0.05, transparent: true, opacity: 0.5 });
            const floor = new THREE.Mesh(new THREE.BoxGeometry(18, 0.1, 12), floorMat);
            floor.position.set(9, -0.05, 6);
            floor.receiveShadow = true;
            scene.add(floor);

            // --- Simple roof ---
            const roofMat = new THREE.MeshStandardMaterial({ color: 0xaa7777 });
            const roof = new THREE.Mesh(new THREE.CylinderGeometry(9.5, 9.5, 1.2, 4), roofMat);
            roof.rotation.y = Math.PI/4;
            roof.position.set(9, wallHeight - 0.1, 6);
            roof.castShadow = true;
            scene.add(roof);

            // --- Labels (CSS2D) ---
            function makeLabel(text, x, z, yOffset = 1.2) {
                const div = document.createElement('div');
                div.textContent = text;
                div.style.color = '#ffdd99';
                div.style.fontSize = '16px';
                div.style.fontWeight = 'bold';
                div.style.background = 'rgba(0,0,0,0.5)';
                div.style.padding = '2px 8px';
                div.style.borderRadius = '16px';
                div.style.border = '1px solid #ffaa66';
                const label = new CSS2DObject(div);
                label.position.set(x, yOffset, z);
                scene.add(label);
            }
            makeLabel('LIVING ROOM', 5, 6, 0.2);
            makeLabel('KITCHEN', 14, 3, 0.2);
            makeLabel('BEDROOM 1', 14, 9.5, 0.2);
            makeLabel('BEDROOM 2', 6, 9.5, 0.2);
            makeLabel('BATH', 16, 5.5, 0.2);
            makeLabel('ENTRY', 2, 1, 0.2);
            makeLabel('FRONT YARD', 9, -3, 0.5);
            makeLabel('BACKYARD', 9, 16, 0.5);
            makeLabel('PARKING', 22, 4, 0.5);
            makeLabel('DOGHOUSE', 14, 14.8, 0.5);

            // --- Animate ---
            function animate() {
                requestAnimationFrame(animate);
                controls.update();
                renderer.render(scene, camera);
                labelRenderer.render(scene, camera);
            }
            animate();

            window.addEventListener('resize', onWindowResize);
            function onWindowResize() {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
                labelRenderer.setSize(window.innerWidth, window.innerHeight);
            }
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
        - **Blue thick segments**: Windows  
        - **Red arrows**: Dimensions (meters)  
        - **Green dashed lines**: Property boundaries (yard, parking)  
        - This is an architectural floor plan (top‑down view).
        """)
else:
    st.markdown("### 🏡 3D Interactive Model – Full Property View")
    st.markdown("_Drag to rotate, right‑click to pan, scroll to zoom._")
    components.html(generate_3d_house(), height=700, scrolling=False)
