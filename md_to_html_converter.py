import markdown
import os

def convert_md_to_html(input_file, output_file):
    # Read the Markdown file
    with open(input_file, 'r', encoding='utf-8') as md_file:
        md_text = md_file.read()

    # Convert Markdown to HTML
    html_text = markdown.markdown(md_text)

    # Write the HTML output to a file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_text)

    print(f"Converted '{input_file}' to '{output_file}' successfully.")

if __name__ == "__main__":
    # Input Markdown file
    input_file = input("Enter the path to the .md file: ")

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print("The specified file does not exist. Please check the path and try again.")
    else:
        # Define the output HTML file name
        output_file = os.path.splitext(input_file)[0] + '.html'

        # Convert the Markdown file to HTML
        convert_md_to_html(input_file, output_file)