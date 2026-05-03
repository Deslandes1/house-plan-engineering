import streamlit as st
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

# Sidebar toggle
view = st.sidebar.radio("Select view:", ["2D Blueprint", "3D Model"])

# ---------- 2D DRAWING (unchanged, works) ----------
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

# ---------- 3D VIEW (embedded as HTML with srcdoc via JavaScript) ----------
def get_3d_html():
    return """<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, Helvetica, sans-serif; }
        #info {
            position: absolute;
            top: 20px;
            left: 20px;
            color: white;
            background: rgba(0,0,0,0.6);
            padding: 8px 15px;
            border-radius: 8px;
            pointer-events: none;
            z-index: 100;
            font-size: 14px;
        }
        #controls-note {
            position: absolute;
            bottom: 20px;
            left: 20px;
            color: #ccc;
            background: rgba(0,0,0,0.5);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 12px;
            pointer-events: none;
            z-index: 100;
        }
    </style>
</head>
<body>
    <div id="info">
        <strong>🏡 3D House Model</strong><br>
        Triangular roof | Balcony | Exit door | Fence | Doghouse
    </div>
    <div id="controls-note">
        🖱️ Drag to rotate | Right-click to pan | Scroll to zoom
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

        // --- Setup ---
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x0a1030);
        scene.fog = new THREE.FogExp2(0x0a1030, 0.008);

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

        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.rotateSpeed = 0.5;
        controls.zoomSpeed = 1.2;
        controls.panSpeed = 0.8;
        controls.target.set(9, 3, 6);

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

        // --- Ground & Yards ---
        const grassMat = new THREE.MeshStandardMaterial({ color: 0x5a9e4e, roughness: 0.8 });
        const frontYard = new THREE.Mesh(new THREE.PlaneGeometry(24, 6), grassMat);
        frontYard.rotation.x = -Math.PI/2;
        frontYard.position.set(9, -0.1, -3);
        frontYard.receiveShadow = true;
        scene.add(frontYard);
        
        const backYard = new THREE.Mesh(new THREE.PlaneGeometry(24, 6), grassMat);
        backYard.rotation.x = -Math.PI/2;
        backYard.position.set(9, -0.1, 15);
        backYard.receiveShadow = true;
        scene.add(backYard);

        // --- Parking ---
        const asphaltMat = new THREE.MeshStandardMaterial({ color: 0x444444, roughness: 0.7 });
        const parking = new THREE.Mesh(new THREE.PlaneGeometry(5, 8), asphaltMat);
        parking.rotation.x = -Math.PI/2;
        parking.position.set(20.5, -0.08, 4);
        parking.receiveShadow = true;
        scene.add(parking);
        const lineMat = new THREE.MeshStandardMaterial({ color: 0xffffff });
        for (let i = 0; i < 3; i++) {
            const line = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.05, 1.5), lineMat);
            line.position.set(20.5, -0.02, 2 + i*2.5);
            line.castShadow = false;
            scene.add(line);
        }

        // --- Fence ---
        const fenceMat = new THREE.MeshStandardMaterial({ color: 0xbc9a6c });
        const postMat = new THREE.MeshStandardMaterial({ color: 0x8b5a2b });
        const fencePoints = [[-3, -2], [21, -2], [21, 14], [-3, 14], [-3, -2]];
        for (let i = 0; i < fencePoints.length - 1; i++) {
            const p1 = fencePoints[i];
            const p2 = fencePoints[i+1];
            const dx = p2[0] - p1[0];
            const dz = p2[1] - p1[1];
            const length = Math.hypot(dx, dz);
            const angle = Math.atan2(dz, dx);
            const rail = new THREE.Mesh(new THREE.BoxGeometry(length, 0.1, 0.2), fenceMat);
            rail.position.set(p1[0] + dx/2, 0.8, p1[1] + dz/2);
            rail.rotation.y = angle;
            rail.castShadow = true;
            scene.add(rail);
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

        // --- House Walls ---
        const wallMat = new THREE.MeshStandardMaterial({ color: 0xcdc9c9, roughness: 0.4 });
        const thickness = 0.3;
        const wallHeight = 3.0;
        function addWall(x, z, width, depth, rotY = 0) {
            const box = new THREE.BoxGeometry(width, wallHeight, depth);
            const mesh = new THREE.Mesh(box, wallMat);
            mesh.position.set(x, wallHeight/2, z);
            mesh.rotation.y = rotY;
            mesh.castShadow = true;
            mesh.receiveShadow = true;
            scene.add(mesh);
        }
        addWall(9, 0, 18, thickness);
        addWall(18, 6, thickness, 12);
        addWall(9, 12, 18, thickness);
        addWall(0, 6, thickness, 12);
        addWall(10, 3.5, thickness, 7);
        addWall(14, 7, 8, thickness);
        addWall(16, 4, 4, thickness);
        addWall(14, 5.5, thickness, 3);

        // --- Doors (3D) ---
        const doorMat = new THREE.MeshStandardMaterial({ color: 0x8B5A2B });
        const knobMat = new THREE.MeshStandardMaterial({ color: 0xFFD700 });
        const doorFront = new THREE.Mesh(new THREE.BoxGeometry(1.0, 2.0, 0.1), doorMat);
        doorFront.position.set(5, 1.0, 0.05);
        doorFront.castShadow = true;
        scene.add(doorFront);
        const knobFront = new THREE.Mesh(new THREE.SphereGeometry(0.08), knobMat);
        knobFront.position.set(5, 1.0, 0.12);
        scene.add(knobFront);
        
        const doorInt = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.0, 1.0), doorMat);
        doorInt.position.set(10.05, 1.0, 3);
        doorInt.castShadow = true;
        scene.add(doorInt);
        const knobInt = new THREE.Mesh(new THREE.SphereGeometry(0.08), knobMat);
        knobInt.position.set(10.12, 1.0, 3);
        scene.add(knobInt);
        
        const doorBath = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.0, 0.8), doorMat);
        doorBath.position.set(14.05, 1.0, 4);
        doorBath.castShadow = true;
        scene.add(doorBath);
        const knobBath = new THREE.Mesh(new THREE.SphereGeometry(0.08), knobMat);
        knobBath.position.set(14.12, 1.0, 4);
        scene.add(knobBath);

        // --- Porch ---
        const porchMat = new THREE.MeshStandardMaterial({ color: 0xc2b280 });
        const porchBase = new THREE.Mesh(new THREE.BoxGeometry(4, 0.2, 2.5), porchMat);
        porchBase.position.set(5, 0, -1.2);
        porchBase.castShadow = true;
        scene.add(porchBase);
        const porchRoofMat = new THREE.MeshStandardMaterial({ color: 0xaa7c4a });
        const porchRoof = new THREE.Mesh(new THREE.BoxGeometry(4.2, 0.1, 2.7), porchRoofMat);
        porchRoof.position.set(5, 2.4, -1.2);
        porchRoof.castShadow = true;
        scene.add(porchRoof);
        const postPos = [[3, -1.2], [7, -1.2]];
        postPos.forEach(pos => {
            const post = new THREE.Mesh(new THREE.BoxGeometry(0.2, 2.2, 0.2), new THREE.MeshStandardMaterial({ color: 0x8B5A2B }));
            post.position.set(pos[0], 1.1, pos[1]);
            post.castShadow = true;
            scene.add(post);
        });

        // --- Doghouse ---
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
        const dogDoorMat = new THREE.MeshStandardMaterial({ color: 0xffaa66 });
        const dogDoor = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.4, 0.05), dogDoorMat);
        dogDoor.position.set(14.3, 0.3, 14);
        scene.add(dogDoor);

        // --- Floor (semi-transparent) ---
        const floorMat = new THREE.MeshStandardMaterial({ color: 0xbc9a6c, roughness: 0.6, metalness: 0.05, transparent: true, opacity: 0.4 });
        const floor = new THREE.Mesh(new THREE.BoxGeometry(18, 0.1, 12), floorMat);
        floor.position.set(9, -0.05, 6);
        floor.receiveShadow = true;
        scene.add(floor);

        // --- Triangular Roof ---
        const roofHeight = 1.8;
        const ridgeHeight = wallHeight + roofHeight;
        const leftSlope = new THREE.BoxGeometry(9, 0.2, 12);
        leftSlope.rotation.x = -Math.atan2(roofHeight, 9);
        leftSlope.position.set(4.5, ridgeHeight - roofHeight/2, 6);
        leftSlope.castShadow = true;
        scene.add(leftSlope);
        const rightSlope = new THREE.BoxGeometry(9, 0.2, 12);
        rightSlope.rotation.x = Math.atan2(roofHeight, 9);
        rightSlope.position.set(13.5, ridgeHeight - roofHeight/2, 6);
        rightSlope.castShadow = true;
        scene.add(rightSlope);
        const ridgeCapMat = new THREE.MeshStandardMaterial({ color: 0xaa8866 });
        const ridgeCap = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.2, 12), ridgeCapMat);
        ridgeCap.position.set(9, ridgeHeight - 0.1, 6);
        ridgeCap.castShadow = true;
        scene.add(ridgeCap);

        // --- Roof Balcony ---
        const balconyY = ridgeHeight - 0.6;
        const balconyWidth = 4, balconyDepth = 3;
        const balconyX = 13.5 + 1;
        const balconyZ = 6;
        const balconyMat = new THREE.MeshStandardMaterial({ color: 0xc2b280 });
        const balconyBase = new THREE.Mesh(new THREE.BoxGeometry(balconyWidth, 0.2, balconyDepth), balconyMat);
        balconyBase.position.set(balconyX, balconyY, balconyZ);
        balconyBase.castShadow = true;
        scene.add(balconyBase);
        const railMat = new THREE.MeshStandardMaterial({ color: 0xaa9977 });
        const railH = 0.8;
        const railT = 0.1;
        const addRail = (x, z, w, d, rot) => {
            const rail = new THREE.Mesh(new THREE.BoxGeometry(w, railH, d), railMat);
            rail.position.set(x, balconyY + railH/2, z);
            rail.castShadow = true;
            scene.add(rail);
        };
        addRail(balconyX, balconyZ - balconyDepth/2, balconyWidth, railT, 0);
        addRail(balconyX, balconyZ + balconyDepth/2, balconyWidth, railT, 0);
        addRail(balconyX - balconyWidth/2, balconyZ, railT, balconyDepth, 0);
        addRail(balconyX + balconyWidth/2, balconyZ, railT, balconyDepth, 0);
        // Table & chair
        const tableMatObj = new THREE.MeshStandardMaterial({ color: 0x8B5A2B });
        const table = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.5, 0.8), tableMatObj);
        table.position.set(balconyX - 0.5, balconyY + 0.3, balconyZ);
        table.castShadow = true;
        scene.add(table);
        const chairMatObj = new THREE.MeshStandardMaterial({ color: 0xaa8866 });
        const chairSeat = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.2, 0.6), chairMatObj);
        chairSeat.position.set(balconyX + 0.7, balconyY + 0.2, balconyZ);
        chairSeat.castShadow = true;
        scene.add(chairSeat);
        const chairBack = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.5, 0.1), chairMatObj);
        chairBack.position.set(balconyX + 0.7, balconyY + 0.45, balconyZ - 0.3);
        chairBack.castShadow = true;
        scene.add(chairBack);

        // --- Exit Door (stairwell) ---
        const exitX = 4.5 - 1.5;
        const exitZ = 6;
        const exitW = 1.2, exitH = 1.8, exitD = 1.5;
        const exitMat = new THREE.MeshStandardMaterial({ color: 0xbc9a6c });
        const exitWalls = new THREE.Mesh(new THREE.BoxGeometry(exitW, exitH, exitD), exitMat);
        exitWalls.position.set(exitX, balconyY + exitH/2, exitZ);
        exitWalls.castShadow = true;
        scene.add(exitWalls);
        const exitRoofMat = new THREE.MeshStandardMaterial({ color: 0xaa7777 });
        const exitRoof = new THREE.Mesh(new THREE.CylinderGeometry(0.9, 0.9, 0.5, 4), exitRoofMat);
        exitRoof.rotation.y = Math.PI/4;
        exitRoof.position.set(exitX, balconyY + exitH, exitZ);
        exitRoof.castShadow = true;
        scene.add(exitRoof);
        const exitDoor = new THREE.Mesh(new THREE.BoxGeometry(0.7, 1.4, 0.08), doorMat);
        exitDoor.position.set(exitX - exitW/2 + 0.05, balconyY + 0.8, exitZ);
        exitDoor.castShadow = true;
        scene.add(exitDoor);
        const exitKnob = new THREE.Mesh(new THREE.SphereGeometry(0.07), knobMat);
        exitKnob.position.set(exitX - exitW/2 + 0.12, balconyY + 0.85, exitZ);
        scene.add(exitKnob);
        const stepMat = new THREE.MeshStandardMaterial({ color: 0xaa8866 });
        for (let i = 0; i < 3; i++) {
            const step = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.2, 0.6), stepMat);
            step.position.set(exitX + 0.8, balconyY + 0.1 + i*0.2, exitZ + 0.4);
            step.castShadow = true;
            scene.add(step);
        }

        // --- CSS2D Labels ---
        function makeLabel(text, x, z, yOffset = 0.2) {
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
            label.position.set(x, yOffset, z);
            scene.add(label);
        }
        makeLabel('LIVING ROOM', 5, 6, 0.2);
        makeLabel('KITCHEN', 14, 3, 0.2);
        makeLabel('BEDROOM 1', 14, 9.5, 0.2);
        makeLabel('BEDROOM 2', 6, 9.5, 0.2);
        makeLabel('BATH', 16, 5.5, 0.2);
        makeLabel('ENTRY', 2, 1, 0.2);
        makeLabel('FRONT YARD', 9, -3, 0.2);
        makeLabel('BACKYARD', 9, 16, 0.2);
        makeLabel('PARKING', 22, 4, 0.2);
        makeLabel('DOGHOUSE', 14, 14.8, 0.2);
        makeLabel('ROOF BALCONY', balconyX, balconyZ, balconyY + 0.6);
        makeLabel('EXIT DOOR', exitX, exitZ, balconyY + 1.0);

        // --- Animation Loop ---
        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
            labelRenderer.render(scene, camera);
        }
        animate();

        // --- Handle window resize ---
        window.addEventListener('resize', onWindowResize);
        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
            labelRenderer.setSize(window.innerWidth, window.innerHeight);
        }
    </script>
</body>
</html>"""

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
        - **Green dashed lines**: Property boundaries (yard, parking)  
        - 2D blueprint (top‑down view)
        """)
else:
    st.markdown("### 🏡 3D Interactive Model – Triangular Roof, Balcony, Exit Door & More")
    st.markdown("_Drag to rotate, right‑click to pan, scroll to zoom._")
    # Use an iframe with srcdoc (pure HTML/CSS/JS) inside st.markdown
    # This avoids deprecation warnings and works reliably.
    iframe_code = f'<iframe srcdoc="{get_3d_html().replace('"', '&quot;')}" width="100%" height="700" style="border:none;"></iframe>'
    st.markdown(iframe_code, unsafe_allow_html=True)
