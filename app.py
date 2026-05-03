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
    ax.set_xlim(-1, 20)
    ax.set_ylim(-1, 15)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_xlabel("Meters (or feet)", fontsize=10)
    ax.set_ylabel("Meters (or feet)", fontsize=10)
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

    return fig

# ---------- 3D VIEW (Three.js) ----------
def generate_3d_house():
    # Generate JavaScript code for Three.js
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ margin: 0; overflow: hidden; }}
            #info {{
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
            }}
        </style>
    </head>
    <body>
        <div id="info">
            <strong>3D House Model</strong><br>
            Drag to rotate | Right-click to pan | Scroll to zoom
        </div>
        <script type="importmap">
            {{
                "imports": {{
                    "three": "https://unpkg.com/three@0.128.0/build/three.module.js",
                    "three/addons/": "https://unpkg.com/three@0.128.0/examples/jsm/"
                }}
            }}
        </script>
        <script type="module">
            import * as THREE from 'three';
            import {{ OrbitControls }} from 'three/addons/controls/OrbitControls.js';
            import {{ CSS2DRenderer, CSS2DObject }} from 'three/addons/renderers/CSS2DRenderer.js';

            // --- Setup Scene, Camera, Renderers ---
            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x111122);
            scene.fog = new THREE.FogExp2(0x111122, 0.008);

            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(20, 15, 20);
            camera.lookAt(9, 0, 6);

            const renderer = new THREE.WebGLRenderer({{ antialias: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.shadowMap.enabled = true;
            document.body.appendChild(renderer.domElement);

            // CSS2 renderer for text labels
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
            // Ambient light
            const ambientLight = new THREE.AmbientLight(0x404060);
            scene.add(ambientLight);
            // Directional light (sun)
            const dirLight = new THREE.DirectionalLight(0xffffff, 1);
            dirLight.position.set(10, 20, 5);
            dirLight.castShadow = true;
            dirLight.receiveShadow = false;
            dirLight.shadow.mapSize.width = 1024;
            dirLight.shadow.mapSize.height = 1024;
            scene.add(dirLight);
            // Fill light from below
            const fillLight = new THREE.PointLight(0xccaa88, 0.3);
            fillLight.position.set(9, -1, 6);
            scene.add(fillLight);
            // Back rim light
            const rimLight = new THREE.PointLight(0xffaa66, 0.4);
            rimLight.position.set(0, 5, 15);
            scene.add(rimLight);

            // --- Helper: Grid and ground ---
            const gridHelper = new THREE.GridHelper(30, 20, 0x88aaff, 0x335588);
            gridHelper.position.y = -0.05;
            scene.add(gridHelper);
            
            // Ground plane (transparent but receives shadows)
            const groundPlane = new THREE.Mesh(
                new THREE.PlaneGeometry(30, 30),
                new THREE.ShadowMaterial({{ opacity: 0.3, color: 0x000000, transparent: true }})
            );
            groundPlane.rotation.x = -Math.PI / 2;
            groundPlane.position.y = -0.05;
            groundPlane.receiveShadow = true;
            scene.add(groundPlane);

            // --- Create walls as extruded boxes ---
            const wallMaterial = new THREE.MeshStandardMaterial({{ color: 0xcdc9c9, roughness: 0.4, metalness: 0.1 }});
            const thickness = 0.3;
            const wallHeight = 3.0;

            function addWall(x, z, width, depth, rotationY = 0) {{
                const box = new THREE.BoxGeometry(width, wallHeight, depth);
                const mesh = new THREE.Mesh(box, wallMaterial);
                mesh.position.set(x, wallHeight/2, z);
                mesh.rotation.y = rotationY;
                mesh.castShadow = true;
                mesh.receiveShadow = true;
                scene.add(mesh);
            }}

            // Outer walls (perimeter)
            addWall(9, 0, 18, thickness);      // bottom (z=0)
            addWall(18, 6, thickness, 12);     // right (x=18)
            addWall(9, 12, 18, thickness);     // top (z=12)
            addWall(0, 6, thickness, 12);      // left (x=0)

            // Inner walls
            // Vertical wall at x=10 from z=0 to z=7
            addWall(10, 3.5, thickness, 7);
            // Horizontal wall from x=10 to x=18 at z=7
            addWall(14, 7, 8, thickness);
            // Bathroom walls (bottom-right)
            addWall(16, 4, 4, thickness);      // horizontal bottom of bathroom (z=4)
            addWall(14, 5.5, thickness, 3);    // vertical left of bathroom (x=14, from z=4 to z=7)

            // --- Floor (semi-transparent slab) ---
            const floorMaterial = new THREE.MeshStandardMaterial({{ color: 0xbc9a6c, roughness: 0.6, metalness: 0.05, transparent: true, opacity: 0.7 }});
            const floor = new THREE.Mesh(new THREE.BoxGeometry(18, 0.1, 12), floorMaterial);
            floor.position.set(9, -0.05, 6);
            floor.receiveShadow = true;
            floor.castShadow = false;
            scene.add(floor);

            // --- Simple roof (pyramid-like) ---
            const roofMaterial = new THREE.MeshStandardMaterial({{ color: 0xaa7777, roughness: 0.8 }});
            const roofHeight = 1.2;
            const roofOverhang = 0.5;
            const roofWidth = 18 + roofOverhang*2;
            const roofDepth = 12 + roofOverhang*2;
            const roof = new THREE.Mesh(new THREE.CylinderGeometry(roofWidth/2, roofDepth/2, roofHeight, 4), roofMaterial);
            roof.rotation.y = Math.PI/4;
            roof.position.set(9, wallHeight - 0.1, 6);
            roof.castShadow = true;
            scene.add(roof);

            // --- Add room labels using CSS2DRenderer ---
            function makeLabel(text, x, z, yOffset = 1.2) {{
                const div = document.createElement('div');
                div.textContent = text;
                div.style.color = '#ffdd99';
                div.style.fontSize = '18px';
                div.style.fontWeight = 'bold';
                div.style.textShadow = '1px 1px 0px black';
                div.style.background = 'rgba(0,0,0,0.5)';
                div.style.padding = '4px 10px';
                div.style.borderRadius = '20px';
                div.style.border = '1px solid #ffaa66';
                div.style.fontFamily = 'Arial, sans-serif';
                const label = new CSS2DObject(div);
                label.position.set(x, yOffset, z);
                scene.add(label);
            }}
            makeLabel('LIVING ROOM', 5, 6, 0.2);
            makeLabel('KITCHEN', 14, 3, 0.2);
            makeLabel('BEDROOM 1', 14, 9.5, 0.2);
            makeLabel('BEDROOM 2', 6, 9.5, 0.2);
            makeLabel('BATHROOM', 16, 5.5, 0.2);
            makeLabel('ENTRY', 2, 1, 0.2);

            // --- Simple furniture indicators (optional) ---
            const furnMaterial = new THREE.MeshStandardMaterial({{ color: 0x88aaff }});
            // Kitchen counter
            const counter = new THREE.Mesh(new THREE.BoxGeometry(2, 0.8, 1), furnMaterial);
            counter.position.set(15, 0.4, 2.5);
            counter.castShadow = true;
            scene.add(counter);
            // Bed in bedroom 1
            const bed = new THREE.Mesh(new THREE.BoxGeometry(1.8, 0.4, 2.2), furnMaterial);
            bed.position.set(15, 0.2, 10);
            bed.castShadow = true;
            scene.add(bed);
            
            // --- Animate ---
            function animate() {{
                requestAnimationFrame(animate);
                controls.update(); // update for damping
                renderer.render(scene, camera);
                labelRenderer.render(scene, camera);
            }}
            animate();

            // Handle window resize
            window.addEventListener('resize', onWindowResize, false);
            function onWindowResize() {{
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
                labelRenderer.setSize(window.innerWidth, window.innerHeight);
            }}
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
        - **Blue arcs & lines**: Doors (arc shows swing direction)  
        - **Blue thick segments**: Windows  
        - **Red arrows**: Dimensions (meters)  
        - **Dashed grid**: 1‑meter reference  
        - This is an architectural floor plan (top‑down view).
        """)
else:
    st.markdown("### 🏡 3D Interactive Model")
    st.markdown("_Drag to rotate, right‑click to pan, scroll to zoom._")
    # Embed the Three.js HTML
    components.html(generate_3d_house(), height=700, scrolling=False)
