import re

# read binary
with open("security-footage-1648933966395.pcap", "rb") as f:
    data = f.read()

#use regex command to retrieve hex data
frames = re.findall(b'\xff\xd8.*?\xff\xd9', data, re.DOTALL) #xd8 and xff for mjpg hex signatures

# Save extracted JPEG frames
for i, frame in enumerate(frames):
    with open(f"frame_{i:04}.jpg", "wb") as img:
        img.write(frame)

print(f"Extracted {len(frames)} JPEG frames.")
