import markdown
import os
import logging

## Introduction
class MarkdownToHTMLConverter:
    def __init__(self):  
        print("Welcome to the Markdown to HTML Converter!")
        
        # Input File Location
        self.input_file = None
        # Output Diretory Location
        self.output_location = None
        # Output File Location
        self.__output_file = None
    
    def set_input_file(self, input_file):

        self.input_file = input_file
        if not os.path.isfile(input_file):
            print("File does not exist.")
            logging.error("File does not exist.")
            exit()
        if not input_file.endswith('.md'):
            print("File is not a Markdown (.md) file.")
            logging.error("File is not a Markdown (.md) file.")
            exit()
    
    def set_output_file(self, output):
        output = output
        try:
            if os.path.isdir(output) and os.access(output, os.W_OK) and not os.path.isfile(output):
                self.output_location = output
                file_name = os.path.basename(self.input_file).replace('.md', '.html')
                self.__output_file = os.path.join(self.output_location, file_name)
            elif os.path.isdir(os.path.dirname(output)) and os.access(os.path.dirname(output), os.W_OK) and not os.path.isfile(output):
                self.__output_file = output
                self.output_location = os.path.dirname(output)
            else:
                print("Output location is not writable or does not exist.")
                logging.error("Output location is not writable or does not exist.")
                exit()
        except Exception as e:
            print(f"An error occurred while setting the output file: {e}")
            logging.error(f"An error occurred while setting the output file: {e}")
            exit()
                
    def conversion(self):

        if not self.input_file or not self.output_location:
            print("Input file or output location is not set.")
            logging.error("Input file or output location is not set.")
            exit()
        
        try:
            with open(self.input_file, 'r', encoding='utf-8') as md_file:
                md_content = md_file.read()
            print(f"Converting {self.input_file} to HTML...")
            html_content = markdown.markdown(md_content)
            
            with open(self.__output_file, 'w', encoding='utf-8') as html_file:
                html_file.write(html_content)
            
            print(f"Conversion successful! HTML file saved at: {self.__output_file}")
            logging.info(f"Conversion successful! HTML file saved at: {self.__output_file}")
        except Exception as e:
            print(f"An error occurred during conversion: {e}")
            logging.error(f"An error occurred during conversion: {e}")
            exit()




def main():
    converter = MarkdownToHTMLConverter()
    
    # Set input file
    input_file = input("Enter the path to the Markdown file: ")
    converter.set_input_file(input_file)
    
    # Set output file or directory
    output_location = input("Enter the output directory or file path: ")
    converter.set_output_file(output_location)
    
    # Perform conversion

    converter.conversion()

if __name__ == "__main__":
    main()
    
