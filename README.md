# Recover-API

A RESTful API designed for managing user posts, comments, collections, and interactions. It provides endpoints for user authentication, post and comment management, and building collections with CRUD operations.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

Recover-API enables users to:

- **User Authentication**: Register, log in, and manage user accounts securely.
- **Post Management**: Create, update, delete posts, and view posts by other users. User can post text, audio and visual files.
- **Comment System**: Add, update, and delete comments on posts, as well as like comments.
- **Collections**: Create and manage personal collections and add posts to them.
- **QA System**: Ask and answer user questions with an inbox feature.

## Getting Started

### Installation

1. Clone the repository:
```bash
pit clone https://github.com/darkchiii/Recover-API.git
cd Recover-API
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Set up the database:

```
python manage.py migrate
```

4. Run the development server:

```bash
python manage.py runserver
```

## Usage

After starting the server, access the API via `http://127.0.0.1:8000/`. You can use tools like [Postman](https://www.postman.com/) to test the endpoints.

## Endpoints

### User Endpoints

- **`POST /api/user/create/`**: Create a new user account.
- **`GET /api/user/token/`**: Obtain a token for authentication.
- **`GET /api/user/me/`**: Get details of the authenticated user.
- **`GET /api/user/users/`**: Get a list of all users.

### Post Endpoints

- **`GET /api/post/`**: Create and retrieve posts.
- **`POST /api/post/`**: Create and retrieve posts.
- **`GET /api/posts/:userId/`**: Get posts by a specific user (if public).
- **`GET /api/post/:postId/`**: Delete, update, or retrieve a specific post.
- **`DELETE /api/post/:postId/`**: Delete, update, or retrieve a specific post.
- **`PATCH /api/post/:postId/`**: Delete, update, or retrieve a specific post.

### Comment Endpoints

- **`GET /api/post/:postId/comments/`**: Create and retrieve comments on posts.
- **`POST /api/post/:postId/comments/`**: Create and retrieve comments on posts.
- **`GET /api/comment/:commentId/`**: Edit or delete a specific comment.
- **`PATCH /api/comment/:commentId/`**: Edit or delete a specific comment.
- **`DELETE /api/comment/:commentId/`**: Edit or delete a specific comment.
- **`POST /api/like/comment/:commentId/`**: Like or unlike a comment.
- **`DELETE /api/like/comment/:commentId/`**: Like or unlike a comment.

### Collection Endpoints

- **`GET /api/collection/`**: Retrieve or create collections.
- **`POST /api/collection/`**: Retrieve or create collections.
- **`GET /api/collection/user/:userId/`**: Get public collections by a user.
- **`GET /api/collection/:collectionId/`**: Retrieve, update, or delete a specific collection.
- **`PATCH /api/collection/:collectionId/`**: Retrieve, update, or delete a specific collection.
- **`DELETE /api/collection/:collectionId/`**: Retrieve, update, or delete a specific collection.
- **`POST /api/collection/post/:postId/`**: Save a post to a collection.

### QA Endpoints

- **`GET /ask/questions/`**: Retrieve a user's question inbox.
- **`POST /ask/:userId/`**: Ask a question to a user.
- **`POST /answer/:questionId/`**: Answer a specific question.
- **`GET /answers/:userId/`**: Retrieve answers provided by a user.
- **`GET /answers/:answerId/`**: Get details of a specific answer.

## Testing

Run the tests with the following command:

```
python manage.py test
```
