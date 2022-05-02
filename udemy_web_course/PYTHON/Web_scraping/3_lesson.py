from cgitb import html
from importlib.resources import contents
from bs4 import BeautifulSoup
html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style type="text/css">

        h1 {
            color: white;
            background: red;
        }

        li {
            color: red;
        }
        #css-li {
            color: blue;
        }
        .green {
            color: green;
        }

    </style>
</head>
<body>

    <h1>HTML</h1>
    <h1 class="green">Web</h1>
    <h3>Programming</h3>

    <ol>
        <li>HTML</li>
        <li id="css-li">CSS</li>
        <li class="green bold">JavaScript</li>
        <li class="green id" id="python-li">Python</li>
    </ol>
    
</body>
</html>
"""

parsed_html = BeautifulSoup(html_string, 'html.parser')
# data = parsed_html.body.contents[1].next_sibling.next_sibling


#data = parsed_html.find(id="css-li").parent.previous_sibling.previous_sibling

data = parsed_html.find(id="css-li").next_sibling
print(data)
