# Pratyush Anand — Software Engineer & UI/UX Architect

A high-performance portfolio website engineered with Python/Flask, modern semantic HTML5, CSS Grid/Flexbox, and vanilla JavaScript. Designed from a **UI/UX Perspective Highlighting Software Engineering**, featuring an integrated background video, dark/light mode theming, and an active showcase of real-world public GitHub projects.

## Highlighted Projects (Public GitHub)

- **[GumpWiser](https://github.com/PratyushAnand-Git/GumpWiser)**: Real-time civic intelligence and rumor-sensing platform built for the World Wide Vibes Hackathon. Senses social misinformation and cross-references against official municipal open data. *(TypeScript / AI / Real-Time NLP)*
- **[RefineSimmer (iOS)](https://github.com/PratyushAnand-Git/RefineSimmer)**: Apple WWDC-26 candidate application (AATC PU). High-performance native iOS culinary simulation built with SwiftUI, fluid gesture physics, and Apple Human Interface Guidelines. *(Swift / SwiftUI / Combine)*
- **[NomadID](https://github.com/PratyushAnand-Git/NomadID)**: Decentralized identity and credential wallet for remote workers and digital nomads. Implements verifiable identity schemas, zero-knowledge proofs, and offline-first mobile sync. *(React Native / TypeScript / Security)*
- **[Project CHAKRA](https://github.com/PratyushAnand-Git/CHAKRA)**: Cognitive Heuristic for Anticipatory Knowledge & Resilience in Energy. Agentic multi-agent orchestrator & geospatial digital twin for national energy supply chains. *(TypeScript / Agentic AI / Constraint Solvers)*
- **[RelocateSmart](https://github.com/PratyushAnand-Git/Relocate_Smart)**: Commute-optimized civic intelligence engine matching housing zones by 9 AM rush-hour traffic matrices and hospital proximity with DPDPA 2023 compliance. *(TypeScript / Geospatial GIS / Traffic Algorithms)*
- **[IdentityXR](https://github.com/PratyushAnand-Git/IdentityXR)**: Experimental spatial computing and WebXR interface exploring 3D interaction models and progressive web graphics. *(JavaScript / WebXR / 3D Graphics)*

## Design & UI/UX Features

- **Ambient Video Hero**: Integrated background video (`bg-hero-0BnFGdr81Ifnj3WbBZoNt1KE4D5DMT.mp4`) with smooth backdrop blur, layered contrast gradients, and an accessible Play/Pause control.
- **Dynamic Theming**: Seamless dark and light modes with system preference detection and local storage persistence.
- **Interactive Project Filtering**: Instant client-side filtering across *All Projects*, *iOS & Native*, *AI & Systems*, *Mobile & Identity*, and *Civic Tech*.
- **Asynchronous Contact Form**: RESTful AJAX form sending to `/api/contact` with instant client-side validation and toast notifications.

## Project Structure

```
portfolio-site/
├── static/
│   ├── css/
│   │   ├── style.css       # Core layout, design tokens, typography, hero video
│   │   ├── dark-mode.css   # Dark mode variables, video overlays, glowing accents
│   │   └── projects.css    # 3D project cards and responsive media queries
│   ├── js/
│   │   ├── main.js         # Navigation, filtering, video toggle, contact AJAX
│   │   └── dark-mode.js    # Theme switching & persistence
│   └── img/                # Profile and project placeholder assets
├── templates/
│   └── index.html          # Main portfolio template with video hero
├── app.py                  # Flask backend with /api/projects & /api/contact
└── requirements.txt        # Minimal Python dependencies
```

## Running the Application

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the application**:
   ```bash
   python app.py
   ```

3. **Open in browser**:
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).

## License

MIT License
