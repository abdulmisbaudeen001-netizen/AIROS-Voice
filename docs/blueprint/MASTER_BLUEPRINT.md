# AIROS Voice Master Blueprint

## Version 1.0 — Foundation

This is the complete approved blueprint for AIROS Voice V1.

All implementation must reference this document as the single source of truth.

---

## Chapter 1: Product Vision & User Experience

### Introduction

AIROS Voice is a private, AI-powered voice-to-text system designed to replace third-party dictation applications while giving the user complete ownership of the backend, the data, and the future intelligence.

**Primary Objective:** Transform spoken audio into text with the fastest and most seamless experience possible.

### Product Philosophy

> Voice should become another keyboard.

The application must never interrupt the user's workflow. Instead of opening an application, the application comes to the user. Everything must happen naturally.

### Design Principles

1. **Speed over decoration** — Minimal animations, no unnecessary screens, no waiting pages
2. **One tap** — Recording begins immediately after pressing the AIROS bubble
3. **Invisible workflow** — User remains inside the application they are currently using
4. **Everything is automatically saved** — Every successful transcription becomes part of history
5. **Simple interface** — Avoid unnecessary buttons and complicated menus

### Target Users

Version 1 is optimized for personal use. Future versions may support public users.

### Success Criteria

- Display the AIROS bubble when appropriate
- Start recording with a single tap
- Convert speech into text using the backend
- Insert returned text into the current text field
- Save every transcript automatically
- Display transcript history
- Allow Copy and Delete from history
- Operate quickly and reliably during everyday use

---

## Chapter 2: Android Client Blueprint

### Components

**Component 1: Floating Voice Bubble**
- Starting recording
- Stopping recording
- Sending audio
- Returning text

**Component 2: AIROS Application**
- Viewing transcript history
- Copying transcripts
- Deleting transcripts
- Settings

**Component 3: Background Service**
- Monitor editable text fields
- Control the floating bubble
- Manage microphone sessions
- Communicate with backend

### Bubble Behavior

The bubble is context-aware and appears only when:
- An editable text field receives focus
- The user is preparing to type

The bubble disappears when:
- The text field loses focus
- The keyboard is dismissed
- The user leaves text-entry mode

### Bubble States

1. **Hidden** — No active text field
2. **Ready** — Text field focused, waiting for input
3. **Recording** — Microphone is active
4. **Processing** — Audio sent, waiting for response
5. **Completed** — Text successfully inserted
6. **Error** — Transcription failed or connection issue

### History Screen

Display every completed transcription with:
- Date
- Time
- Transcript

Supported actions:
- Copy
- Delete

### Settings Screen

Essential options only:
- Backend URL
- Connection status
- Microphone permission status
- Overlay permission status
- Accessibility permission status
- Application version
- Privacy information

### Android Permissions Required

- Microphone access
- Display over other apps (if required for bubble)
- Accessibility Service (to detect fields and insert text)

---

## Chapter 3: Backend Communication Blueprint

### Communication Model

Communication is request-response.

Flow:
1. Android records audio
2. User taps Done
3. Recording stops
4. Audio is uploaded
5. Backend processes audio
6. Backend returns text
7. Android inserts text
8. Transcript is saved to history

### API Responsibility

The backend is responsible for:
- Receiving audio
- Validating requests
- Speech recognition
- Text formatting
- Returning transcript
- Saving transcript history (optional)

### Android Responsibility

The Android client is responsible for:
- Capturing microphone input
- Uploading audio
- Waiting for response
- Inserting returned text
- Updating local history

### Response Handling

**On Success:**
- Return transcript
- Android inserts text
- Transcript added to history

**On Failure:**
- Return error message
- Android displays notification
- No text inserted

### Network Failures

If backend unreachable:
- Preserve recorded audio temporarily
- Notify user
- Allow retry

---

## Chapter 4: System Architecture

### High-Level Architecture

```
User Speaks
    ↓
Android App
    ↓
HTTPS Request
    ↓
AIROS Backend (Render)
    ↓
Speech-to-Text Engine
    ↓
Formatted Text
    ↓
Android App
    ↓
Insert into Active Text Field
```

### Repository Organization

```
AIROS-Voice/
├── android/
├── backend/
├── docs/
├── assets/
├── README.md
├── LICENSE
└── .gitignore
```

### Android Project Structure

```
android/
├── app/
├── ui/
├── services/
├── network/
├── database/
├── models/
├── repository/
├── permissions/
├── navigation/
├── utils/
└── build.gradle
```

### Backend Project Structure

```
backend/
├── api/
├── transcriber/
├── services/
├── models/
├── database/
├── utils/
├── config/
├── requirements.txt
└── main.py
```

### Module Independence

Each module should evolve independently. Android UI changes should not require backend changes. Backend AI improvements should not require Android redesign.

---

## Chapter 5: Development Roadmap & Execution Strategy

### Development Principles

1. Build one feature at a time
2. Keep commits small and focused
3. Test each feature immediately after implementation
4. Do not begin a new milestone until previous is stable
5. Prioritize reliability over adding new features
6. Keep codebase modular and maintainable

### Milestones

1. **Milestone 1** — Project Foundation
2. **Milestone 2** — Android Foundation
3. **Milestone 3** — Bubble & Recording
4. **Milestone 4** — Backend Integration
5. **Milestone 5** — Text Insertion
6. **Milestone 6** — History
7. **Milestone 7** — Stability
8. **Milestone 8** — Release

### Git Workflow

- Create feature branch for each milestone
- Commit logical changes
- Merge only after testing
- Keep main branch stable

### Version 1 Completion Criteria

- Launch successfully
- Detect supported text-entry contexts
- Present AIROS bubble according to approved behavior
- Record audio
- Send audio to backend
- Receive transcript
- Insert transcript into active text field
- Save transcript history
- Display history
- Copy transcripts
- Delete transcripts
- Operate reliably throughout normal use

### Intentionally Excluded from Version 1

- AI chat
- Translation
- Grammar correction
- Text rewriting
- Transcript editing
- OCR
- Screen analysis
- Voice commands
- Cloud synchronization
- Multi-device support
- User authentication

---

## Non-Negotiable Rules

1. Follow the approved blueprint exactly
2. Do not introduce features outside Version 1
3. Do not simplify architecture without approval
4. Keep codebase modular and scalable
5. Keep Android client lightweight
6. Keep backend logic on the server
7. Every engineering decision must support future expansion

---

**End of AIROS Voice Master Blueprint v1.0**

This document is the single source of truth for all AIROS Voice development.
