# Ticket Booking Website for Hockey and Boxing Matches

## Overview
This project is a Flask-based web application for reserving tickets for hockey and boxing matches. The website is in French and includes user registration with email verification, login, event listing, and booking functionalities.

## Project Structure
- `app/`: Main application package
  - `models/`: Database models (User, Event, Booking)
  - `routes/`: Flask route blueprints (auth, events, bookings)
  - `utils/`: Utility modules for authentication and security
  - `templates/`: HTML templates (to be added)
  - `static/`: Static files like CSS, JS, images (to be added)
- `migrations/`: Database migrations (if using Flask-Migrate)
- `config.py`: Configuration settings
- `run.py`: Application entry point

## Setup Instructions
1. Create and activate a Python virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/macOS
   ```
2. Install dependencies:
   ```
   pip install flask flask_sqlalchemy flask_bcrypt flask_jwt_extended
   ```
3. Run the application:
   ```
   python run.py
   ```
4. Access the website at `http://localhost:5000`

## GitHub Upload
1. Initialize git repository:
   ```
   git init
   git add .
   git commit -m "Initial commit"
   ```
2. Create a new repository on GitHub.
3. Add remote and push:
   ```
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

## Next Steps
- Implement frontend templates using Jinja2 based on existing HTML files.
- Connect frontend with backend APIs.
- Add email sending for verification codes.
- Enhance security and validation.

## License
MIT License
