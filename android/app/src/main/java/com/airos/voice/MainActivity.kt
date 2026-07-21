package com.airos.voice

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.airos.voice.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Foundation setup
        initializeUI()
    }

    private fun initializeUI() {
        // Placeholder for UI initialization
    }
}
