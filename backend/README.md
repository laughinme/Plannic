# Plannic API

FastAPI backend for the Plannic application. This API provides endpoints for managing users and tasks, with notification capabilities to the Telegram bot.

## Project Structure

The API follows a three-layer architecture:

- **Routers**: Handle HTTP requests and responses
- **Services**: Implement business logic
- **Repositories**: Manage database operations

### Main Components

- `app/routers`: API endpoints for users and tasks
- `app/services`: Business logic implementation
- `app/repositories`: Database access layer
- `app/models`: SQLAlchemy ORM models
- `app/schemas`: Pydantic schemas for validation
- `app/core`: Core functionality like security
- `app/notification`: Services for sending notifications to the bot
- `app/utils`: Utility functions and helpers
- `app/config`: Application configuration
- `app/db`: Database connection and session management

## Setup and Run

1. Create and activate a virtual environment
2. Install dependencies:
   ```
   poetry install --only api
   ```
3. Create `.env` file with environment variables:
   ```
   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///./app.db
   BOT_WEBHOOK_URL=http://bot:8000/webhook
   ```
4. Run the application:
   ```
   cd api
   uvicorn app.main:app --reload
   ```

## API Documentation

Once running, API documentation is available at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Integration with Bot

The API can send notifications to the Telegram bot through webhooks. Events like task creation and updates trigger notifications. 