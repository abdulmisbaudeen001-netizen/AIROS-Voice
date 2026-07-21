# AIROS Voice V1

**Private AI-powered voice-to-text system for Android.**

Transform spoken audio into text with the fastest and most seamless experience possible.

## Project Vision

AIROS Voice is designed around one simple principle: **Voice becomes another keyboard.**

The user should feel that speaking is faster than typing. The interaction must become muscle memory.

Touch. Speak. Done.

## Architecture

```
AIROS Voice
├── android/          → Native Android application
├── backend/          → Speech-to-text backend (Render)
├── docs/             → Documentation and blueprints
├── assets/           → Icons and branding
└── README.md
```

### Components

- **Android Application** — Floating bubble, audio recording, text insertion, history archive
- **Backend (Render)** — Speech recognition, transcript processing
- **History Archive** — Transcript storage and retrieval

## Quick Start

### Android Development

```bash
cd android
./gradlew build
./gradlew installDebug
```

### Backend Development

```bash
cd backend
pip install -r requirements.txt
python main.py
```

## Development Milestones

1. ✅ **Milestone 1** — Project Foundation
2. ⬜ **Milestone 2** — Android Foundation
3. ⬜ **Milestone 3** — Bubble & Recording
4. ⬜ **Milestone 4** — Backend Integration
5. ⬜ **Milestone 5** — Text Insertion
6. ⬜ **Milestone 6** — History
7. ⬜ **Milestone 7** — Stability
8. ⬜ **Milestone 8** — Release

## Documentation

See `/docs/blueprint/` for the complete AIROS Voice Master Blueprint.

## License

Proprietary. See LICENSE for details.

## Status

**Version 1.0 — Foundation Phase**

The blueprint is approved. Development is underway.
