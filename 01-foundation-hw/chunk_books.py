from gitsource import chunk_documents
from pathlib import Path

def get_chunks(book_filename):
    """
    Reads a markdown book, chunks it, and returns the list of chunks.
    This function handles paths correctly whether run from the script location
    or imported from a notebook.
    """
    # Determine directory where this script is located
    base_dir = Path(__file__).resolve().parent
    
    # Construct absolute path to the book file
    book_path = base_dir / "books_text" / book_filename
    
    if not book_path.exists():
        # Fallback: check current directory if relative imports are tricky
        # This handles cases where __file__ might be misleading or empty
        candidate = Path("books_text") / book_filename
        if candidate.exists():
            book_path = candidate.resolve()
        else:
            raise FileNotFoundError(f"Book file not found at: {book_path} or {candidate}")
    
    # Read content
    with open(book_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Split into lines and filter empty/whitespace lines
    lines = [line for line in content.splitlines() if line.strip()]
    
    # Create document dictionary
    document = {
        "source": str(book_path),
        "content": lines
    }
    
    # Chunk the document
    chunks = chunk_documents([document], size=100, step=50)
    
    return chunks
