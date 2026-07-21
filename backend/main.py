"""
AIROS Voice Backend - Main Entry Point

Responsible for:
- Receiving audio from Android client
- Speech recognition processing
- Returning transcripts
- Saving transcript history (optional)
"""

import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024  # 25MB max upload
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', '/tmp/airos_uploads')

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return {
        'status': 'ok',
        'version': '1.0.0-foundation',
        'service': 'AIROS Voice Backend'
    }, 200


@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    """
    Transcribe audio endpoint
    Receives audio file, processes it, returns transcript
    """
    return {
        'status': 'placeholder',
        'message': 'Transcription endpoint - to be implemented in Milestone 4'
    }, 200


@app.errorhandler(404)
def not_found(error):
    return {'error': 'Endpoint not found'}, 404


@app.errorhandler(500)
def internal_error(error):
    logger.error(f'Internal error: {error}')
    return {'error': 'Internal server error'}, 500


if __name__ == '__main__':
    debug = os.getenv('DEBUG', 'False') == 'True'
    port = int(os.getenv('PORT', 5000))

    logger.info(f'Starting AIROS Voice Backend on port {port}')
    logger.info(f'Debug mode: {debug}')

    app.run(host='0.0.0.0', port=port, debug=debug)
