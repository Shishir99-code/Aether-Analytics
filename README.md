# Aether Analytics Demo Web Application

A Django-based demo web application designed to showcase resume matchmaking and real-time chat functionality for an upcoming startup, **Aether Analytics**. The application allows users to upload resumes, find the best potential matches based on text similarity, and communicate in a private chat room.

---

## Features

### Resume Matchmaking
- **PDF to Text Conversion**: Extracts text from PDF resumes using `pdfminer`.
- **Text Cleaning & Preprocessing**:
  - Removes special characters, URLs, redundant spaces, and numbers.
  - Optional stemming, stopword removal, and punctuation removal.
- **Similarity Metrics**:
  - Jaccard similarity
  - TF-IDF cosine similarity
- **Matching Engine**:
  - Identifies potential matches based on job title, company, and resume similarity.
  - Sends chat room invites via email using SendGrid.

### Real-Time Chat
- Users can create or join chat rooms.
- Messages are sent and retrieved in real-time using Django views and AJAX.
- Unique room codes are generated for secure and private conversations.

### Frontend
- Built with HTML5, CSS3, and JavaScript.
- Bootstrap and Crispy Forms used for responsive design.
- AJAX and WebSockets for real-time chat updates.
