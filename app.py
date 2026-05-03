import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(page_title="House Plan Pro", layout="wide")

st.title("🏠 Engineering House Plan & 3D Model")

# Toggle between 2D and 3D
view_mode = st.sidebar.radio("Switch View", ["2D Engineering Drawing", "3D Interactive Model"])

def draw_2d_blueprint():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(-2, 20)
    ax.set_ylim(-4, 15)
    ax.set_aspect('equal')
    
    # Main Outer Walls
    # Removed solid_capstyle to fix Python 3.14/Matplotlib 3.10 error
    ax.add_patch(patches.Rectangle((0, 0), 18, 12, linewidth=4, edgecolor='black', facecolor='none'))
    
    # Internal Divisions
    ax.plot([10, 10], [0, 7], color='black', linewidth=3) # Living/Kitchen wall
    ax.plot([10, 18], [7, 7], color='black', linewidth=3) # Kitchen/Bed wall
    
    # Balcony (Dashed Line)
    ax.add_patch(patches.Rectangle((-0.5, -0.5), 19, 13, linewidth=1, edgecolor='red', linestyle='--', facecolor='none'))
    
    # Annotations
    ax.text(5, 6, "LIVING ROOM", ha='center', fontsize=12, fontweight='bold')
    ax.text(14, 3.5, "KITCHEN", ha='center', fontsize=10)
    ax.text(14, 9.5, "BEDROOM", ha='center', fontsize=10)
    
    ax.set_title("Project: Residential Floor Plan", loc='left', fontsize=14)
    ax.axis('off')
    return fig

def get_3d_html():
    return """
    <div id="container"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0xeeeeee);
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({antialias: true});
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Lighting
        const light = new THREE.DirectionalLight(0xffffff, 1);
        light.position.set(5, 10, 7.5);
        scene.add(light);
        scene.add(new THREE.AmbientLight(0x404040));

        // House Base
        const geometry = new THREE.BoxGeometry(18, 3, 12);
        const material = new THREE.MeshStandardMaterial({ color: 0xcccccc });
        const house = new THREE.Mesh(geometry, material);
        house.position.y = 1.5;
        scene.add(house);

        // Balcony (The missing piece)
        const balconyGeo = new THREE.BoxGeometry(19, 0.2, 13);
        const balconyMat = new THREE.MeshStandardMaterial({ color: 0x88aaff, transparent: true, opacity: 0.6 });
        const balcony = new THREE.Mesh(balconyGeo, balconyMat);
        balcony.position.y = 3.1;
        scene.add(balcony);

        // Ground
        const ground = new THREE.Mesh(new THREE.PlaneGeometry(40, 40), new THREE.MeshStandardMaterial({color: 0x999999}));
        ground.rotation.x = -Math.PI / 2;
        scene.add(ground);

        camera.position.set(20, 15, 20);
        camera.lookAt(0, 0, 0);

        function animate() {
            requestAnimationFrame(animate);
            house.rotation.y += 0.005;
            balcony.rotation.y += 0.005;
            renderer.render(scene, camera);
        }
        animate();
    </script>
    <style>body { margin: 0; }</style>
    """

if view_mode == "2D Engineering Drawing":
    st.pyplot(draw_2d_blueprint())
else:
    # Using the standard component to avoid the iframe 'srcdoc' keyword error
    components.html(get_3d_html(), height=600)
