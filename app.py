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
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            pointer-events: none; z-index: 100; border-left: 5px solid #ffcc00;
        }
    </style>
</head>
<body>
    <div id="info">
        <b style="font-size: 18px;">🏗️ Modern Villa Model</b><br>
        Left Click: Rotate | Right Click: Pan | Scroll: Zoom
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

        // --- Scene & Camera Setup ---
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x87ceeb); // Sky Blue
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
        controls.target.set(0, 1, 0);

        // --- Lighting (Cinematic) ---
        const hemiLight = new THREE.HemisphereLight(0xffffff, 0x444444, 0.6);
        scene.add(hemiLight);

        const sunLight = new THREE.DirectionalLight(0xffffff, 1.2);
        sunLight.position.set(10, 20, 10);
        sunLight.castShadow = true;
        sunLight.shadow.mapSize.width = 2048;
        sunLight.shadow.mapSize.height = 2048;
        scene.add(sunLight);

        // --- Materials ---
        const wallMat = new THREE.MeshStandardMaterial({ color: 0xf5f5f5, roughness: 0.8 });
        const roofMat = new THREE.MeshStandardMaterial({ color: 0x3d3d3d, metalness: 0.3, roughness: 0.4 });
        const grassMat = new THREE.MeshStandardMaterial({ color: 0x4e7a3e, roughness: 1 });
        const woodMat = new THREE.MeshStandardMaterial({ color: 0x5d4037 });
        const glassMat = new THREE.MeshStandardMaterial({ 
            color: 0x88ccff, 
            transparent: true, 
            opacity: 0.6, 
            metalness: 0.9, 
            roughness: 0.1 
        });

        // --- Building Elements ---
        
        // Grass Base
        const ground = new THREE.Mesh(new THREE.CircleGeometry(50, 32), grassMat);
        ground.rotation.x = -Math.PI / 2;
        ground.receiveShadow = true;
        scene.add(ground);

        // Main House Body
        const house = new THREE.Mesh(new THREE.BoxGeometry(6, 4, 5), wallMat);
        house.position.y = 2;
        house.castShadow = true;
        house.receiveShadow = true;
        scene.add(house);

        // Modern Flat/Sloped Roof
        const roof = new THREE.Mesh(new THREE.BoxGeometry(7, 0.5, 6), roofMat);
        roof.position.set(0, 4.2, 0);
        roof.rotation.z = 0.05; // Slight architectural tilt
        roof.castShadow = true;
        scene.add(roof);

        // Front Door with Frame
        const doorFrame = new THREE.Mesh(new THREE.BoxGeometry(1.2, 2.2, 0.1), woodMat);
        doorFrame.position.set(0, 1.1, 2.51);
        scene.add(doorFrame);

        // Windows (Glass Effect)
        const win1 = new THREE.Mesh(new THREE.BoxGeometry(1.5, 1.5, 0.1), glassMat);
        win1.position.set(-1.8, 2.2, 2.51);
        scene.add(win1);

        const win2 = win1.clone();
        win2.position.set(1.8, 2.2, 2.51);
        scene.add(win2);

        // --- Environment (Trees) ---
        function createTree(x, z) {
            const group = new THREE.Group();
            const trunk = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 1.5), woodMat);
            const leaves = new THREE.Mesh(new THREE.SphereGeometry(1, 8, 8), new THREE.MeshStandardMaterial({color: 0x2d5a27}));
            leaves.position.y = 1.2;
            trunk.castShadow = true;
            group.add(trunk);
            group.add(leaves);
            group.position.set(x, 0.75, z);
            scene.add(group);
        }

        createTree(-6, -4);
        createTree(6, -3);
        createTree(-5, 6);

        // --- Animation Loop ---
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
