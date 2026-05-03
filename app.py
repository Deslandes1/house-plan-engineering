import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties

st.set_page_config(
    page_title="House Plan | 2D Blueprint & 3D Model",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Architectural House Plan")
st.markdown("Switch between **2D engineering drawing** and **3D interactive model**.")

view = st.sidebar.radio("Select view:", ["2D Blueprint", "3D Model"])

# ---------- 2D BLUEPRINT (same as before) ----------
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

    # Doors
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

    # Labels
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

    # Yard/parking boundaries
    ax.plot([-3, -3], [-2, 14], 'g--', linewidth=1, alpha=0.6)
    ax.plot([21, 21], [-2, 14], 'g--', linewidth=1, alpha=0.6)
    ax.plot([-3, 21], [14, 14], 'g--', linewidth=1, alpha=0.6)
    ax.plot([-3, 21], [-2, -2], 'g--', linewidth=1, alpha=0.6)
    ax.text(-2, 6, "FRONT YARD", rotation=90, fontsize=8, color='green', alpha=0.7)
    ax.text(10, 13, "BACKYARD", fontsize=8, color='green', alpha=0.7, ha='center')
    ax.text(19.5, 4, "PARKING", rotation=90, fontsize=8, color='blue', alpha=0.7)

    return fig

# ---------- SIMPLIFIED 3D MODEL (GUARANTEED TO WORK) ----------
def get_3d_html():
    return """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; overflow: hidden; }
        #info {
            position: absolute; top: 20px; left: 20px; color: white;
            background: rgba(0,0,0,0.6); padding: 8px 15px; border-radius: 8px;
            font-family: Arial; pointer-events: none; z-index: 100;
        }
    </style>
</head>
<body>
    <div id="info">🏠 3D House – Simple but complete | Drag to rotate | Scroll to zoom</div>
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

        // --- Setup ---
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x111122);
        scene.fog = new THREE.FogExp2(0x111122, 0.01);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(15, 10, 15);
        camera.lookAt(0, 0, 0);

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.shadowMap.enabled = true;
        document.body.appendChild(renderer.domElement);

        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.rotateSpeed = 0.5;
        controls.zoomSpeed = 1.2;
        controls.panSpeed = 0.8;
        controls.target.set(0, 2, 0);

        // --- Lighting ---
        const ambientLight = new THREE.AmbientLight(0x404060);
        scene.add(ambientLight);
        const dirLight = new THREE.DirectionalLight(0xffffff, 1);
        dirLight.position.set(5, 10, 7);
        dirLight.castShadow = true;
        scene.add(dirLight);
        const backLight = new THREE.PointLight(0xccaa88, 0.3);
        backLight.position.set(-2, 3, -4);
        scene.add(backLight);

        // --- Ground (grass) ---
        const groundMat = new THREE.MeshStandardMaterial({ color: 0x5a9e4e, roughness: 0.8 });
        const ground = new THREE.Mesh(new THREE.PlaneGeometry(20, 20), groundMat);
        ground.rotation.x = -Math.PI / 2;
        ground.position.y = -0.1;
        ground.receiveShadow = true;
        scene.add(ground);

        // --- Simple House (base cube) ---
        const houseMat = new THREE.MeshStandardMaterial({ color: 0xcdc9c9, roughness: 0.4 });
        const houseBase = new THREE.Mesh(new THREE.BoxGeometry(4, 3, 4), houseMat);
        houseBase.position.set(0, 1.5, 0);
        houseBase.castShadow = true;
        houseBase.receiveShadow = true;
        scene.add(houseBase);

        // --- Roof (triangular prism using a rotated cylinder with 3 segments) ---
        // A cylinder with 3 segments gives a triangular prism. Rotate it to point upwards.
        const roofMat = new THREE.MeshStandardMaterial({ color: 0xaa7777 });
        const roof = new THREE.Mesh(new THREE.CylinderGeometry(2.5, 2.5, 1.5, 3), roofMat);
        roof.position.set(0, 3.2, 0);
        roof.castShadow = true;
        scene.add(roof);

        // --- Door (simple brown rectangle at front) ---
        const doorMat = new THREE.MeshStandardMaterial({ color: 0x8B5A2B });
        const door = new THREE.Mesh(new THREE.BoxGeometry(0.8, 1.5, 0.2), doorMat);
        door.position.set(0, 0.8, 2.05);
        door.castShadow = true;
        scene.add(door);
        // Doorknob
        const knobMat = new THREE.MeshStandardMaterial({ color: 0xFFD700 });
        const knob = new THREE.Mesh(new THREE.SphereGeometry(0.08), knobMat);
        knob.position.set(0.3, 0.9, 2.15);
        scene.add(knob);

        // --- Window (blue rectangle on right wall) ---
        const windowMat = new THREE.MeshStandardMaterial({ color: 0x88aaff });
        const windowGeo = new THREE.Mesh(new THREE.BoxGeometry(1.0, 1.0, 0.1), windowMat);
        windowGeo.position.set(2.05, 1.8, 0);
        windowGeo.castShadow = true;
        scene.add(windowGeo);

        // --- Simple fence (four posts with rails around the house) ---
        const fenceMat = new THREE.MeshStandardMaterial({ color: 0xbc9a6c });
        const postMat = new THREE.MeshStandardMaterial({ color: 0x8b5a2b });
        const fenceSize = 5;
        const fenceY = 0.5;
        // Posts at corners
        const corners = [[-2.5, -2.5], [2.5, -2.5], [2.5, 2.5], [-2.5, 2.5]];
        corners.forEach(corner => {
            const post = new THREE.Mesh(new THREE.BoxGeometry(0.2, 1.0, 0.2), postMat);
            post.position.set(corner[0], fenceY, corner[1]);
            post.castShadow = true;
            scene.add(post);
        });
        // Rails (horizontal)
        const railPos = [[-2.5, -2.5, 2.5, -2.5], [2.5, -2.5, 2.5, 2.5], [2.5, 2.5, -2.5, 2.5], [-2.5, 2.5, -2.5, -2.5]];
        railPos.forEach(rail => {
            const dx = rail[2] - rail[0];
            const dz = rail[3] - rail[1];
            const length = Math.hypot(dx, dz);
            const angle = Math.atan2(dz, dx);
            const railMesh = new THREE.Mesh(new THREE.BoxGeometry(length, 0.1, 0.2), fenceMat);
            railMesh.position.set(rail[0] + dx/2, fenceY + 0.3, rail[1] + dz/2);
            railMesh.rotation.y = angle;
            railMesh.castShadow = true;
            scene.add(railMesh);
        });

        // --- Parking (simple asphalt plane at side) ---
        const asphaltMat = new THREE.MeshStandardMaterial({ color: 0x333333, roughness: 0.8 });
        const parking = new THREE.Mesh(new THREE.BoxGeometry(2.5, 0.1, 3), asphaltMat);
        parking.position.set(-4, -0.05, -2.5);
        parking.receiveShadow = true;
        scene.add(parking);
        // White line
        const line = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.05, 2), new THREE.MeshStandardMaterial({ color: 0xffffff }));
        line.position.set(-4, 0, -2.5);
        line.castShadow = false;
        scene.add(line);

        // --- Doghouse (small house in the back) ---
        const dogMat = new THREE.MeshStandardMaterial({ color: 0xaa8c5e });
        const dogBase = new THREE.Mesh(new THREE.BoxGeometry(1.0, 0.5, 1.0), dogMat);
        dogBase.position.set(3, 0.25, 3.5);
        dogBase.castShadow = true;
        scene.add(dogBase);
        const dogRoof = new THREE.Mesh(new THREE.CylinderGeometry(0.7, 0.7, 0.4, 4), dogMat);
        dogRoof.rotation.y = Math.PI/4;
        dogRoof.position.set(3, 0.7, 3.5);
        dogRoof.castShadow = true;
        scene.add(dogRoof);
        const dogDoorMat = new THREE.MeshStandardMaterial({ color: 0xffaa66 });
        const dogDoor = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.4, 0.05), dogDoorMat);
        dogDoor.position.set(3.3, 0.3, 3.5);
        scene.add(dogDoor);

        // --- Simple labels using CSS2DRenderer ---
        import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';
        const labelRenderer = new CSS2DRenderer();
        labelRenderer.setSize(window.innerWidth, window.innerHeight);
        labelRenderer.domElement.style.position = 'absolute';
        labelRenderer.domElement.style.top = '0px';
        labelRenderer.domElement.style.left = '0px';
        labelRenderer.domElement.style.pointerEvents = 'none';
        document.body.appendChild(labelRenderer.domElement);

        function makeLabel(text, x, y, z) {
            const div = document.createElement('div');
            div.textContent = text;
            div.style.color = '#ffdd99';
            div.style.fontSize = '16px';
            div.style.fontWeight = 'bold';
            div.style.background = 'rgba(0,0,0,0.6)';
            div.style.padding = '4px 12px';
            div.style.borderRadius = '20px';
            div.style.border = '1px solid #ffaa66';
            div.style.fontFamily = 'Arial';
            const label = new CSS2DObject(div);
            label.position.set(x, y, z);
            scene.add(label);
        }
        makeLabel('FRONT DOOR', 0, 1.2, 2.3);
        makeLabel('DOGHOUSE', 3, 0.6, 3.8);
        makeLabel('PARKING', -4, 0.2, -2.5);

        // --- Animation loop ---
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

# ---------- DISPLAY ----------
if view == "2D Blueprint":
    fig = draw_house_plan()
    st.pyplot(fig)
    with st.expander("📐 Legend & Instructions"):
        st.markdown("""
        - **Black thick lines**: Walls  
        - **Blue arcs & lines**: Doors (arc = swing direction)  
        - **Blue thick segments**: Windows  
        - **Red arrows**: Dimensions (meters)  
        - **Green dashed lines**: Property boundaries  
        """)
else:
    st.markdown("### 🏡 3D Interactive Model – Simple but Complete House")
    st.markdown("_Drag to rotate, right‑click to pan, scroll to zoom._")
    components.html(get_3d_html(), height=700, scrolling=False)
