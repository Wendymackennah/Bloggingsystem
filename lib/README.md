# Blogging System CLI Python Project

This is a command-line interface (CLI) Python project for managing a simple blogging system. Users can add posts, add comments to posts, view posts, search for posts, and exit the application.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your_username/blogging-system-cli.git
```

2. Navigate to the project directory:

```bash
cd blogging-system-cli
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Database Setup

This project uses SQLite for its database. The database file is located at `lib/db/bloggingsystem.db`.

## Usage

Once installed, you can run the CLI tool via the terminal:

```bash
python main.py
```

### Main Menu Options

- **1. Add Post:** Add a new blog post.
- **2. Add Comment:** Add a comment to an existing post.
- **3. View Post:** View comments for a specific post.
- **4. Search Post:** Search for posts by title or content.
- **5. Exit:** Exit the application.

### Example Usage

#### Add Post

To add a new post, select option `1` from the main menu. You'll be prompted to enter the title and content of the post.

#### Add Comment

To add a comment to an existing post, select option `2` from the main menu. You'll be asked to enter the post ID where you want to add the comment and then provide the comment text.

#### View Post

To view comments for a specific post, select option `3` from the main menu. Enter the post ID when prompted, and it will display all comments associated with that post.

#### Search Post

To search for posts containing a specific keyword in their title or content, select option `4` from the main menu. Enter the keyword you want to search for, and it will display matching posts.

## Contributing

Contributions are welcome! If you have suggestions or want to report a bug, please open an issue on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
