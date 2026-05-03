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

# ---------- 2D DRAWING FUNCTION (Professional Engineer Style) ----------
def draw_house_plan():
    # Use a crisp white background and standard engineering fonts
    fig, ax = plt.subplots(figsize=(14, 11), facecolor='white')
    ax.set_facecolor('white')
    
    # Set plot limits
    ax.set_xlim(-5, 25)
    ax.set_ylim(-5, 18)
    ax.set_aspect('equal')
    
    # Engineering Grid (Light and subtle)
    ax.grid(True, which='both', color='#E0E0E0', linestyle='-', linewidth=0.5)
    
    # 1. LAND & EXTERIOR (Dashed lines for boundaries)
    # Property Boundary
    ax.plot([-3, 21, 21, -3, -3], [-2, -2, 14, 14, -2], color='black', linestyle='-.', linewidth=1, label='Property Line')
    
    # Parking Area (Matching 3D)
    ax.add_patch(patches.Rectangle((18, 0), 5, 8, fill=False, hatch='///', color='#666666', alpha=0.4))
    ax.text(20.5, 4, "PARKING (ASPHALT)", rotation=90, fontsize=9, ha='center', fontweight='bold')

    # Porch (Matching 3D)
    ax.add_patch(patches.Rectangle((3, -2), 4, 2, facecolor='#F5F5DC', edgecolor='black', linewidth=1.5))
    ax.text(5, -1, "ENTRY PORCH", ha='center', fontsize=8, fontweight='bold')

    # Doghouse (Matching 3D)
    ax.add_patch(patches.Rectangle((13.5, 13.5), 1.0, 1.2, facecolor='none', edgecolor='black'))
    ax.plot([13.5, 14, 14.5], [14.7, 15.2, 14.7], color='black') # Small roof icon
    ax.text(14, 13, "DOGHOUSE", ha='center', fontsize=7)

    # 2. THE HOUSE STRUCTURE (Thick Black Walls)
    # Outer walls
    outer_walls = [((0,0), (18,0)), ((18,0), (18,12)), ((18,12), (0,12)), ((0,12), (0,0))]
    for (x1,y1), (x2,y2) in outer_walls:
        ax.plot([x1, x2], [y1, y2], color='black', linewidth=5, solid_capstyle='square')

    # Balcony/Roof Outline (Dashed red line to show overhang from 3D)
    ax.plot([-0.2, 18.2, 18.2, -0.2, -0.2], [-0.1, -0.1, 12.1, 12.1, -0.1], 
            color='red', linestyle='--', linewidth=1, alpha=0.5)
    ax.text(9, 12.3, "BALCONY RAILING PERIMETER (OVERHEAD)", color='red', fontsize=7, ha='center')

    # Inner walls
    ax.plot([10, 10], [0, 7], 'k-', linewidth=4)
    ax.plot([10, 18], [7, 7], 'k-', linewidth=4)
    ax.plot([14, 18], [4, 4], 'k-', linewidth=4)
    ax.plot([14, 14], [4, 7], 'k-', linewidth=4)

    # 3. ARCHITECTURAL SYMBOLS (Doors & Windows)
    # Doors
    doors = [
        (10, 3, 270, 360, 10, 10.6, 3, 3), 
        (14, 7, 0, 90, 14, 14, 7, 7.6),    
        (10, 8.5, 270, 360, 10, 10.6, 8.5, 8.5), 
        (16, 7, 0, 90, 16, 16, 7, 7.6),    
        (14, 4, 90, 180, 14, 14, 4, 3.4),  
        (5, 0, 0, 90, 5, 5, 0, 0.6) # Main Door
    ]
    for cx, cy, t1, t2, x1, x2, y1, y2 in doors:
        ax.add_patch(patches.Arc((cx, cy), 1.2, 1.2, theta1=t1, theta2=t2, linewidth=1.5, color='black'))
        ax.plot([x1, x2], [y1, y2], color='black', linewidth=1.5)

    # Windows (Standard architectural parallel lines)
    windows = [((0, 4), (0, 6)), ((11, 0), (13, 0)), ((12, 12), (14, 12)), ((18, 9), (18, 11))]
    for (wx1, wy1), (wx2, wy2) in windows:
        ax.plot([wx1, wx2], [wy1, wy2], color='white', linewidth=6) # Break wall
        ax.plot([wx1, wx2], [wy1, wy2], color='black', linewidth=1) # Window line 1
        # Offset for double line effect
        off = 0.1
        if wx1 == wx2: ax.plot([wx1+off, wx2+off], [wy1, wy2], color='black', linewidth=1)
        else: ax.plot([wx1, wx2], [wy1+off, wy2+off], color='black', linewidth=1)

    # 4. ANNOTATIONS
    font_rooms = FontProperties(weight='bold', size=10)
    ax.text(5, 6, "LIVING ROOM\n(FIN. FLOOR: 0.00)", ha='center', fontproperties=font_rooms)
    ax.text(14, 3, "KITCHEN", ha='center', fontproperties=font_rooms)
    ax.text(14, 9.5, "BEDROOM 1", ha='center', fontproperties=font_rooms)
    ax.text(6, 9.5, "BEDROOM 2", ha='center', fontproperties=font_rooms)
    ax.text(16, 5.5, "BATH", ha='center', fontproperties=font_rooms)

    # Dimensions
    ax.annotate('', xy=(0, -3.5), xytext=(18, -3.5), arrowprops=dict(arrowstyle='<->', color='black'))
    ax.text(9, -4, "18.00 m", ha='center', fontweight='bold')
    
    ax.annotate('', xy=(23.5, 0), xytext=(23.5, 12), arrowprops=dict(arrowstyle='<->', color='black'))
    ax.text(24, 6, "12.00 m", rotation=90, va='center', fontweight='bold')

    # 5. PROFESSIONAL TITLE BLOCK (Bottom Right)
    rect = patches.Rectangle((14, -4.5), 10, 3, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    ax.text(14.5, -2.2, "PROJECT: MODERN RESIDENCE", fontsize=8, fontweight='bold')
    ax.text(14.5, -2.8, "SHEET: GROUND FLOOR PLAN (2D)", fontsize=7)
    ax.text(14.5, -3.4, "SCALE: 1:100 | UNIT: METERS", fontsize=7)
    ax.text(14.5, -4, "DESIGNED BY: ENGINEER AI", fontsize=7)

    # Remove axes for a clean "sheet" look
    ax.axis('off')
    return fig

# ---------- 3D VIEW (Three.js) - KEPT THE SAME ----------
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
            ✅ Porch | ✅ Yards | ✅ Fence | ✅ Parking | ✅ Doghouse
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
            camera.position.set(22, 14, 18);

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
            dirLight.position.set(10, 20, 5);
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

            // Floor
            const floor = new THREE.Mesh(new THREE.BoxGeometry(18, 0.1, 12), new THREE.MeshStandardMaterial({ color: 0xbc9a6c, transparent: true, opacity: 0.5 }));
            floor.position.set(9, -0.05, 6); scene.add(floor);

            // Porch
            const porchBase = new THREE.Mesh(new THREE.BoxGeometry(4, 0.2, 2.5), new THREE.MeshStandardMaterial({ color: 0xc2b280 }));
            porchBase.position.set(5, 0, -1.2); scene.add(porchBase);

            // Doghouse
            const dogBase = new THREE.Mesh(new THREE.BoxGeometry(1.0, 0.5, 1.2), new THREE.MeshStandardMaterial({ color: 0xaa8c5e }));
            dogBase.position.set(14, 0.25, 14); scene.add(dogBase);

            // Labels
            function makeLabel(t, x, z) {
                const d = document.createElement('div'); d.textContent = t;
                d.style.color = '#ffdd99'; d.style.background = 'rgba(0,0,0,0.5)';
                d.style.padding = '2px 8px'; d.style.borderRadius = '16px';
                const l = new CSS2DObject(d); l.position.set(x, 0.2, z); scene.add(l);
            }
            makeLabel('LIVING ROOM', 5, 6); makeLabel('KITCHEN', 14, 3);
            makeLabel('BACKYARD', 9, 16);

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
    st.pyplot(draw_house_plan())
else:
    st.markdown("### 🏡 3D Interactive Model")
    components.html(generate_3d_house(), height=700, scrolling=False)
