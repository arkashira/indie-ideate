```markdown
# tech-spec.md

## Stack
- **Language**: Python
- **Framework**: FastAPI
- **Runtime**: Docker (for containerization)

## Hosting
- **Platform**: 
  - Vercel (for frontend hosting)
  - Heroku (for backend hosting)
- **Free Tier**: 
  - Vercel offers a generous free tier for static sites and serverless functions.
  - Heroku provides a free tier for small applications with limited resources.

## Data Model
### Collections
1. **Users**
   - **user_id**: UUID (Primary Key)
   - **username**: String (Unique)
   - **email**: String (Unique)
   - **password_hash**: String
   - **created_at**: Timestamp

2. **Ideas**
   - **idea_id**: UUID (Primary Key)
   - **user_id**: UUID (Foreign Key)
   - **title**: String
   - **description**: Text
   - **status**: Enum (draft, validated, rejected)
   - **created_at**: Timestamp
   - **updated_at**: Timestamp

3. **Feedback**
   - **feedback_id**: UUID (Primary Key)
   - **idea_id**: UUID (Foreign Key)
   - **user_id**: UUID (Foreign Key)
   - **comment**: Text
   - **rating**: Integer (1-5)
   - **created_at**: Timestamp

## API Surface
1. **User Registration**
   - **Method**: POST
   - **Path**: `/api/users/register`
   - **Purpose**: Register a new user.

2. **User Login**
   - **Method**: POST
   - **Path**: `/api/users/login`
   - **Purpose**: Authenticate a user and return a JWT token.

3. **Create Idea**
   - **Method**: POST
   - **Path**: `/api/ideas`
   - **Purpose**: Create a new idea for the logged-in user.

4. **Get Ideas**
   - **Method**: GET
   - **Path**: `/api/ideas`
   - **Purpose**: Retrieve all ideas for the logged-in user.

5. **Update Idea**
   - **Method**: PUT
   - **Path**: `/api/ideas/{idea_id}`
   - **Purpose**: Update an existing idea.

6. **Delete Idea**
   - **Method**: DELETE
   - **Path**: `/api/ideas/{idea_id}`
   - **Purpose**: Delete an existing idea.

7. **Submit Feedback**
   - **Method**: POST
   - **Path**: `/api/feedback`
   - **Purpose**: Submit feedback for an idea.

8. **Get Feedback**
   - **Method**: GET
   - **Path**: `/api/feedback/{idea_id}`
   - **Purpose**: Retrieve all feedback for a specific idea.

## Security Model
- **Authentication**: JWT (JSON Web Tokens) for user sessions.
- **Secrets Management**: Use environment variables to store sensitive information (e.g., database credentials, API keys).
- **IAM**: Role-based access control (RBAC) to manage permissions for different user roles (e.g., admin, user).

## Observability
- **Logs**: Use structured logging with Loguru for application logs.
- **Metrics**: Integrate Prometheus for monitoring key metrics (e.g., request counts, response times).
- **Traces**: Use OpenTelemetry for distributed tracing to monitor performance and troubleshoot issues.

## Build/CI
- **CI/CD Tool**: GitHub Actions for continuous integration and deployment.
- **Build Steps**:
  1. Linting with Flake8.
  2. Running unit tests with pytest.
  3. Building Docker images.
  4. Deploying to Heroku and Vercel on successful builds.
```
