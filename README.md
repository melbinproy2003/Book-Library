# Book Library

A comprehensive web application for managing and exploring a collection of books.

## Features

- **Search and Browse**: Easily search and browse through a wide collection of books.
- **User Authentication**: Secure login and registration for users.
- **Book Details**: Detailed information about each book, including cover images and descriptions.
- **Admin Panel**: Admin interface for managing the book collection and user information.

## Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/melbinproy2003/Book-Library.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Book-Library
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Visit `http://127.0.0.1:8000/` in your browser.
- Register or log in to access all features.
- Search for books and view detailed information.

## Project Structure

- `bookapp/`: Main application directory.
- `media/`: Directory for media files such as book covers.
- `templates/`: HTML templates for the web application.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django's command-line utility for administrative tasks.
- `.idea/`: IDE configuration files.
  
## License

This project is licensed under the MIT License.

## Contact

For any inquiries or issues, please contact [melbinproy2003](https://github.com/melbinproy2003).

---

Feel free to customize this template further based on specific project needs.
