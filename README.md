# Hieroglyphy

A tool for converting strings, numbers, and scripts to equivalent sequences of
()[]{}+! characters that run in the browser.

## Usage and installation

You can use the class inside the python file or use it as a stand-alone script.

    [matt@mfsec hieroglyph.py]$ ./hieroglyphy.py 
    # Copyright (c) <2012> <Matías Ariel Ré Medina>
    # Hieroglyphy, port from JavasCript version by <Patricio Palladino>
    [!] Usage: ./hieroglyphy.py script <File>|number <Number>|string <String>
    [!] Examples:
    	 ./hieroglyphy.py script file.js
    	 ./hieroglyphy.py string "alert('xss')"
    	 ./hieroglyphy.py number 1337

    [matt@mfsec hieroglyph.py]$ ./hieroglyphy.py string alert
    # Copyright (c) <2012> <Matías Ariel Ré Medina>
    # Hieroglyphy, port from JavasCript version by <Patricio Palladino>
    [*] Encoded string below: alert
    (+{}+[])[+!![]]+(![]+[])[!+[]+!![]]+([][+[]]+[])[!+[]+!![]+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]]

#### If you liked this check out
    [pyronbee](http://github.com/mattaereal/pyronbee) and learn how to use the
    encodings to detect how good are your WAF rules.
