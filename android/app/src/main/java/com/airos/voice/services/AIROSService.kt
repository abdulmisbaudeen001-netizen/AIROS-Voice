package com.airos.voice.services

import android.app.Service
import android.content.Intent
import android.os.IBinder

/**
 * AIROSService: Background service responsible for:
 * - Monitoring editable text fields
 * - Controlling the floating bubble
 * - Managing microphone sessions
 * - Communicating with backend
 *
 * This service runs in the background to enable system-wide dictation.
 */
class AIROSService : Service() {

    override fun onBind(intent: Intent?): IBinder? {
        return null
    }

    override fun onCreate() {
        super.onCreate()
        // Initialize service
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        return START_STICKY
    }

    override fun onDestroy() {
        super.onDestroy()
        // Clean up resources
    }
}
