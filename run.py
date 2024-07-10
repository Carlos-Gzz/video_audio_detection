import sys
import os

# Add the 'video_audio_detection' directory to the Python path
project_root = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'video_audio_detection')
sys.path.append(project_root)

# Print the PYTHONPATH and directory contents for debugging
print("PYTHONPATH:", sys.path)
print("Directory Contents:", os.listdir(project_root))

from app import app

if __name__ == "__main__":
    app.run(debug=True)
