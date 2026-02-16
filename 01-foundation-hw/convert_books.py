from markitdown import MarkItDown
import os

def convert_books_to_markdown(books_dir='books', output_dir='books_text'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    md = MarkItDown()

    for filename in os.listdir(books_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(books_dir, filename)
            md_filename = filename.replace('.pdf', '.md')
            md_path = os.path.join(output_dir, md_filename)
            
            if os.path.exists(md_path):
                print(f"Skipping {filename}, {md_filename} already exists.")
            else:
                print(f"Converting {filename} to markdown...")
                try:
                    result = md.convert(pdf_path)
                    with open(md_path, 'w', encoding='utf-8') as f:
                        f.write(result.text_content)
                    print(f"Saved {md_filename}")
                except Exception as e:
                    print(f"Failed to convert {filename}: {e}")

    # Check specifically for Think Python 2e
    think_python_md = os.path.join(output_dir, 'thinkpython2.md')
    if os.path.exists(think_python_md):
        with open(think_python_md, 'r', encoding='utf-8') as f:
            line_count = sum(1 for line in f)
        print(f"\nLine count for Think Python 2e ({think_python_md}): {line_count}")
    else:
        print("\nThink Python 2e markdown file not found.")

if __name__ == "__main__":
    convert_books_to_markdown()
