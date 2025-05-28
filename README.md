# secure-video-generator_2.0
A secure web app to generate a downloadable video using image + text (and audio later), with OpenCV and Flask.

```
🧰 Final Tech Stack
🔙 Backend:
Python 3.x
Flask – API & routing
OpenCV – generate video from image and text
FFmpeg – merge audio with video (later)
subprocess – for FFmpeg command execution
SSL/TLS (OpenSSL) – simulate secure HTTPS (self-signed)

🌐 Frontend:
HTML5 – form to upload image + text (+ audio later)
Tailwind CSS (optional) – minimal styling
JavaScript – form handling and file download logic

🧪 Dev Tools:
Git + GitHub – version control and hosting
.gitignore – exclude certs/, env/, __pycache__, etc.
requirements.txt – for dependency management
```

🗂️ Folder Structure
```
secure-video-generator/
├── app.py
├── static/
│   └── style.css  ← optional (for Tailwind/custom styling)
├── templates/
│   └── index.html
├── uploads/
│   └── (uploaded files go here)
├── certs/          ← self-signed SSL certs (excluded from Git)
├── generated_videos/
│   └── (output videos)
├── .gitignore
├── README.md
├── requirements.txt
└── summary.pdf     ← your final reflection & notes
```