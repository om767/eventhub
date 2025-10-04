# EventHub

**One Platform, Every Event, Zero Chaos**

EventHub is a comprehensive event management platform designed to streamline the planning, orchestration, and analysis of unforgettable events. With AI-assisted insights and seamless vendor collaboration, EventHub empowers organizers, vendors, attendees, and sponsors to create memorable experiences effortlessly.

## Features

- **Smart Event Builder**: Intuitive drag-and-drop interface with AI-powered suggestions for designing perfect event timelines.
- **All-in-one Dashboard**: Real-time analytics, budget tracking, and guest management in a centralized command center.
- **Seamless Vendor Management**: Connect with trusted vendors, track contracts, and manage payments effortlessly.
- **AI-Powered Insights**: Get intelligent recommendations for venues, catering, and scheduling based on event goals using Google Gemini AI.
- **Task Management**: Create, assign, update, and track tasks for event organization.
- **Event Logs**: Maintain detailed logs of all event-related actions and changes.
- **Real-time Chat**: Communicate across different channels for event coordination.
- **Multi-Role Support**: Dedicated interfaces for organizers, vendors, attendees, and sponsors.
- **Authentication & Authorization**: Secure JWT-based authentication system.
- **Responsive Design**: Modern, mobile-friendly UI with dark/light theme toggle.

## Tech Stack

### Backend
- **FastAPI**: High-performance web framework for building APIs.
- **SQLAlchemy**: ORM for database interactions.
- **MySQL**: Relational database for data persistence.
- **JWT**: JSON Web Tokens for secure authentication.
- **Google Generative AI (Gemini)**: AI-powered event planning assistance.
- **Pydantic**: Data validation and serialization.

### Frontend
- **HTML5/CSS3/JavaScript**: Static web pages served by FastAPI.
- **Responsive Design**: Mobile-first approach with CSS Grid and Flexbox.
- **Theme System**: Dark and light mode support.

## Installation

### Prerequisites
- Python 3.8+
- MySQL Server
- Git

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd eventhub
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the `backend/` directory with the following variables:
   ```
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   DATABASE_URL=mysql+mysqlconnector://username:password@localhost/eventhub
   GEMINI_API_KEY=your-gemini-api-key-here
   ```

5. **Set up the database:**
   - Create a MySQL database named `eventhub`.
   - Run the database initialization (tables are created automatically on first run).

## Usage

### Running the Application

1. **Start the backend server:**
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

2. **Alternative: Start the simple HTTP server for frontend:**
   ```bash
   python server.py
   ```
   The application will be available at `http://localhost:8080`.

### API Documentation

When running the FastAPI server, visit `http://localhost:8000/docs` for interactive API documentation powered by Swagger UI.

## API Endpoints

### Authentication
- `POST /api/auth/users/` - Create a new user
- `POST /api/auth/token` - Login and get access token

### Organizer
- `GET /api/organizer/tasks/` - Get all tasks for the event
- `POST /api/organizer/tasks/` - Create a new task
- `PUT /api/organizer/tasks/{task_id}/status` - Update task status
- `DELETE /api/organizer/tasks/{task_id}` - Delete a task
- `GET /api/organizer/logs/` - Get event logs

### Shared
- `GET /api/shared/chat/{channel}` - Get chat messages for a channel
- `POST /api/shared/chat/{channel}` - Post a message to a channel

### AI
- `POST /api/ai/generate-plan` - Generate event plan using AI

## Database Schema

The application uses the following main entities:

- **Events**: Core event information
- **Users**: System users with roles (organizer, vendor, attendee, sponsor)
- **Tasks**: Event-related tasks with status tracking
- **EventLogs**: Audit trail of event actions
- **ChatMessages**: Real-time communication messages
- **LayoutItems**: Event layout planning
- **Sponsors**: Sponsorship management
- **Leads**: Attendee-sponsor interactions
- **Interests**: User interest categories

## Project Structure

```
eventhub/
├── backend/
│   ├── main.py              # FastAPI application setup
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # Database operations
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── AuthenticationRouter.py
│   │   ├── organizer.py
│   │   ├── shared.py
│   │   └── gemini.py
│   └── requirements.txt
├── front end/
│   ├── index.html           # Landing page
│   ├── login.html           # Login page
│   ├── signup.html          # Registration page
│   ├── organizer dashboard.html
│   ├── attendee.html
│   ├── vendor.html
│   ├── sponsor.html
│   ├── spoc.html
│   ├── task.html
│   ├── budget.html
│   ├── event calender.html
│   ├── event log.html
│   ├── analytical.html
│   ├── notification panel.html
│   ├── weather forcast.html
│   ├── about.html
│   ├── faq.html
│   └── css/
│       ├── style.css
│       ├── global.css
│       └── dashboard.css
├── server.py                # Simple HTTP server

```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact the development team at support@eventhub.com.

---

**EventHub** - Making event management effortless, one event at a time.
