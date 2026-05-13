# Football Teams Backend

## Project Overview
The Football Teams Backend is a RESTful API designed to manage amateur football teams. It provides the core infrastructure for an application, allowing users to create accounts, manage player profiles, form or join football teams, and track achievements.

## Architecture
This project is structured using a Domain-Driven Design (DDD) approach. The codebase is organized into discrete bounded contexts (such as `accounts`, `player`, `team`, and `achievement`) to separate business logic from the web framework layer, ensuring long-term maintainability.

## Tech Stack
- Django 5.0 & Django REST Framework
- PostgreSQL
- JWT Authentication
- Docker
- pytest

## API Endpoints

All endpoints except registration and login require a valid JWT Bearer token in the Authorization header.

### Accounts (`/api/auth/`)
| Method | Endpoint | Request Body | Response |
|--------|----------|--------------|----------|
| POST | `/login/` | `email`, `password` | 200: `access`, `refresh` tokens |
| POST | `/refresh/` | `refresh` | 200: `access` token |
| POST | `/register/` | `email`, `password` | 200: User data |
| POST | `/logout/` | `refresh` | 204: No Content |

### Player (`/api/player/`)
| Method | Endpoint | Request Body | Response |
|--------|----------|--------------|----------|
| GET | `/me/` | None | 200: Player details |
| PATCH | `/nick/` | `new_nickname` | 200: Updated player details |

### Team (`/api/team/`)
| Method | Endpoint | Request Body | Response |
|--------|----------|--------------|----------|
| POST | `/team-create/` | `team_name`, `team_nickname`, `team_slogan`, `team_city`, `team_country` | 201: Team details |
| GET | `/team-details/` | `team_name` | 200: Team information |
| POST | `/team-join-request/` | `team_name` | 200: Success message |
| GET | `/team-join-request-list/` | `team_name` | 200: Pending requests |
| POST | `/team-accept-join-request/` | `player_request_name`, `team_name` | 200: Success message |
| POST | `/team-leave/` | `team_name` | 200: Success message |
| DELETE | `/team-delete/` | `team_name` | 200: Success message |
| POST | `/team-follow/` | `team_name` | 200: Follow status |
| POST | `/team-unfollow/` | `team_name` | 200: Unfollow status |

### Achievement (`/api/achievement/`)
| Method | Endpoint | Request Body | Response |
|--------|----------|--------------|----------|
| POST | `/achievement-acquired/` | None | 200: Achievement details |

---
**Note:** For the full interactive OpenAPI documentation, run the application and navigate to `/api/schema/`.
