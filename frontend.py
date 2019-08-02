def create_frontend_html_file(factorial_url: str):
    return """
        <!DOCTYPE html>
        <html lang="en">
        <body>
        <div>
            <input type="text" id="factorial">Factorial: Enter a non-negative number</input>
            <button onclick="httpGet(1)">Send Request</button>
        </div<br><br>
        
        <h4>Solution:</h4>
        <div id="output"></div>
        
        <script>
            var output = document.getElementById('output');
        
            function httpGet(func_call) {{
                let xmlHttp = new XMLHttpRequest();
                if (func_call === 1) {{
                    xmlHttp.open("GET", "{factorial_url}" + document.getElementById("factorial").value, false);
                }}
                xmlHttp.send(null);
                let returnValue = xmlHttp.responseText;
                output.innerHTML = returnValue;
            }}
        </script>
        
        </body>
        </html>
    """.format(factorial_url=factorial_url)
