# AIROS Voice Development Guide

## Project Structure

```
AIROS-Voice/
├── android/              → Native Android application
│   ├── app/
│   ├── ui/
│   ├── services/
│   ├── network/
│   ├── database/
│   ├── models/
│   ├── repository/
│   ├── permissions/
│   ├── navigation/
│   ├── utils/
│   └── build.gradle
│
├── backend/              → Speech-to-text backend
│   ├── api/
│   ├── services/
│   ├── transcriber/
│   ├── models/
│   ├── database/
│   ├── config/
│   ├── utils/
│   ├── requirements.txt
│   └── main.py
│
├── docs/                 → Documentation
│   ├── blueprint/
│   ├── architecture/
│   └── development/
│
├── assets/               → Icons and branding
│   ├── icons/
│   ├── images/
│   └── branding/
│
└── README.md
```

## Development Principles

1. **One responsibility per module** — Each folder has a single, clear purpose.
2. **Minimal duplication** — Avoid repeating code across modules.
3. **Clean architecture** — Separate concerns. Keep Android and backend independent.
4. **Modular design** — Modules should evolve independently.
5. **Production quality** — Write code as if it will be shipped immediately.

## Android Development

### Setup

```bash
cd android
./gradlew build
```

### Build APK

```bash
./gradlew assembleDebug
```

### Install on Device

```bash
./gradlew installDebug
```

### Project Structure

- **app/** — Main application logic and entry point
- **ui/** — UI components, screens, and fragments
- **services/** — Background services and system integration
- **network/** — HTTP communication with backend
- **database/** — Local transcript storage
- **models/** — Data classes and entities
- **repository/** — Data access abstraction layer
- **permissions/** — Android permission handling
- **navigation/** — Screen navigation and flow
- **utils/** — Utility functions and helpers

## Backend Development

### Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run Locally

```bash
python main.py
```

The backend will start on `http://localhost:5000` (or configured port).

### Project Structure

- **api/** — REST API endpoints
- **services/** — Business logic and services
- **transcriber/** — Speech recognition integration
- **models/** — Data models and schemas
- **database/** — Database operations
- **config/** — Configuration management
- **utils/** — Utility functions

## Git Workflow

### Branch Naming

- `feature/milestone-X-description` — New milestone feature
- `fix/issue-description` — Bug fix
- `chore/maintenance-task` — Maintenance or setup

### Commit Convention

```
type: brief description

Longer explanation if needed.
```

**Types:**
- `feat:` — New feature
- `fix:` — Bug fix
- `chore:` — Setup, configuration, or maintenance
- `docs:` — Documentation
- `refactor:` — Code refactoring
- `test:` — Testing

### Example

```
feat: Implement floating bubble component

- Create BubbleService
- Handle bubble visibility
- Implement tap detection
```

## Testing

### Android Testing

```bash
cd android
./gradlew test                    # Unit tests
./gradlew connectedAndroidTest    # Instrumented tests
```

### Backend Testing

```bash
cd backend
pytest
```

## Environment Variables

Create a `.env` file in the backend directory:

```
BACKEND_URL=http://localhost:5000
WHISPER_MODEL=base
DEBUG=True
```

**Never commit `.env` to version control.**

## Deployment

### Android

APK will be generated in `android/app/build/outputs/apk/`.

### Backend

Deploy to Render using the configured settings. See `backend/config/` for deployment configuration.

## Documentation

All architectural decisions and design docs belong in:

- `docs/blueprint/` — AIROS Voice Master Blueprint
- `docs/architecture/` — Technical architecture decisions
- `docs/development/` — Development notes and guides

## Version Tracking

Current version: **1.0-foundation** (Milestone 1)

Version updates are made only upon milestone completion.
