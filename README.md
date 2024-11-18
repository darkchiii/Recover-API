# Recover-API

A RESTful API designed for managing user posts, comments, collections, and interactions. It provides endpoints for user authentication, post and comment management, and building collections with CRUD operations.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Testing](#testing)

## Features

Recover-API enables users to:

### 1. User Authentication
- **Registration**: Users can create a new account by providing basic information such as email, username, and password. Secure password hashing ensures data protection.
- **Login**: Users can log in securely using their credentials (email and password). Authentication tokens are provided upon successful login, which can be used for accessing protected endpoints.
  
#### **Post Management**
- **Create Posts**: Users can create new posts containing text, audio, image, and video files. They can add titles and descriptions to their posts. 
- **Update Posts**: Users can edit their existing posts to update the content, title, or media.
- **Delete Posts**: Users can delete their posts whenever needed. 
- **View Posts**: Users can view posts created by themselves and others, including media files such as images, videos, and audio.

#### **Comment System**
- **Add Comments**: Users can comment on posts to provide feedback or engage in discussions.
- **Update Comments**: Users can edit their comments to update the content, such as correcting errors or adding more information.
- **Delete Comments**: Users can delete their comments at any time.
- **Like Comments**: Users can like comments made by others, enabling them to express appreciation or agreement.
- **Reply to Comments**: Users can reply to specific comments, creating a threaded conversation within posts.

#### **Collections**
- **Create Collections**: Users can create personalized collections to organize their posts. These collections can be named.
- **Manage Collections**: Users can edit their collection details, such as name and privacy settings.
- **Add Posts to Collections**: Users can add posts to their collections for easy access and organization. This feature allows users to create thematic groupings of posts.
- **View Collections**: Users can view all their created collections and the posts within each collection.
- **Delete Collections**: Users can remove collections, which deletes the collection but does not delete the posts within them.

#### **QA System**
- **Ask Questions**: Users can ask questions to other users in a Q&A format. This allows for community-driven knowledge sharing.
- **Answer Questions**: Users can provide answers to questions asked by others, contributing to discussions and sharing knowledge.


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

Below is a comprehensive list of API endpoints, grouped by functionality with a description of each.

### Authentication

- **`POST /api/user/create/`**  
  Create a new user account.  
  **Request Body**: { "name": "username", "email": "user@example.com", "password": "password" }  
  **Response**: Returns details of the newly created user.
  
- **`GET /api/user/token/`**  
  Obtain a token for authentication.  
  **Request Body**: { "email": "user@example.com", "password": "password" }  
  **Response**: Returns an authentication token.

- **`GET /api/user/me/`**  
  Get details of the authenticated user.  
  **Response**: Returns user information.
  
- **`GET /api/user/users/`** 
  Get a list of all users.  
  **Response**: Returns a list of all created profiles. 

### Post Endpoints

- **`GET /api/post/`**  
  Retrieve a list of posts.  
  **Response**: Returns a list of post data.

- **`POST /api/post/`**  
  Create a new post. Post supports several types of files; the user can add text, photo, video or audio file. One post can contain one file type.
In the body request if a user wants to add a photo his sample request should look like this: { "images_file": path, "description": "file_description", "public": false }. Public field is set to true by default.

Depending on the type of file, the name of the field where the user adds the file path can look like this:
Audio file - **Request Body**: `{ “audio_file”: path, etc. }`, supports file extensions: .mp3, .wav
Images file - **Request Body**: `{ “images_file”: path, etc. }`, supports file extensions: .jpg, .jpeg, .png
Text file - **Request Body**: `{ “text_file”: "text", etc. }`
Video file - **Request Body**: `{ “video_file”: path, etc. }`, supports file extensions: mp4, .avi, .mov
The api contains functions that validate added files.

**Request Body**: { "images_file": "path", "description": "file_description", "public": true }  
**Response**: Returns details of the newly created post.
 
- **`GET /api/posts/:userId/`**  
  Retrieve posts created by a specific user if they are public.  
  Response: Returns a list of the user's public posts.

- **`GET /api/post/:postId/`**  
  Retrieve details of a specific post by ID.  
  Response: Returns the post data. 

- **`DELETE /api/post/:postId/`**  
  Delete a specific post by ID.  
  Response: Confirms the deletion of the post. 

- **`PATCH /api/post/:postId/`**  
  Update a specific post by ID.  
  Request Body: { "description": "file_description", "public": true  }  
  Response: Returns the updated post details.


### Comment Endpoints

- **`GET /api/post/:postId/comments/`**  
  Retrieve a list of comments for a specific post by `postId`.  
  **Response**: Returns a list of comments associated with the specified post. 

- **`POST /api/post/:postId/comments/`**  
  Create a new comment for a specific post by `postId`.  
  **Request Body**: `{ "parent_comment": "parent_comment_id", "content": "content" }`  
  The `parent_comment` is optional. If the user wants to reply to a comment, the "parent_comment_id" will be added to the request, otherwise the user will create a standalone comment under the post.
  **Response**: Returns details of the newly created comment.
  
- **`GET /api/comment/:commentId/`**  
  Retrieve details of a specific comment by `commentId`.  
  **Response**: Returns the comment data, including the author, content, creation date, and replies if they exist.
  
- **`PATCH /api/comment/:commentId/`**  
  Update a specific comment by `commentId`.  
  **Request Body**: `{ "content": "updated_comment_text" }`  
  **Response**: Returns the updated comment details.

- **`DELETE /api/comment/:commentId/`**  
  Delete a specific comment by `commentId`.  
  **Response**: Confirms the deletion of the comment.

- **`POST /api/like/comment/:commentId/`** LIKE DO EDYCJI 
  Like a specific comment by `commentId`. If the comment is already liked by the user, this action will unlike it.  
  **Response**: Returns the updated like status of the comment, including the total count of likes.
  
- **`DELETE /api/like/comment/:commentId/`**  
  Unlike a specific comment by `commentId`.  
  **Response**: Confirms the unliking of the comment, including the updated like count.

### Collection Endpoints

- **`GET /api/collection/`**  
  Retrieve a list of all collections of logged in user.  
  **Response**: Returns a list of collections.

- **`POST /api/collection/`**  
  Create a new collection.  
  **Request Body**: `{ "title": "collection_title", "public": true }`  
  The `public` field is set by default to `true`.  
  **Response**: Returns details of the newly created collection.

- **`GET /api/collection/user/:userId/`**  
  Retrieve public collections created by a specific user identified by `userId`.  
  **Response**: Returns a list of public collections associated with the specified user.

- **`GET /api/collection/:collectionId/`**  
  Retrieve details of a specific collection by `collectionId`.  
  **Response**: Returns the collection data, including the name, description, visibility status, and associated posts.

- **`PATCH /api/collection/:collectionId/`**  
  Update details of a specific collection by `collectionId`.  
  **Request Body**: `{ "title": "collection_title", "public": true }`
  **Response**: Returns the updated collection details.

- **`DELETE /api/collection/:collectionId/`**  
  Delete a specific collection by `collectionId`.  
  **Response**: Confirms the deletion of the collection.

- **`POST /api/collection/post/:postId/`**  
This endpoint allows a user to save a specific post to a collection. If the collection does not already exist, it will be created. The post will be added to the collection, and the post’s "saves" counter will be incremented. If a collection ID is provided, the post is added to the specified collection. Otherwise, a new collection is created for the user.  
  **Request Body**: `{ "title": "optional_title" }`  
  *If no title is provided, a new collection will be created with a default title based on the number of collections the user has.*  
  **Response**: Returns the details of the collection to which the post was added.

  This functionality supports organizing posts into collections and incrementing a post's "saves" count, making it easier for users to manage and categorize their content.


### QA Endpoints

- **`GET /ask/questions/`**  
  Retrieve the question inbox for the currently authenticated user. This returns all the questions directed to the user that have not yet been answered.  
  **Response**: Returns a list of questions directed to the authenticated user where the `answer` field is `null` (i.e., unanswered).

- **`POST /ask/:userId/`**  
  Ask a question to a specific user, identified by `userId`. This creates a new question directed to the specified user.  
  **Request Body**: `{ "content": "your_question_text" }`  
  **Response**: Confirms that the question has been successfully created and sent to the specified user.

- **`POST /answer/:questionId/`**  
  Answer a specific question, identified by `questionId`. The logged-in user provides an answer to the question posed by another user.  
  **Request Body**: `{ "content": "your_answer_text" }`  
  **Response**: Returns the details of the newly created answer, including the content and the question it addresses.

- **`GET /answers/:userId/`**  
  Retrieve a list of answers provided by a specific user, identified by `userId`. This returns all answers given by the specified user.  
  **Response**: Returns a list of answers, including the question content, the answer content, and additional metadata like the questioner and respondent names.

- **`GET /answers/:answerId/`**  
  Get details of a specific answer by `answerId`. This provides detailed information about a specific answer, including the question it addresses and the answer's content.  
  **Response**: Returns the answer data, including the question it addresses, the answer content, and the creation date.

## Testing

Run the tests with the following command:

```
python manage.py test
```
