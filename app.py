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

# ---------- 3D VIEW (Three.js) with triangular roof, balcony, exit door ----------
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
            ✅ Triangular roof | ✅ Roof balcony | ✅ Exit door | ✅ All features
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

            // Setup
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

            const controls = new OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.rotateSpeed = 0.5;
            controls.zoomSpeed = 1.2;
            controls.panSpeed = 0.8;
            controls.target.set(9, 3, 6);

            // Lighting
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

            // Ground / Yards
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

            // Parking
            const asphalt = new THREE.MeshStandardMaterial({ color: 0x444444, roughness: 0.7 });
            const parking = new THREE.Mesh(new THREE.PlaneGeometry(5, 8), asphalt);
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

            // Fence
            const fenceMaterial = new THREE.MeshStandardMaterial({ color: 0xbc9a6c });
            const postMat = new THREE.MeshStandardMaterial({ color: 0x8b5a2b });
            const fencePoints = [[-3, -2], [21, -2], [21, 14], [-3, 14], [-3, -2]];
            for (let i = 0; i < fencePoints.length - 1; i++) {
                const p1 = fencePoints[i];
                const p2 = fencePoints[i+1];
                const dx = p2[0] - p1[0];
                const dz = p2[1] - p1[1];
                const length = Math.hypot(dx, dz);
                const angle = Math.atan2(dz, dx);
                const rail = new THREE.Mesh(new THREE.BoxGeometry(length, 0.1, 0.2), fenceMaterial);
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

            // House walls (same as before)
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
            addWall(9, 0, 18, thickness);
            addWall(18, 6, thickness, 12);
            addWall(9, 12, 18, thickness);
            addWall(0, 6, thickness, 12);
            addWall(10, 3.5, thickness, 7);
            addWall(14, 7, 8, thickness);
            addWall(16, 4, 4, thickness);
            addWall(14, 5.5, thickness, 3);

            // Doors (3D)
            const doorMaterial = new THREE.MeshStandardMaterial({ color: 0x8B5A2B });
            const knobMat = new THREE.MeshStandardMaterial({ color: 0xFFD700 });
            const doorFront = new THREE.Mesh(new THREE.BoxGeometry(1.0, 2.0, 0.1), doorMaterial);
            doorFront.position.set(5, 1.0, 0.05);
            doorFront.castShadow = true;
            scene.add(doorFront);
            const knobFront = new THREE.Mesh(new THREE.SphereGeometry(0.08), knobMat);
            knobFront.position.set(5, 1.0, 0.12);
            scene.add(knobFront);
            
            const doorInt = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.0, 1.0), doorMaterial);
            doorInt.position.set(10.05, 1.0, 3);
            doorInt.castShadow = true;
            scene.add(doorInt);
            const knobInt = new THREE.Mesh(new THREE.SphereGeometry(0.08), knobMat);
            knobInt.position.set(10.12, 1.0, 3);
            scene.add(knobInt);
            
            const doorBath = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.0, 0.8), doorMaterial);
            doorBath.position.set(14.05, 1.0, 4);
            doorBath.castShadow = true;
            scene.add(doorBath);
            const knobBath = new THREE.Mesh(new THREE.SphereGeometry(0.08), knobMat);
            knobBath.position.set(14.12, 1.0, 4);
            scene.add(knobBath);

            // Porch
            const porchMaterial = new THREE.MeshStandardMaterial({ color: 0xc2b280 });
            const porchBase = new THREE.Mesh(new THREE.BoxGeometry(4, 0.2, 2.5), porchMaterial);
            porchBase.position.set(5, 0, -1.2);
            porchBase.castShadow = true;
            scene.add(porchBase);
            const porchRoof = new THREE.Mesh(new THREE.BoxGeometry(4.2, 0.1, 2.7), new THREE.MeshStandardMaterial({ color: 0xaa7c4a }));
            porchRoof.position.set(5, 2.4, -1.2);
            porchRoof.castShadow = true;
            scene.add(porchRoof);
            const postPositions = [[3, -1.2], [7, -1.2]];
            postPositions.forEach(pos => {
                const post = new THREE.Mesh(new THREE.BoxGeometry(0.2, 2.2, 0.2), new THREE.MeshStandardMaterial({ color: 0x8B5A2B }));
                post.position.set(pos[0], 1.1, pos[1]);
                post.castShadow = true;
                scene.add(post);
            });

            // Doghouse
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

            // Floor (semi-transparent)
            const floorMat = new THREE.MeshStandardMaterial({ color: 0xbc9a6c, roughness: 0.6, metalness: 0.05, transparent: true, opacity: 0.5 });
            const floor = new THREE.Mesh(new THREE.BoxGeometry(18, 0.1, 12), floorMat);
            floor.position.set(9, -0.05, 6);
            floor.receiveShadow = true;
            scene.add(floor);

            // *** TRIANGULAR (GABLED) ROOF with BALCONY & EXIT DOOR ***
            const roofMatMain = new THREE.MeshStandardMaterial({ color: 0xaa7777, roughness: 0.6 });
            const roofHeight = 1.8;    // peak height above walls
            const houseWidth = 18;
            const houseDepth = 12;
            // Create a gabled roof using an extruded shape or two rotated boxes.
            // We'll make a single triangular prism for simplicity: a box rotated 45°? Better: CylinderGeometry with 4 sides rotated gives pyramid, not gable.
            // For a gable, we can create two half-roofs as rotated boxes.
            const roofLength = houseDepth; // along Z
            const roofWidth = houseWidth;   // along X
            const ridgeHeight = wallHeight + roofHeight;
            // Left roof slope (from ridge to left wall)
            const leftSlope = new THREE.BoxGeometry(houseWidth/2, 0.2, roofLength);
            leftSlope.rotation.x = -Math.atan2(roofHeight, houseWidth/2);
            leftSlope.position.set(9 - houseWidth/4, ridgeHeight - roofHeight/2, 6);
            leftSlope.castShadow = true;
            scene.add(leftSlope);
            // Right roof slope
            const rightSlope = new THREE.BoxGeometry(houseWidth/2, 0.2, roofLength);
            rightSlope.rotation.x = Math.atan2(roofHeight, houseWidth/2);
            rightSlope.position.set(9 + houseWidth/4, ridgeHeight - roofHeight/2, 6);
            rightSlope.castShadow = true;
            scene.add(rightSlope);
            // Add ridge cap (thin box)
            const ridgeCap = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.2, roofLength), new THREE.MeshStandardMaterial({ color: 0xaa8866 }));
            ridgeCap.position.set(9, ridgeHeight - 0.1, 6);
            ridgeCap.castShadow = true;
            scene.add(ridgeCap);

            // ---- BALCONY on top of the roof (flat area on one side) ----
            // We'll create a flat platform on the right side of the roof (above the right slope) at y = ridgeHeight - 0.5
            const balconyY = ridgeHeight - 0.6;
            const balconyWidth = 4;
            const balconyDepth = 3;
            const balconyX = 9 + houseWidth/4 + 1;
            const balconyZ = 6;
            const balconyMat = new THREE.MeshStandardMaterial({ color: 0xc2b280 });
            const balconyBase = new THREE.Mesh(new THREE.BoxGeometry(balconyWidth, 0.2, balconyDepth), balconyMat);
            balconyBase.position.set(balconyX, balconyY, balconyZ);
            balconyBase.castShadow = true;
            scene.add(balconyBase);
            // Railing around balcony
            const railMat = new THREE.MeshStandardMaterial({ color: 0xaa9977 });
            const railHeight = 0.8;
            const railThick = 0.1;
            // front rail (along X)
            const frontRail = new THREE.Mesh(new THREE.BoxGeometry(balconyWidth, railHeight, railThick), railMat);
            frontRail.position.set(balconyX, balconyY + railHeight/2, balconyZ - balconyDepth/2);
            frontRail.castShadow = true;
            scene.add(frontRail);
            // back rail
            const backRail = new THREE.Mesh(new THREE.BoxGeometry(balconyWidth, railHeight, railThick), railMat);
            backRail.position.set(balconyX, balconyY + railHeight/2, balconyZ + balconyDepth/2);
            backRail.castShadow = true;
            scene.add(backRail);
            // left rail (along Z)
            const leftRail = new THREE.Mesh(new THREE.BoxGeometry(railThick, railHeight, balconyDepth), railMat);
            leftRail.position.set(balconyX - balconyWidth/2, balconyY + railHeight/2, balconyZ);
            leftRail.castShadow = true;
            scene.add(leftRail);
            // right rail
            const rightRail = new THREE.Mesh(new THREE.BoxGeometry(railThick, railHeight, balconyDepth), railMat);
            rightRail.position.set(balconyX + balconyWidth/2, balconyY + railHeight/2, balconyZ);
            rightRail.castShadow = true;
            scene.add(rightRail);
            // Add a small table and chair on balcony (simple boxes)
            const tableMat = new THREE.MeshStandardMaterial({ color: 0x8B5A2B });
            const table = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.5, 0.8), tableMat);
            table.position.set(balconyX - 0.5, balconyY + 0.3, balconyZ);
            table.castShadow = true;
            scene.add(table);
            const chairMat = new THREE.MeshStandardMaterial({ color: 0xaa8866 });
            const chairSeat = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.2, 0.6), chairMat);
            chairSeat.position.set(balconyX + 0.7, balconyY + 0.2, balconyZ);
            chairSeat.castShadow = true;
            scene.add(chairSeat);
            const chairBack = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.5, 0.1), chairMat);
            chairBack.position.set(balconyX + 0.7, balconyY + 0.45, balconyZ - 0.3);
            chairBack.castShadow = true;
            scene.add(chairBack);

            // ---- EXIT DOOR (stairwell / small house on roof) ----
            // Build a small structure on the left side of the roof with a door.
            const exitX = 9 - houseWidth/4 - 1.5;
            const exitZ = 6;
            const exitW = 1.2;
            const exitH = 1.8;
            const exitD = 1.5;
            const exitMat = new THREE.MeshStandardMaterial({ color: 0xbc9a6c });
            const exitWalls = new THREE.Mesh(new THREE.BoxGeometry(exitW, exitH, exitD), exitMat);
            exitWalls.position.set(exitX, balconyY + exitH/2, exitZ);
            exitWalls.castShadow = true;
            scene.add(exitWalls);
            // Roof of exit structure (small triangle)
            const exitRoofMat = new THREE.MeshStandardMaterial({ color: 0xaa7777 });
            const exitRoof = new THREE.Mesh(new THREE.CylinderGeometry(0.9, 0.9, 0.5, 4), exitRoofMat);
            exitRoof.rotation.y = Math.PI/4;
            exitRoof.position.set(exitX, balconyY + exitH, exitZ);
            exitRoof.castShadow = true;
            scene.add(exitRoof);
            // Door on the exit structure (facing outward)
            const exitDoor = new THREE.Mesh(new THREE.BoxGeometry(0.7, 1.4, 0.08), doorMaterial);
            exitDoor.position.set(exitX - exitW/2 + 0.05, balconyY + 0.8, exitZ);
            exitDoor.castShadow = true;
            scene.add(exitDoor);
            const exitKnob = new THREE.Mesh(new THREE.SphereGeometry(0.07), knobMat);
            exitKnob.position.set(exitX - exitW/2 + 0.12, balconyY + 0.85, exitZ);
            scene.add(exitKnob);
            // Stairs from roof to balcony (simple steps)
            const stepMat = new THREE.MeshStandardMaterial({ color: 0xaa8866 });
            for (let i = 0; i < 3; i++) {
                const step = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.2, 0.6), stepMat);
                step.position.set(exitX + 0.8, balconyY + 0.1 + i*0.2, exitZ + 0.4);
                step.castShadow = true;
                scene.add(step);
            }

            // Labels
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
            makeLabel('ROOF BALCONY', balconyX, balconyZ, balconyY + 0.8);
            makeLabel('EXIT DOOR', exitX, exitZ, balconyY + 1.2);

            // Animate
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
        - **Blue arcs & lines**: Doors  
        - **Blue thick segments**: Windows  
        - **Red arrows**: Dimensions (meters)  
        - **Green dashed lines**: Property boundaries  
        - 2D blueprint (top‑down view)
        """)
else:
    st.markdown("### 🏡 3D Interactive Model – With Triangular Roof, Balcony & Exit Door")
    st.markdown("_Drag to rotate, right‑click to pan, scroll to zoom._")
    components.html(generate_3d_house(), height=700, scrolling=False)
