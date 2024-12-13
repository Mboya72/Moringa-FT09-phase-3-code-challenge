# Magazine Management System
This is a simple console-based application for managing authors, magazines, and articles. 
The system allows users to input data for authors, magazines, and articles, store the information 
in a database, and retrieve it for display.

## Features
  **Create Authors:** Add new authors to the database.
  **Create Magazines:** Add magazines with categories to the database.
  **Create Articles:** Write articles that are linked to both authors and magazines.
  **Display Data:** Retrieve and display all authors, magazines, and articles from the database.

## Requirements
Python 3.x
SQLite database
Database schema with tables: authors, magazines, articles

## Setup
## **Install Dependencies:**
  Ensure you have Python 3.x installed.
  Install any required dependencies (e.g., SQLite).
  If using an external package manager, create a requirements.txt for your packages.

## **Database Setup:**
  The database and tables are automatically created when the script runs using create_tables() from the database.setup module.
  Tables include:
    **authors:** Stores author details.
    **magazines:** Stores magazine names and categories.
    **articles:** Stores article details, linked to authors and magazines.

## Usage
  **Run the application:**
    To start the application, execute the script:
      python main.py
  **Interactive Input:**
    The program will prompt you to enter details for an author, a magazine, and an article.
  ### Example input:

    Enter author's name: John Doe
    Enter magazine name: Tech Weekly
    Enter magazine category: Technology
    Enter article title: The Future of AI
    Enter article content: AI is transforming industries...

  ### **Database Operations:**

Authors: The Author.create() method is used to add a new author to the database.
Magazines: The Magazine.create() method is used to add a new magazine with a category.
Articles: The Article.create() method is used to add an article linked to the created author and magazine.
Viewing Data:

After data is inserted, the application queries the database for all authors, magazines, 
and articles and displays them on the console.

  ### Example Output
   After running the program and entering sample data, the output will look like this:

  Enter author's name: John Doe
  Enter magazine name: Tech Weekly
  Enter magazine category: Technology
  Enter article title: The Future of AI
  Enter article content: AI is transforming industries...
  Magazines:
  <Magazine Tech Weekly (Technology)>
  Authors:
  <Author John Doe>
  Articles:
  <Article The Future of AI>

## License
This project is open-source and available under the MIT License.

