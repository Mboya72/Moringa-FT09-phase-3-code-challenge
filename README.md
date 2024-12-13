# Magazine Management System
This is a simple console-based application for managing authors, magazines, and articles. <br/>
The system allows users to input data for authors, magazines, and articles, store the information<br/> 
in a database, and retrieve it for display.

## Features
  **Create Authors:** Add new authors to the database.<br/>
  **Create Magazines:** Add magazines with categories to the database.<br/>
  **Create Articles:** Write articles that are linked to both authors and magazines.<br/>
  **Display Data:** Retrieve and display all authors, magazines, and articles from the database.<br/>

## Requirements
Python 3.x<br/>
SQLite database<br/>
Database schema with tables: authors, magazines, articles<br/>

## Setup
## **Install Dependencies:**
  Ensure you have Python 3.x installed.<br/>
  Install any required dependencies (e.g., SQLite).<br/>
  If using an external package manager, create a requirements.txt for your packages.<br/>

## **Database Setup:**
  The database and tables are automatically created when the script runs using create_tables() from the database.setup module.<br/>
  Tables include:<br/>
    **authors:** Stores author details.<br/>
    **magazines:** Stores magazine names and categories.<br/>
    **articles:** Stores article details, linked to authors and magazines.<br/>

## Usage
  **Run the application:**<br/>
    To start the application, execute the script:<br/>
      ```python main.py```<br/>
  **Interactive Input:**<br/>
    The program will prompt you to enter details for an author, a magazine, and an article.<br/>
  ### Example input:

    Enter author's name: John Doe
    Enter magazine name: Tech Weekly
    Enter magazine category: Technology
    Enter article title: The Future of AI
    Enter article content: AI is transforming industries...

  ### **Database Operations:**

**Authors:** The Author.create() method is used to add a new author to the database.<br/>
**Magazines:** The Magazine.create() method is used to add a new magazine with a category.<br/>
**Articles:** The Article.create() method is used to add an article linked to the created author and magazine.<br/>
**Viewing Data:** After data is inserted, the application queries the database for all authors, magazines, <br/>
and articles and displays them on the console.

  ### Example Output
   After running the program and entering sample data, the output will look like this:
```
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
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

