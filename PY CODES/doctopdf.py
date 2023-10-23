import os
import win32com.client as win32

def convert_to_pdf(input_path, output_path):
    # Create an instance of the Word application
    word = win32.gencache.EnsureDispatch('Word.Application')
    try:
        # Open the input Word file
        doc = word.Documents.Open("F:\AAI\Sale Deed-  dr Soumyan dey bhagawati ghansoli.docx")
        
        # Save the file as PDF
        doc.SaveAs(output_path, FileFormat=17)  # FileFormat=17 represents PDF format
        
        # Close the document and quit Word
        doc.Close()
        word.Quit()
        
        print(f"Conversion complete. PDF file saved at: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = '"F:\AAI\Sale Deed-  dr Soumyan dey bhagawati ghansoli.docx"'   # Replace with your input Word file path
output_file = '"F:\AAI\New folder"'  # Replace with your desired output PDF file path

convert_to_pdf(input_file, output_file)
