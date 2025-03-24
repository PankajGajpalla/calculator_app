# import numpy as np

# # Video parameters
# width, height = 320, 240
# frames = 30  # Number of frames

# # Generate random pixel values (grayscale for simplicity)
# video_data = np.random.randint(0, 256, (frames, height, width), dtype=np.uint8)

# # Save as a binary file
# with open("video.raw", "wb") as f:
#     f.write(video_data.tobytes())

# print("Binary video file 'video.raw' created.")







# import numpy as np

# # Video parameters
# width, height, frames = 320, 240, 30  # 30 frames
# video_data = np.linspace(0, 255, width * height * frames, dtype=np.uint8)  # Smooth transition
# video_data.tofile("gradient.raw")  # Save as raw binary




import numpy as np
import cv2
import os as os

# Video parameters
width, height, frames = 320, 240, 30  # 30 frames at 320x240 resolution

# Create a directory to save frames
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

for i in range(frames):
    # Generate a frame with a simple pattern (gradient + circle animation)
    img = np.zeros((height, width), dtype=np.uint8)
    cv2.circle(img, (50 + i * 5, 120), 30, 255, -1)  # Moving white circle
    cv2.imwrite(f"{output_dir}/frame_{i:03d}.png", img)

    # Save raw binary data
    img.tofile(f"{output_dir}/frame_{i:03d}.raw")

print("Frames saved successfully!")
