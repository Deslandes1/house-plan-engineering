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

# ---------- LANGUAGE SELECTION ----------
lang = st.sidebar.selectbox("🌐 Language / Idioma / Langue", ["English", "Español", "Français"])

# ---------- TRANSLATIONS ----------
translations = {
    "English": {
        "title": "🏠 Architectural House Plan",
        "subtitle": "Switch between **2D engineering drawing** and **3D interactive model**.",
        "sidebar_logo": "🌍 GlobalInternet.py",
        "sidebar_name": "**Gesner Deslandes** – Coder in Chief",
        "sidebar_contact": "📞 (509)-47385663  |  ✉️ deslandes78@gmail.com",
        "pricing_title": "### 💰 Market Pricing (Competitive)",
        "pricing_basic": "- **Full house plan (2D + 3D):** **$1,500 USD**",
        "pricing_mod": "- **Custom modifications:** +$300",
        "pricing_landscape": "- **Landscape & exterior design:** +$500",
        "pricing_permit": "- **Permit‑ready drawings:** +$700",
        "pricing_package": "- **Complete package (all of the above):** **$2,800 USD**",
        "pricing_note": "💡 _Prices negotiable for volume or charity projects._",
        "land_title": "### 🌎 Required Land Size",
        "land_min": "The house shown here (18 m × 12 m footprint) plus yards, parking, and fence **requires approximately:**  \n- **0.25 acres** (1,000 m²) for the house + immediate garden.",
        "land_comfort": "- **0.35 – 0.5 acres** for a comfortable layout with front/back yards, parking, and doghouse.",
        "land_reco": "- **Recommendation:** **0.4 acres** (1,600 m²) for full privacy and room to expand.",
        "land_caption": "_Based on typical suburban zoning._",
        "footer": "🔨 **Built by GlobalInternet.py – Python software on demand**",
        "view_selector": "Select view:",
        "view_2d": "2D Blueprint",
        "view_3d": "3D Model",
        "legend_title": "📐 Legend & Instructions",
        "legend_text": """
        - **Black thick lines**: Walls  
        - **Blue arcs & lines**: Doors (arc = swing direction)  
        - **Blue thick segments**: Windows  
        - **Red arrows**: Dimensions (meters)  
        - **Green dashed lines**: Property boundaries (yard, parking)  
        - This is an architectural floor plan (top‑down view).
        """,
        "room_living": "LIVING ROOM",
        "room_kitchen": "KITCHEN",
        "room_bed1": "BEDROOM 1",
        "room_bed2": "BEDROOM 2",
        "room_bath": "BATH",
        "room_entry": "ENTRY",
        "yard_front": "FRONT YARD",
        "yard_back": "BACKYARD",
        "parking_label": "PARKING",
        "doghouse_label": "DOGHOUSE",
        "door_front_label": "FRONT DOOR",
        "info_title": "3D House Model",
        "info_features": "✅ Porch | ✅ Front/Back yards | ✅ Fence | ✅ Parking | ✅ Doghouse | ✅ Doors"
    },
    "Español": {
        "title": "🏠 Plano Arquitectónico",
        "subtitle": "Cambie entre **dibujo de ingeniería 2D** y **modelo interactivo 3D**.",
        "sidebar_logo": "🌍 GlobalInternet.py",
        "sidebar_name": "**Gesner Deslandes** – Jefe de Programación",
        "sidebar_contact": "📞 (509)-47385663  |  ✉️ deslandes78@gmail.com",
        "pricing_title": "### 💰 Precios de Mercado (Competitivos)",
        "pricing_basic": "- **Plano completo (2D + 3D):** **$1,500 USD**",
        "pricing_mod": "- **Modificaciones personalizadas:** +$300",
        "pricing_landscape": "- **Diseño de paisajismo y exteriores:** +$500",
        "pricing_permit": "- **Planos listos para permisos:** +$700",
        "pricing_package": "- **Paquete completo (todo lo anterior):** **$2,800 USD**",
        "pricing_note": "💡 _Precios negociables para proyectos comunitarios o de gran volumen._",
        "land_title": "### 🌎 Tamaño de Terreno Requerido",
        "land_min": "La casa mostrada (18 m × 12 m) más patios, estacionamiento y cerca **requiere aproximadamente:**  \n- **0.25 acres** (1,000 m²) para la casa + jardín inmediato.",
        "land_comfort": "- **0.35 – 0.5 acres** para una distribución cómoda con patios delantero/trasero, estacionamiento y caseta para perro.",
        "land_reco": "- **Recomendación:** **0.4 acres** (1,600 m²) para total privacidad y espacio para expandir.",
        "land_caption": "_Basado en zonificación suburbana típica._",
        "footer": "🔨 **Construido por GlobalInternet.py – Software Python bajo demanda**",
        "view_selector": "Seleccionar vista:",
        "view_2d": "Plano 2D",
        "view_3d": "Modelo 3D",
        "legend_title": "📐 Leyenda e Instrucciones",
        "legend_text": """
        - **Líneas negras gruesas**: Paredes  
        - **Líneas y arcos azules**: Puertas (el arco muestra dirección de apertura)  
        - **Segmentos azules gruesos**: Ventanas  
        - **Flechas rojas**: Dimensiones (metros)  
        - **Líneas verdes discontinuas**: Límites de propiedad (jardín, estacionamiento)  
        - Plano arquitectónico (vista superior).
        """,
        "room_living": "SALA DE ESTAR",
        "room_kitchen": "COCINA",
        "room_bed1": "DORMITORIO 1",
        "room_bed2": "DORMITORIO 2",
        "room_bath": "BAÑO",
        "room_entry": "ENTRADA",
        "yard_front": "JARDÍN DELANTERO",
        "yard_back": "JARDÍN TRASERO",
        "parking_label": "ESTACIONAMIENTO",
        "doghouse_label": "CASETA PARA PERRO",
        "door_front_label": "PUERTA PRINCIPAL",
        "info_title": "Modelo de Casa 3D",
        "info_features": "✅ Porche | ✅ Jardín delantero/trasero | ✅ Cerca | ✅ Estacionamiento | ✅ Caseta | ✅ Puertas"
    },
    "Français": {
        "title": "🏠 Plan Architectural",
        "subtitle": "Passez du **dessin technique 2D** au **modèle interactif 3D**.",
        "sidebar_logo": "🌍 GlobalInternet.py",
        "sidebar_name": "**Gesner Deslandes** – Chef Programmeur",
        "sidebar_contact": "📞 (509)-47385663  |  ✉️ deslandes78@gmail.com",
        "pricing_title": "### 💰 Tarifs Concurrentiels",
        "pricing_basic": "- **Plan complet (2D + 3D) :** **1 500 USD**",
        "pricing_mod": "- **Modifications personnalisées :** +300 USD",
        "pricing_landscape": "- **Aménagement paysager et extérieurs :** +500 USD",
        "pricing_permit": "- **Plans pour permis de construire :** +700 USD",
        "pricing_package": "- **Forfait complet (tout inclus) :** **2 800 USD**",
        "pricing_note": "💡 _Prix négociables pour projets caritatifs ou en volume._",
        "land_title": "### 🌎 Superficie de Terrain Nécessaire",
        "land_min": "La maison présentée (18 m × 12 m) plus jardins, parking et clôture **nécessite environ :**  \n- **0,25 acre** (1 000 m²) pour la maison + jardin immédiat.",
        "land_comfort": "- **0,35 – 0,5 acre** pour une configuration confortable avec jardin avant/arrière, parking et niche.",
        "land_reco": "- **Recommandation :** **0,4 acre** (1 600 m²) pour une intimité totale et de l'espace pour agrandir.",
        "land_caption": "_Basé sur un zonage suburbain typique._",
        "footer": "🔨 **Construit par GlobalInternet.py – Logiciels Python à la demande**",
        "view_selector": "Choisir la vue :",
        "view_2d": "Plan 2D",
        "view_3d": "Modèle 3D",
        "legend_title": "📐 Légende et Instructions",
        "legend_text": """
        - **Lignes noires épaisses** : Murs  
        - **Lignes et arcs bleus** : Portes (l'arc indique le sens d'ouverture)  
        - **Segments bleus épais** : Fenêtres  
        - **Flèches rouges** : Dimensions (mètres)  
        - **Lignes vertes pointillées** : Limites de propriété (jardin, parking)  
        - Plan architectural (vue de dessus).
        """,
        "room_living": "SALON",
        "room_kitchen": "CUISINE",
        "room_bed1": "CHAMBRE 1",
        "room_bed2": "CHAMBRE 2",
        "room_bath": "SALLE DE BAIN",
        "room_entry": "ENTRÉE",
        "yard_front": "JARDIN AVANT",
        "yard_back": "JARDIN ARRIÈRE",
        "parking_label": "PARKING",
        "doghouse_label": "NICHE",
        "door_front_label": "PORTE D'ENTRÉE",
        "info_title": "Modèle 3D de la Maison",
        "info_features": "✅ Porche | ✅ Jardins avant/arrière | ✅ Clôture | ✅ Parking | ✅ Niche | ✅ Portes"
    }
}

t = translations[lang]

# ---------- SIDEBAR CONTENT ----------
with st.sidebar:
    st.markdown(f"## {t['sidebar_logo']}")
    st.markdown(t['sidebar_name'])
    st.markdown(t['sidebar_contact'])
    st.markdown("---")
    
    st.markdown(t['pricing_title'])
    st.markdown(t['pricing_basic'])
    st.markdown(t['pricing_mod'])
    st.markdown(t['pricing_landscape'])
    st.markdown(t['pricing_permit'])
    st.markdown(t['pricing_package'])
    st.info(t['pricing_note'])
    
    st.markdown("---")
    st.markdown(t['land_title'])
    st.markdown(t['land_min'])
    st.markdown(t['land_comfort'])
    st.markdown(t['land_reco'])
    st.caption(t['land_caption'])
    st.markdown("---")
    st.markdown(t['footer'])

# ---------- SIDEBAR TOGGLE ----------
view = st.sidebar.radio(t['view_selector'], [t['view_2d'], t['view_3d']])

# ---------- 2D DRAWING FUNCTION (with translations) ----------
def draw_house_plan(trans):
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

    # Room labels (translated)
    font = FontProperties(weight='bold', size=10)
    ax.text(5, 6, trans['room_living'], ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(14, 3, trans['room_kitchen'], ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(14, 9.5, trans['room_bed1'], ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(6, 9.5, trans['room_bed2'], ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(16, 5.5, trans['room_bath'], ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(2, 0.8, trans['room_entry'], ha='center', va='center', fontproperties=font, bbox=dict(facecolor='white', alpha=0.7))

    # Dimensions (unchanged)
    ax.annotate('', xy=(0, -1), xytext=(18, -1), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(9, -1.5, "18.0 m", ha='center', va='center', color='red', fontsize=9)
    ax.annotate('', xy=(19, 0), xytext=(19, 12), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(19.5, 6, "12.0 m", ha='center', va='center', color='red', fontsize=9, rotation=90)
    ax.annotate('', xy=(0, -1.2), xytext=(10, -1.2), arrowprops=dict(arrowstyle='<->', color='red', lw=1))
    ax.text(5, -1.7, "10.0 m", ha='center', color='red', fontsize=8)

    # Yard and parking boundaries (labels translated)
    ax.plot([-3, -3], [-2, 14], 'g--', linewidth=1, alpha=0.6)
    ax.plot([21, 21], [-2, 14], 'g--', linewidth=1, alpha=0.6)
    ax.plot([-3, 21], [14, 14], 'g--', linewidth=1, alpha=0.6)
    ax.plot([-3, 21], [-2, -2], 'g--', linewidth=1, alpha=0.6)

    ax.text(-2, 6, trans['yard_front'], rotation=90, fontsize=8, color='green', alpha=0.7)
    ax.text(10, 13, trans['yard_back'], fontsize=8, color='green', alpha=0.7, ha='center')
    ax.text(19.5, 4, trans['parking_label'], rotation=90, fontsize=8, color='blue', alpha=0.7)

    return fig

# ---------- 3D MODEL HTML (with translated labels) ----------
def generate_3d_house(trans):
    # Build HTML with dynamic labels
    html = f"""
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
            <strong>{trans['info_title']}</strong><br>
            Drag to rotate | Right-click to pan | Scroll to zoom<br>
            {trans['info_features']}
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
            camera.position.set(22, 14, 18);
            camera.lookAt(9, 0, 6);

            const renderer = new THREE.WebGLRenderer({{ antialias: true }});
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

            // --- Controls ---
            const controls = new OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.rotateSpeed = 0.5;
            controls.zoomSpeed = 1.2;
            controls.panSpeed = 0.8;
            controls.target.set(9, 2, 6);

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

            // --- Ground / Yards ---
            const grassMaterial = new THREE.MeshStandardMaterial({{ color: 0x5a9e4e, roughness: 0.8 }});
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
            const asphalt = new THREE.MeshStandardMaterial({{ color: 0x444444, roughness: 0.7 }});
            const parking = new THREE.Mesh(new THREE.PlaneGeometry(5, 8), asphalt);
            parking.rotation.x = -Math.PI/2;
            parking.position.set(20.5, -0.08, 4);
            parking.receiveShadow = true;
            scene.add(parking);
            const lineMat = new THREE.MeshStandardMaterial({{ color: 0xffffff }});
            for (let i = 0; i < 3; i++) {{
                const line = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.05, 1.5), lineMat);
                line.position.set(20.5, -0.02, 2 + i*2.5);
                line.castShadow = false;
                scene.add(line);
            }}

            // Fence
            const fenceMaterial = new THREE.MeshStandardMaterial({{ color: 0xbc9a6c }});
            const postMat = new THREE.MeshStandardMaterial({{ color: 0x8b5a2b }});
            const fencePoints = [[-3, -2], [21, -2], [21, 14], [-3, 14], [-3, -2]];
            for (let i = 0; i < fencePoints.length - 1; i++) {{
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
                for (let j = 0; j <= numPosts; j++) {{
                    const t = j / numPosts;
                    const px = p1[0] + dx * t;
                    const pz = p1[1] + dz * t;
                    const post = new THREE.Mesh(new THREE.BoxGeometry(0.2, 1.2, 0.2), postMat);
                    post.position.set(px, 0.6, pz);
                    post.castShadow = true;
                    scene.add(post);
                }}
            }}

            // Walls
            const wallMaterial = new THREE.MeshStandardMaterial({{ color: 0xcdc9c9, roughness: 0.4 }});
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
            addWall(9, 0, 18, thickness);
            addWall(18, 6, thickness, 12);
            addWall(9, 12, 18, thickness);
            addWall(0, 6, thickness, 12);
            addWall(10, 3.5, thickness, 7);
            addWall(14, 7, 8, thickness);
            addWall(16, 4, 4, thickness);
            addWall(14, 5.5, thickness, 3);

            // Doors
            const doorMaterial = new THREE.MeshStandardMaterial({{ color: 0x8B5A2B }});
            const knobMat = new THREE.MeshStandardMaterial({{ color: 0xFFD700 }});
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
            const porchMaterial = new THREE.MeshStandardMaterial({{ color: 0xc2b280 }});
            const porchBase = new THREE.Mesh(new THREE.BoxGeometry(4, 0.2, 2.5), porchMaterial);
            porchBase.position.set(5, 0, -1.2);
            porchBase.castShadow = true;
            scene.add(porchBase);
            const porchRoof = new THREE.Mesh(new THREE.BoxGeometry(4.2, 0.1, 2.7), new THREE.MeshStandardMaterial({{ color: 0xaa7c4a }}));
            porchRoof.position.set(5, 2.4, -1.2);
            porchRoof.castShadow = true;
            scene.add(porchRoof);
            const postPositions = [[3, -1.2], [7, -1.2]];
            postPositions.forEach(pos => {{
                const post = new THREE.Mesh(new THREE.BoxGeometry(0.2, 2.2, 0.2), new THREE.MeshStandardMaterial({{ color: 0x8B5A2B }}));
                post.position.set(pos[0], 1.1, pos[1]);
                post.castShadow = true;
                scene.add(post);
            }});

            // Doghouse
            const dogMat = new THREE.MeshStandardMaterial({{ color: 0xaa8c5e }});
            const dogBase = new THREE.Mesh(new THREE.BoxGeometry(1.0, 0.5, 1.2), dogMat);
            dogBase.position.set(14, 0.25, 14);
            dogBase.castShadow = true;
            scene.add(dogBase);
            const dogRoof = new THREE.Mesh(new THREE.CylinderGeometry(0.9, 0.9, 0.5, 4), dogMat);
            dogRoof.rotation.y = Math.PI/4;
            dogRoof.position.set(14, 0.7, 14);
            dogRoof.castShadow = true;
            scene.add(dogRoof);
            const dogDoor = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.4, 0.05), new THREE.MeshStandardMaterial({{ color: 0xffaa66 }}));
            dogDoor.position.set(14.3, 0.3, 14);
            scene.add(dogDoor);

            // Floor
            const floorMat = new THREE.MeshStandardMaterial({{ color: 0xbc9a6c, roughness: 0.6, metalness: 0.05, transparent: true, opacity: 0.5 }});
            const floor = new THREE.Mesh(new THREE.BoxGeometry(18, 0.1, 12), floorMat);
            floor.position.set(9, -0.05, 6);
            floor.receiveShadow = true;
            scene.add(floor);

            // Roof
            const roofMat = new THREE.MeshStandardMaterial({{ color: 0xaa7777 }});
            const roof = new THREE.Mesh(new THREE.CylinderGeometry(9.5, 9.5, 1.2, 4), roofMat);
            roof.rotation.y = Math.PI/4;
            roof.position.set(9, wallHeight - 0.1, 6);
            roof.castShadow = true;
            scene.add(roof);

            // --- Labels (translated) ---
            function makeLabel(text, x, z, yOffset = 1.2) {{
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
            }}
            makeLabel('{trans['room_living']}', 5, 6, 0.2);
            makeLabel('{trans['room_kitchen']}', 14, 3, 0.2);
            makeLabel('{trans['room_bed1']}', 14, 9.5, 0.2);
            makeLabel('{trans['room_bed2']}', 6, 9.5, 0.2);
            makeLabel('{trans['room_bath']}', 16, 5.5, 0.2);
            makeLabel('{trans['room_entry']}', 2, 1, 0.2);
            makeLabel('{trans['yard_front']}', 9, -3, 0.5);
            makeLabel('{trans['yard_back']}', 9, 16, 0.5);
            makeLabel('{trans['parking_label']}', 22, 4, 0.5);
            makeLabel('{trans['doghouse_label']}', 14, 14.8, 0.5);
            makeLabel('{trans['door_front_label']}', 5, 0.1, 1.2);

            // --- Animation loop ---
            function animate() {{
                requestAnimationFrame(animate);
                controls.update();
                renderer.render(scene, camera);
                labelRenderer.render(scene, camera);
            }}
            animate();

            window.addEventListener('resize', onWindowResize);
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
    return html

# ---------- DISPLAY SELECTED VIEW ----------
st.title(t['title'])
st.markdown(t['subtitle'])

if view == t['view_2d']:
    fig = draw_house_plan(t)
    st.pyplot(fig)
    with st.expander(t['legend_title']):
        st.markdown(t['legend_text'])
else:
    st.markdown(f"### {t['info_title']}")
    st.markdown("_Drag to rotate, right‑click to pan, scroll to zoom._")
    components.html(generate_3d_house(t), height=700, scrolling=False)
