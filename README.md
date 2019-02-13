# Advanced-Optical-Character-Recognizer
# (Document-to-Text-and-Speech)

### Make a shallow clone of the repository in system's local environment.
> git clone https://github.com/harshitsaini/Document-to-Text-and-Speech.git --depth 1

### Install the packaged repository in system's local/virtual environment using setup.py present in the root directory of the cloned repository. This command installs a library named doc2speech.
> python3 setup.py install

### Python code below is an example of how the doc2speech library works.

```python
import doc2speech

# Driver function
if __name__ == '__main__':
  
  # Path of the folder where document image is present
  doc_path    = "/path/to/documentImage/"
  
  # Name of the document image to be converted
  docName     = 'doc.png'
  
  # Path of the folder where output has to be generated
  output_path = "/path/to/output/"
   
  doc2speech.performConversion(doc_path    = doc_path,
                               docName     = docName,
                               output_path = output_path)
```
