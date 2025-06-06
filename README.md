# 🕵️ Security Footage Recovery from PCAP

> **TryHackMe Challenge: Digital Forensics – "Security Footage"**  
> Goal: Recover surveillance footage by reconstructing JPEG images from packet capture data and combining them into a playable video.

---

## 📁 Project Description

This project demonstrates how to recover lost or deleted surveillance footage using network forensics. Given a `.pcap` file containing Motion JPEG (MJPEG) video stream data, we extract raw image frames embedded in the packet payload and reconstruct the original video.

The workflow consists of two main steps:
1. **Extract JPEG images** from the PCAP file using pattern-matching on JPEG file signatures in the raw packet data.
2. **Rebuild the video** by stitching the JPEGs into a playable AVI format using OpenCV.

---

## 🧪 Requirements

- Python 3.6+
- `opencv-python`
- Wireshark or tshark 

Install dependencies:
```bash
pip install opencv-python
```

## 📹 Output
- Extracted images: frame_0000.jpg, frame_0001.jpg, ...
- Final recovered video: retrieved.avi

The video can be played using VLC, Windows Media Player, or any player that supports .avi.

📦 Repository Structure
```
.
├── security-footage-1648933966395.pcap
├── extractFromPcap.py        # JPEG extractor
├── toVideo.py                # Video builder
├── frame_0000.jpg            # Extracted frames
├── retrieved.avi             # Final video
└── README.md
```

🧠 Forensics Insights
- JPEG signatures (FFD8 ... FFD9) are recoverable from raw packet data.
- MJPEG streams over HTTP often include full-frame images.
- PCAPs can be utilised for file carving if disk forensics isn't an option.
