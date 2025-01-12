# Knowledge Base Backend

This is the backend server for the Knowledge Base system, built with Flask and SQLAlchemy.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Copy `.env.example` to `.env` and update the values:
```
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=mysql+pymysql://username:password@localhost/knowledge_base
SECRET_KEY=your-secret-key-here
UPLOAD_FOLDER=uploads
```

5. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Run the server:
```bash
flask run --port=3001
```

## API Endpoints

### Knowledge Items

- `GET /api/knowledge` - Get all knowledge items (supports pagination and search)
- `GET /api/knowledge/<id>` - Get a specific knowledge item
- `POST /api/knowledge` - Create a new knowledge item
- `PUT /api/knowledge/<id>` - Update a knowledge item
- `DELETE /api/knowledge/<id>` - Delete a knowledge item
- `GET /api/knowledge/search?q=keyword` - Search knowledge items

### File Upload

- `POST /api/upload` - Upload an image file

## Development

To run the server in development mode:
```bash
flask run --debug --port=3001
```
