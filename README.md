# API Portfolio

<h3>Student Profile</h3>
Full Name: Ivan P. Duran <br>
Section: BSIT - 4E <br>
Year Standing: 3rd Year Irregular
<hr>

<h3>Contents</h3>
<ul>
  <li>Laboratory 1: Factorial Calculator API</li> 
  <li>Laboratory 2: Basic Task Management System<</li>
  <li>Laboratory 3: Enhanced Task Management with Error Handling</li>
  <li>Laboratory 4: Secure and Versioned Task Management API</li>
  <li>Laboratory 5: Deployed API Links</li>
  <li>Key Takeways</li>
</ul>
<hr>
    
<h4>Laboratory 1: Factorial Calculator API</h4>

In this laboratory, I created a simple FastAPI application to manage tasks using different HTTP methods (GET, POST, PUT, DELETE). This activity served as a foundation to understand how APIs work and how to structure them. By working with FastAPI, I learned how to define routes for various operations such as fetching tasks, adding new ones, updating them, and deleting them. I also understood the importance of data validation and how APIs interact with data and return results in JSON format. This lab was a key step in building a strong foundation in API development, preparing me for more complex applications in the future.
<hr>

<h4>Laboratory 2: Basic Task Management System</h4>

In this laboratory, I created a Task Management API using FastAPI, which allowed me to learn the basic structure of an API and how it functions. I designed a Task model with attributes like task_id, task_title, task_desc, and is_finished. Using Pydantic for validation, I created a simple in-memory database (task_db) to store tasks.

The API supports four main operations:

GET: Retrieve a task by ID.
POST: Add a new task with validation checks for ID uniqueness and required fields.
PUT: Update an existing task’s title, description, or status, with validation to ensure meaningful changes.
DELETE: Remove a task by ID.

This laboratory helped me grasp how APIs handle CRUD operations and served as a foundation for understanding FastAPI's structure and request handling.
<hr>

<h4>Laboratory 3: Enhanced Task Management with Error Handling</h4>
In this activity, I worked with an external API to fetch and manipulate data. I learned how to retrieve data from APIs, process it using Python, and return the results in a valid JSON format. The goal was to create an API that combines multiple external APIs, formats the data as required, and returns it to the user.

For example, I created endpoints that return posts and comments from a placeholder API, format them based on specific criteria (like user ID), and combine them in meaningful ways. One of the tasks was to create a detailed post API that shows all posts of a user along with comments for each post.

By doing this, I gained experience with:
1. Fetching and manipulating data from external APIs
2. Formatting and returning data in JSON format
3. Combining different API calls into a single API

This exercise helped me understand how to work with data from multiple sources and create an API that returns comprehensive and structured information to the user.
<hr>

<h4>Laboratory 4: Secure and Versioned Task Management API</h4>

In this laboratory, I created an API that manages tasks using FastAPI. The main goals of this lab were to implement a simple CRUD (Create, Read, Update, Delete) system with the addition of API versioning and API key authentication.

I first created a basic API to manage tasks with endpoints for creating, reading, updating, and deleting tasks. The API accepts and returns JSON data using FastAPI’s built-in features. I also implemented API versioning by separating the routes into two versions: apiv1 and apiv2. In version 1, the responses are simple, while in version 2, I added more validation and authentication using API keys.

In version 2 of the API, I required a valid API key to access the routes, enhancing the security of the API. The key is checked via a custom api_key_check function, which ensures that the requests contain a valid API key in the header.

This laboratory helped me better understand API development, versioning, and security practices. It also reinforced the importance of validation and error handling in creating robust APIs.
<hr>

<h4>Laboratory 5: Deployed API Links</h4>
<ul>
  <li>Laboratory 1: https://itec116-duran-factorial.onrender.com/docs</li>
  <li>Laboratory 2: https://itec116-duran-basic-task-management.onrender.com/docs</li>
  <li>Laboratory 3: https://itec116-duran-tm-with-error-handling.onrender.com/docs</li>
  <li>Laboratory 4: https://itec116-duran.onrender.com</li>
</ul>
<hr>

<h3>Key Takeways</h3>
Through the laboratories, I gained valuable knowledge and skills in designing and developing APIs using FastAPI. These sessions provided hands-on experience with various concepts, allowing me to build a strong foundation in API development, error handling, security, and best practices.

1. I learned the fundamentals of APIs, including their structure and how they work, which enabled me to design endpoints aligned with specific functionalities.

2. The implementation of CRUD operations taught me how to manage data efficiently within an application. Input validation techniques were also applied to maintain data integrity and prevent errors.

3. Error handling was emphasized, where I learned to provide meaningful error messages and utilize FastAPI’s HTTPException for structured exception handling.

4. API versioning was introduced to manage backward compatibility effectively. I created separate endpoints for each version, such as /apiv1 and /apiv2, ensuring seamless updates for different clients.

5. Security measures, such as API key authentication, were implemented to restrict unauthorized access. I gained experience in validating authorization headers and securely managing sensitive data.

6. FastAPI’s dependency injection features were explored, particularly using Depends to simplify authentication and validation processes. This approach improved code reusability and maintainability.

7. I integrated .env files and environment variables to securely manage sensitive information like API keys, enhancing the security and scalability of the applications.

8. Debugging and testing practices were strengthened by identifying and resolving issues in API logic and response structures, boosting my confidence in developing robust APIs.

These takeaways highlight my progression in mastering API development, ensuring scalability, security, and efficiency in real-world scenarios.

