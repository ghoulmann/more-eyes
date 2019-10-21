import os, mimetypes, datetime, textract

class DataFile():
    def __init__(self, textsource):
        self.start_process = datetime.datetime.now().timestamp()
        if os.path.isfile(textsource):
            self.submit_datetime = datetime.datetime.strftime(datetime.datetime.now(), "%m/%d/%Y, %H:%M:%S")
            self.path = textsource
            self.last_modified = datetime.datetime.strftime(datetime.datetime.fromtimestamp(os.path.getmtime(self.path)), "%m/%d/%Y, %H:%M:%S")
            
            self.mime_type = mimetypes.guess_type(self.path, strict=True)
            # filetype
            #self.filetype = filetype.guess(textsource)
            #self.file_extension = self.filetype.extension
            #self.mime_type_confirm = self.filetype.mime
            self.abspath = os.path.abspath(self.path)
            self.filename = os.path.basename(self.path)
            self.file_base = os.path.splitext(self.filename)[0]
            self.file_ext = os.path.splitext(self.filename)[1]
            self.filesize = os.path.getsize(self.path)
            # read file with Python
            #with open(textsource, "r") as f:
            #    self.content = f.read()
            # Extract Content with Textract
            self.extracted_content = textract.process(textsource, 'utf-8')
            self.content = self.extracted_content.decode('utf-8')
        else:
            self.content = textsource
        self.process_time = datetime.datetime.now().timestamp() - self.start_process #seconds
    #def process(self, self.content):
                                                                            
    #def readability(self, self.content):
    #def nlp(self, self.content):

    
