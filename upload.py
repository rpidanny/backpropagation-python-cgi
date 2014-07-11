#!C:\Python27\python.exe

import cgi, os
import cgitb; cgitb.enable()

try: 
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) 
    msvcrt.setmode (1, os.O_BINARY)
except ImportError:
    pass
	
form = cgi.FieldStorage()

fileitem = form['filename']


if fileitem.filename:
   fn = os.path.basename(fileitem.filename)
   open(fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'
   
print """\
Content-Type: text/html\n
<html>
<head>
<title>Result</title>
<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
   <h2>%s</h2>
   <br>
   <br>
   <a href="/ai/train.py">Train The System with the new dataset...</a>
</body>
</html>
""" % (message,)
