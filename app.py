import os
import re
import logging
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Curated public GitHub projects for Pratyush Anand
PROJECTS = [
    {
        "id": "gumpwiser",
        "title": "GumpWiser",
        "badge": "Civic AI Sensing",
        "category": "AI & Civic Tech",
        "featured": True,
        "description": "Real-time civic intelligence and rumor-sensing platform built for World Wide Vibes. Ingests hyper-local social sentiment, senses community rumors, and cross-references them against official city and municipal APIs to deliver real-time reality checks.",
        "technologies": ["TypeScript", "AI Sensing", "Node.js", "Civic APIs", "Real-Time NLP"],
        "github": "https://github.com/PratyushAnand-Git/GumpWiser",
        "demo": "#",
        "metrics": "World Wide Vibes Hackathon",
        "architecture_note": "Multi-stream pipeline combining social rumor ingestion, sentiment scoring, and verifiable municipal data cross-referencing."
    },
    {
        "id": "refinesimmer",
        "title": "RefineSimmer (iOS)",
        "badge": "Apple WWDC-26",
        "category": "iOS Engineering",
        "featured": True,
        "description": "High-fidelity native iOS application developed for Apple WWDC-26 (AATC PU). Implements an interactive culinary simulation experience leveraging SwiftUI, smooth physical spring gestures, modern Swift concurrency, and Apple Human Interface Guidelines.",
        "technologies": ["Swift", "SwiftUI", "Combine", "iOS SDK", "WWDC '26"],
        "github": "https://github.com/PratyushAnand-Git/RefineSimmer",
        "demo": "#",
        "metrics": "WWDC-26 Candidate Project",
        "architecture_note": "Unidirectional Data Flow (UDF) architecture with granular SwiftUI view updates, tactile haptic feedback, and dynamic layout responsiveness."
    },
    {
        "id": "nomadid",
        "title": "NomadID",
        "badge": "Cross-Platform Identity",
        "category": "Mobile & Security",
        "featured": True,
        "description": "A cross-platform decentralized identity management solution built with React Native. Enables remote professionals and digital nomads to manage portable verified credentials, cryptographic authentication, and zero-knowledge identity assertions on mobile.",
        "technologies": ["React Native", "TypeScript", "Cryptography", "Mobile Security", "Offline-First"],
        "github": "https://github.com/PratyushAnand-Git/NomadID",
        "demo": "#",
        "metrics": "Zero-Knowledge Credentialing",
        "architecture_note": "Secure enclave key generation, portable identity schema validation, and offline-first mobile sync mechanism."
    },
    {
        "id": "chakra",
        "title": "Project CHAKRA",
        "badge": "Agentic Digital Twin",
        "category": "Systems & AI",
        "featured": False,
        "description": "Cognitive Heuristic for Anticipatory Knowledge & Resilience in Energy. An agentic multi-agent orchestrator and geospatial digital twin designed to monitor, simulate, and dynamically optimize national energy supply chains and contingency rerouting.",
        "technologies": ["TypeScript", "Agentic AI", "Constraint Solvers", "Geospatial", "System Design"],
        "github": "https://github.com/PratyushAnand-Git/CHAKRA",
        "demo": "#",
        "metrics": "Multi-Agent Orchestration",
        "architecture_note": "Agent coordination protocols backed by constraint satisfaction solvers and live geospatial telemetry."
    },
    {
        "id": "relocate-smart",
        "title": "RelocateSmart",
        "badge": "Civic & Commute Intelligence",
        "category": "Full-Stack & Data",
        "featured": False,
        "description": "A legally compliant commute and civic intelligence engine for Indian job seekers. Computes optimal living zones by analyzing 9 AM rush-hour traffic matrices, hospital access, and verified open municipal records under DPDPA 2023 & IT Rules compliance.",
        "technologies": ["TypeScript", "Geospatial Analytics", "Traffic Algorithms", "Municipal APIs", "DPDPA 2023"],
        "github": "https://github.com/PratyushAnand-Git/Relocate_Smart",
        "demo": "#",
        "metrics": "Commute Matrix Optimization",
        "architecture_note": "Multi-criteria spatial decision analysis (MCDA) engine evaluating commute distance, rush-hour bottlenecks, and municipal infrastructure."
    },
    {
        "id": "identityxr",
        "title": "IdentityXR",
        "badge": "Spatial Computing & WebXR",
        "category": "UI/UX & Spatial Web",
        "featured": False,
        "description": "An experimental immersive WebXR interface bridging spatial UI/UX interaction models with identity assertion. Features interactive 3D spatial widgets, tactile UI motion, and modern progressive rendering.",
        "technologies": ["JavaScript", "WebXR", "React", "3D Graphics", "Spatial Interaction"],
        "github": "https://github.com/PratyushAnand-Git/IdentityXR",
        "demo": "#",
        "metrics": "Spatial UI/UX Prototype",
        "architecture_note": "6-DoF spatial input listeners, shaders for dynamic ambient lighting, and high-performance WebGL state pipeline."
    }
]

@app.route('/')
def index():
    return render_template('index.html', projects=PROJECTS)

@app.route('/api/projects', methods=['GET'])
def get_projects():
    return jsonify(PROJECTS), 200

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid request body. Expected JSON."}), 400
    
    name = (data.get('name') or '').strip()
    email = (data.get('email') or '').strip()
    message = (data.get('message') or '').strip()

    if not name or len(name) < 2 or not re.match(r"^[A-Za-z\s.\-']+$", name):
        return jsonify({"error": "Please provide a valid name (at least 2 letters)."}), 400

    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email or not re.match(email_pattern, email):
        return jsonify({"error": "Please provide a valid email address."}), 400

    if not message or len(message) < 10:
        return jsonify({"error": "Message must be at least 10 characters long."}), 400

    app.logger.info(f"Contact inquiry from '{name}' <{email}>: {message}")

    return jsonify({
        "success": True,
        "message": f"Thank you, {name}! Your message has been received successfully."
    }), 200

@app.errorhandler(404)
def not_found(e):
    return render_template('index.html', projects=PROJECTS), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
