# AIROS Voice Backend API Specification

## Version 1.0 — Foundation

This document defines the communication contract between the Android client and the AIROS Voice backend.

### Base URL

Development: `http://localhost:5000`
Production: (Render deployment URL)

---

## Endpoints

### 1. Health Check

**Endpoint:** `GET /health`

**Purpose:** Verify backend is online and responsive

**Request:**
```
GET /health HTTP/1.1
```

**Response (200 OK):**
```json
{
  "status": "ok",
  "version": "1.0.0-foundation",
  "service": "AIROS Voice Backend"
}
```

---

### 2. Transcribe Audio

**Endpoint:** `POST /api/transcribe`

**Purpose:** Convert audio to text

**Request Headers:**
```
Content-Type: multipart/form-data
```

**Request Body:**
```
audio: [binary audio file]
format: [audio format, e.g., "wav", "mp3"]
language: [optional, default: "en"]
```

**Response (200 OK):**
```json
{
  "success": true,
  "transcript": "The transcribed text goes here",
  "confidence": 0.95,
  "duration": 5.2,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Response (400 Bad Request):**
```json
{
  "success": false,
  "error": "Invalid audio file"
}
```

**Response (500 Internal Server Error):**
```json
{
  "success": false,
  "error": "Speech recognition failed"
}
```

---

## Audio Specifications

- **Format:** WAV, MP3, or M4A
- **Sample Rate:** 16 kHz recommended
- **Channels:** Mono or Stereo
- **Bit Depth:** 16-bit
- **Max Size:** 25 MB
- **Max Duration:** 60 minutes (limited by API timeout)

---

## Error Handling

### Common Errors

| HTTP Status | Error | Cause |
|------------|-------|-------|
| 400 | Invalid audio file | Corrupted or unsupported format |
| 413 | Payload too large | Audio exceeds 25 MB |
| 500 | Speech recognition failed | Backend processing error |
| 503 | Service unavailable | Backend temporarily down |

### Retry Strategy

- On network failure: Retry up to 3 times with exponential backoff
- On 5xx errors: Retry after 30 seconds
- On 4xx errors: Do not retry (fix the request)

---

## Future Expansion

The API is designed to support:

- Translation of transcripts
- Grammar correction
- Text rewriting
- Custom AI processing
- Transcript history queries

These capabilities can be added as new endpoints without changing the core transcription flow.

---

## Communication Flow

```
Android Client
    ↓
Records Audio
    ↓
Compresses/Packages
    ↓
POST /api/transcribe
    ↓
AIROS Backend
    ↓
Speech Recognition
    ↓
Format Transcript
    ↓
Return JSON Response
    ↓
Android Client
    ↓
Parse Response
    ↓
Insert Text
    ↓
Save to History
```

---

**End of API Specification v1.0**
