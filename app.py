def get_3d_html():
    return """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; overflow: hidden; background-color: #1a1a2e; }
        #info {
            position: absolute; top: 20px; left: 20px; color: white;
            background: rgba(0,0,0,0.7); padding: 10px 20px; border-radius: 12px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; pointer-events: none; z-index: 100;
            border: 1px solid rgba(255,255,255,0.2);
        }
    </style>
</head>
<body>
    <div id="info">🏠 Modern Architectural Preview | Drag to Orbit | Scroll to Zoom</div>
    <script type="importmap">
        {
            "imports": {
                "three": "https://unpkg.com/three@0.160.0/build/three.module.js",
                "three/addons/": "https://unpkg.com/three@0.160.0/examples/jsm/"
            }
        }
    </script>
    <script type="module">
        import * as THREE from 'three';
        import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

        // --- Scene & Camera ---
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x87ceeb); // Sky blue
        scene.fog = new THREE.Fog(0x87ceeb, 20, 100);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(12, 8, 12);

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        document.body.appendChild(renderer.domElement);

        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.target.set(0, 1.5, 0);

        // --- Lighting ---
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
        scene.add(ambientLight);

        const sunLight = new THREE.DirectionalLight(0xffffff, 1.2);
        sunLight.position.set(10, 20, 10);
        sunLight.castShadow = true;
        sunLight.shadow.mapSize.width = 2048;
        sunLight.shadow.mapSize.height = 2048;
        scene.add(sunLight);

        // --- Ground ---
        const groundGeo = new THREE.CircleGeometry(50, 64);
        const groundMat = new THREE.MeshStandardMaterial({ color: 0x3d5a35, roughness: 1 });
        const ground = new THREE.Mesh(groundGeo, groundMat);
        ground.rotation.x = -Math.PI / 2;
        ground.receiveShadow = true;
        scene.add(ground);

        // --- House Base ---
        const houseGroup = new THREE.Group();
        scene.add(houseGroup);

        const wallMat = new THREE.MeshStandardMaterial({ color: 0xfaf9f6, roughness: 0.5 });
        const houseBase = new THREE.Mesh(new THREE.BoxGeometry(6, 3.5, 5), wallMat);
        houseBase.position.y = 1.75;
        houseBase.castShadow = true;
        houseBase.receiveShadow = true;
        houseGroup.add(houseBase);

        // --- Realistic Gabled Roof ---
        const roofShape = new THREE.Shape();
        roofShape.moveTo(-3.5, 0);
        roofShape.lineTo(0, 2.5);
        roofShape.lineTo(3.5, 0);
        roofShape.lineTo(-3.5, 0);

        const extrudeSettings = { depth: 6, bevelEnabled: false };
        const roofGeo = new THREE.ExtrudeGeometry(roofShape, extrudeSettings);
        const roofMat = new THREE.MeshStandardMaterial({ color: 0x4a4a4a, roughness: 0.8 });
        const roof = new THREE.Mesh(roofGeo, roofMat);
        roof.position.set(0, 3.5, 3);
        roof.rotation.y = Math.PI / 2;
        roof.castShadow = true;
        houseGroup.add(roof);

        // --- Windows ---
        function createWindow(x, y, z, rotY = 0) {
            const winGroup = new THREE.Group();
            // Frame
            const frame = new THREE.Mesh(new THREE.BoxGeometry(1.2, 1.2, 0.15), new THREE.MeshStandardMaterial({ color: 0x222222 }));
            // Glass
            const glass = new THREE.Mesh(new THREE.BoxGeometry(1.0, 1.0, 0.1), new THREE.MeshStandardMaterial({ 
                color: 0xadd8e6, transparent: true, opacity: 0.6, roughness: 0 
            }));
            winGroup.add(frame, glass);
            winGroup.position.set(x, y, z);
            winGroup.rotation.y = rotY;
            houseGroup.add(winGroup);
        }

        createWindow(1.5, 2, 2.5);   // Front Right
        createWindow(-1.5, 2, 2.5);  // Front Left
        createWindow(3, 2, 0, Math.PI/2); // Side

        // --- Door & Porch ---
        const door = new THREE.Mesh(new THREE.BoxGeometry(1, 2.2, 0.1), new THREE.MeshStandardMaterial({ color: 0x5d4037 }));
        door.position.set(0, 1.1, 2.5);
        houseGroup.add(door);

        const porch = new THREE.Mesh(new THREE.BoxGeometry(2, 0.2, 1.5), new THREE.MeshStandardMaterial({ color: 0x888888 }));
        porch.position.set(0, 0.1, 3.2);
        porch.receiveShadow = true;
        scene.add(porch);

        // --- Chimney ---
        const chimney = new THREE.Mesh(new THREE.BoxGeometry(0.8, 4, 0.8), new THREE.MeshStandardMaterial({ color: 0x7b3f00 }));
        chimney.position.set(-1.8, 4, -1);
        chimney.castShadow = true;
        houseGroup.add(chimney);

        // --- Animation ---
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
