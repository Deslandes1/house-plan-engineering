import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- PAGE CONFIG ---
st.set_page_config(page_title="Professional House Plan Engineering", layout="wide")

# --- 2D BLUEPRINT ENGINE ---
def draw_house_plan():
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Property Boundary (Green Dashed)
    property_bound = patches.Rectangle((-2, -2), 14, 12, linewidth=2, edgecolor='green', facecolor='none', linestyle='--')
    ax.add_patch(property_bound)
    
    # Main Structure (Walls)
    # Living Room & Kitchen
    house_base = patches.Rectangle((0, 0), 10, 8, linewidth=4, edgecolor='black', facecolor='#f0f0f0')
    ax.add_patch(house_base)
    
    # Internal Walls
    plt.plot([5, 5], [0, 8], color='black', linewidth=3) # Vertical Divider
    plt.plot([5, 10], [4, 4], color='black', linewidth=3) # Horizontal Divider
    
    # Windows (Blue Segments)
    plt.plot([2, 4], [8, 8], color='blue', linewidth=6) # Front Window 1
    plt.plot([6, 8], [8, 8], color='blue', linewidth=6) # Front Window 2
    plt.plot([10, 10], [1, 3], color='blue', linewidth=6) # Side Window
    
    # Door Arcs
    # Main Entrance
    entrance_door = patches.Arc((4.5, 0), 1.5, 1.5, theta1=0, theta2=90, color='blue', linewidth=2)
    ax.add_patch(entrance_door)
    plt.plot([4.5, 4.5], [0, 0.75], color='blue', linewidth=2)
    
    # Labels
    plt.text(2.5, 4, 'Living Area', fontsize=12, ha='center', fontweight='bold')
    plt.text(7.5, 6, 'Bedroom 1', fontsize=12, ha='center', fontweight='bold')
    plt.text(7.5, 2, 'Kitchen / Dining', fontsize=12, ha='center', fontweight='bold')
    
    # Dimensions
    ax.annotate('', xy=(0, -0.5), xytext=(10, -0.5), arrowprops=dict(arrowstyle='<->', color='red'))
    plt.text(5, -0.8, '10.0m', color='red', ha='center')
    
    ax.annotate('', xy=(-0.5, 0), xytext=(-0.5, 8), arrowprops=dict(arrowstyle='<->', color='red'))
    plt.text(-1.2, 4, '8.0m', color='red', va='center', rotation=90)

    # Plot Styling
    ax.set_xlim(-3, 15)
    ax.set_ylim(-3, 11)
    ax.set_aspect('equal')
    plt.axis('off')
    return fig

# --- 3D HTML ENGINE ---
def get_3d_html():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; overflow: hidden; background-color: #1a1a2e; }
            #info {
                position: absolute; top: 10px; left: 10px; color: white;
                background: rgba(0,0,0,0.6); padding: 8px; border-radius: 5px;
                font-family: sans-serif; pointer-events: none; z-index: 10;
            }
        </style>
    </head>
    <body>
        <div id="info"><b>3D Preview</b>: Drag to Rotate</div>
        <script type="importmap">
            { "imports": { "three": "https://unpkg.com/three@0.128.0/build/three.module.js" } }
        </script>
        <script type="module">
            import * as THREE from 'three';
            
            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x87ceeb);
            
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
            camera.position.set(8, 5, 8);
            camera.lookAt(0, 1, 0);

            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.body.appendChild(renderer.domElement);

            // House Geometry
            const geometry = new THREE.BoxGeometry(6, 4, 4);
            const material = new THREE.MeshStandardMaterial({ color: 0xffffff });
            const house = new THREE.Mesh(geometry, material);
            house.position.y = 2;
            scene.add(house);

            // Roof
            const roofGeo = new THREE.ConeGeometry(5, 2, 4);
            const roofMat = new THREE.MeshStandardMaterial({ color: 0x8b4513 });
            const roof = new THREE.Mesh(roofGeo, roofMat);
            roof.position.y = 5;
            roof.rotation.y = Math.PI / 4;
            scene.add(roof);

            // Lights
            const light = new THREE.DirectionalLight(0xffffff, 1);
            light.position.set(5, 10, 7.5);
            scene.add(light);
            scene.add(new THREE.AmbientLight(0x404040));

            function animate() {
                requestAnimationFrame(animate);
                house.rotation.y += 0.005;
                roof.rotation.y += 0.005;
                renderer.render(scene, camera);
            }
            animate();
        </script>
    </body>
    </html>
    """

# --- MAIN APP INTERFACE ---
def main():
    st.title("🏗️ Professional House Plan Engineering")
    st.sidebar.header("Control Panel")
    
    view = st.sidebar.radio("Select View Mode", ["2D Blueprint", "3D Interactive Model"])
    
    st.sidebar.divider()
    st.sidebar.info("This tool generates engineering-grade house plans and interactive 3D visualizations.")

    if view == "2D Blueprint":
        st.subheader("Architectural 2D Layout")
        col1, col2 = st.columns([3, 1])
        
        with col1:
            fig = draw_house_plan()
            st.pyplot(fig)
        
        with col2:
            st.markdown("### Specifications")
            st.write("- **Total Area:** 80 m²")
            st.write("- **Rooms:** 3 + Kitchen")
            st.write("- **Scale:** 1:100")
            st.download_button("Download Blueprint (PNG)", "blueprint.png", "image/png")

    else:
        st.subheader("3D Structural Visualization")
        # Fixed the call to use the stable components.html to avoid the srcdoc error
        components.html(get_3d_html(), height=600)

if __name__ == "__main__":
    main()
