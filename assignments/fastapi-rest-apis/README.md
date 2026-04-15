# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework. In this assignment, you will learn how to define endpoints, validate request data, and return structured JSON responses for common API operations.

## 📝 Tasks

### 🛠️ Build the API Foundation

#### Description
Set up a FastAPI app for a simple resource (for example, books, tasks, or products). Create clear route paths and response formats so users can retrieve data from your API.

#### Requirements
Completed program should:

- Create a FastAPI application in a Python file
- Include at least one GET endpoint that returns a list of items
- Include at least one GET endpoint that returns a single item by ID
- Return JSON responses with consistent field names


### 🛠️ Implement Create, Update, and Delete Operations

#### Description
Add write operations to your API and validate incoming request data. Your API should handle creating new items, updating existing ones, and deleting records.

#### Requirements
Completed program should:

- Include a POST endpoint to create a new item
- Include a PUT or PATCH endpoint to update an existing item
- Include a DELETE endpoint to remove an item by ID
- Use Pydantic models for request validation
- Return appropriate success or error messages with HTTP status codes
