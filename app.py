import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("3D Test - Rotating Cube")

cube_html = """
<!DOCTYPE html>
<html>
<head><style>body { margin: 0; }</style></head>
<body>
<script type="importmap">
  {
    "imports": {
      "three": "https://unpkg.com/three@0.128.0/build/three.module.js"
    }
  }
</script>
<script type="module">
  import * as THREE from 'three';
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x111122);
  const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
  camera.position.set(2,2,2);
  camera.lookAt(0,0,0);
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);
  const geometry = new THREE.BoxGeometry(1,1,1);
  const material = new THREE.MeshStandardMaterial({ color: 0x44aa88 });
  const cube = new THREE.Mesh(geometry, material);
  scene.add(cube);
  const light = new THREE.DirectionalLight(0xffffff, 1);
  light.position.set(1,2,1);
  scene.add(light);
  function animate() {
    requestAnimationFrame(animate);
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    renderer.render(scene, camera);
  }
  animate();
</script>
</body>
</html>
"""
components.html(cube_html, height=600)
