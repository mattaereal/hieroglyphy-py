#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Copyright (c) <2012> <Matías Ariel Ré Medina>
# Hieroglyphy, port from JavasCript version by <Patricio Palladino>
# alcuadrado@github ~ mattaereal@github

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import sys

class Hieroglyphy:
    def __init__(self):
        """
        Here we define our alphabet.
        """
        #self.numbers = [
        #            "+[]",
        #            "+!![]",
        #            "!+[]+!![]",
        #            "!+[]+!![]+!![]",
        #            "!+[]+!![]+!![]+!![]",
        #            "!+[]+!![]+!![]+!![]+!![]",
        #            "!+[]+!![]+!![]+!![]+!![]+!![]",
        #            "!+[]+!![]+!![]+!![]+!![]+!![]+!![]",
        #            "!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]",
        #            "!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]"
        #]

        self.numbers = [
                    "+[]",
                    "-~[]",
                    "-~-~[]",
                    "-~-~-~[]",
                    "-~-~-~-~[]",
                    "-~-~-~-~-~[]",
                    "-~-~-~-~-~-~[]",
                    "-~-~-~-~-~-~-~[]",
                    "-~-~-~-~-~-~-~-~[]",
                    "-~-~-~-~-~-~-~-~-~[]"
        ]

        
        self.characters = {
                    "0" : "(" + self.numbers[0] + "+[])",
                    "1" : "(" + self.numbers[1] + "+[])",
                    "2" : "(" + self.numbers[2] + "+[])",
                    "3" : "(" + self.numbers[3] + "+[])",
                    "4" : "(" + self.numbers[4] + "+[])",
                    "5" : "(" + self.numbers[5] + "+[])",
                    "6" : "(" + self.numbers[6] + "+[])",
                    "7" : "(" + self.numbers[7] + "+[])",
                    "8" : "(" + self.numbers[8] + "+[])",
                    "9" : "(" + self.numbers[9] + "+[])"
        }

        self._object_Object = "{}+[]"
        self._NaN = "+{}+[]"
        self._true = "!![]+[]"
        self._false = "![]+[]"
        self._undefined = "[][+[]]+[]"

        self.characters[" "] = "(" + self._object_Object + ")[" + \
                                self.numbers[7]  + "]"
        self.characters["["] = "(" + self._object_Object + ")[" + \
                                self.numbers[0]  + "]"
        self.characters["]"] = "(" + self._object_Object + ")[" + \
                                self.characters["1"] + "+" + \
                                self.characters["4"] + "]"
        self.characters["a"] = "(" + self._NaN + ")[" + self.numbers[1] + "]"
        self.characters["b"] = "(" + self._object_Object + ")[" + \
                                self.numbers[2] + "]"
        self.characters["c"] = "(" + self._object_Object + ")[" + \
                                self.numbers[5] + "]"
        self.characters["d"] = "(" + self._undefined + ")[" + self.numbers[2] \
                                + "]"
        self.characters["e"] = "(" + self._undefined + ")[" + self.numbers[3] \
                                + "]"
        self.characters["f"] = "(" + self._undefined + ")[" + self.numbers[4] \
                                + "]"
        self.characters["i"] = "(" + self._undefined + ")[" + self.numbers[5] \
                                + "]"
        self.characters["j"] = "(" + self._object_Object + ")[" + \
                                self.numbers[3] + "]"
        self.characters["l"] = "(" + self._false + ")[" + self.numbers[2] + "]"
        self.characters["n"] = "(" + self._undefined + ")[" + self.numbers[1] \
                                + "]"
        self.characters["o"] = "(" + self._object_Object + ")[" + \
                                self.numbers[1] + "]"
        self.characters["r"] = "(" + self._true + ")[" + self.numbers[1] + "]"
        self.characters["s"] = "(" + self._false + ")[" + self.numbers[3] + "]"
        self.characters["t"] = "(" + self._true + ")[" + self.numbers[0] + "]"
        self.characters["u"] = "(" + self._undefined + ")[" + self.numbers[0] \
                                + "]"
        self.characters["N"] = "(" + self._NaN + ")[" + self.numbers[0] + "]"
        self.characters["O"] = "(" + self._object_Object + ")[" + \
                                self.numbers[8] + "]"

        self._Infinity = "+(" + self.numbers[1] + "+" + self.characters["e"] \
                        + "+" + self.characters["1"] + "+" + \
                        self.characters["0"] + "+" + self.characters["0"] \
                        + "+" + self.characters["0"] + ")+[]"

        self.characters["y"] = "(" + self._Infinity + ")[" + self.numbers[7] \
                                + "]"
        self.characters["I"] = "(" + self._Infinity + ")[" + self.numbers[0] \
                                + "]"

        self._1e100 = "+(" + self.numbers[1] + "+" + self.characters["e"] \
                        + "+" + self.characters["1"] + "+" + \
                        self.characters["0"] + "+" + self.characters["0"] \
                        + ")+[]"

        self.characters["+"] = "(" + self._1e100 + ")[" + self.numbers[2] + "]"

        self.functionConstructor = "[][" + self.hieroglyphyString("sort") \
                                    + "][" + \
                                    self.hieroglyphyString("constructor") + "]"

        ##Below self.characters need target http(s) pages
        self.locationString = "[]+" + self.hieroglyphyScript("return location")
        self.characters["h"] = "(" + self.locationString + ")" + "[" + \
                                self.numbers[0] + "]"
        self.characters["p"] = "(" + self.locationString + ")" + "[" + \
                                self.numbers[3] + "]"
        self.characters["/"] = "(" + self.locationString + ")" + "[" + \
                                self.numbers[6] + "]"

        self.unescape = self.hieroglyphyScript("return unescape")
        self.escape = self.hieroglyphyScript("return escape")
        

        self.characters["%"] = self.escape + "(" + self.hieroglyphyString("[") \
                                + ")[" + self.numbers[0] + "]"


    def getHexaString (self, number, digits):
        """
        Transforms a number into hex, and returns it casted to string.
        """

        string = str(hex(number)[2:])
        while (len(string) < digits):
            string = "0" + string
        return string

    def getUnescapeSequence (self, charCode):
        """
        Returns a charcode as its unescape sequence.
        """
        return self.unescape + "(" + \
            self.hieroglyphyString("%" + self.getHexaString(charCode, 2)) + ")"

    def getHexaSequence (self, charCode):
        """
        Returns a charcode as its hexadecimal sequence.
        """
        return self.hieroglyphyString("\\x" + self.getHexaString(charCode, 2))

    def getUnicodeSequence (self, charCode):
        """
        Returns a charcode as its unicode sequence.
        """
        return self.hieroglyphyString("\\u" + self.getHexaString(charCode, 4))


    def hieroglyphyString (self, string):
        """
        Returns a hieroglyphied string.
        """
        hieroglyphiedStr = ""

        for char in string:
            if hieroglyphiedStr != "":
                hieroglyphiedStr += "+"

            hieroglyphiedStr += self.hieroglyphyCharacter(unicode(char))

        return hieroglyphiedStr


    def hieroglyphyCharacter (self, char):
        """
        Returns a hieroglyphied single character.
        """

        if (char in self.characters):
            return self.characters[char]

        charCode = ord(char)

        if ((char == "\\") or (char == "x")):
            ##These chars must be handled appart becuase the others need them
            self.characters[char] = self.getUnescapeSequence(charCode)
            return self.characters[char]
        
        shortestSequence = self.getUnicodeSequence(charCode)

        ##ASCII self.characters can be obtained with hexa and unscape sequences
        if (charCode < 128):
            unescapeSequence = self.getUnescapeSequence(charCode)
            if (len(shortestSequence) > len(unescapeSequence)):
                shortestSequence = unescapeSequence

            hexaSequence = self.getHexaSequence(charCode)
            if (len(shortestSequence) > len(hexaSequence)):
                shortestSequence = hexaSequence

        self.characters[char] = shortestSequence

        return shortestSequence

    def hieroglyphyNumber (self, n):
        """
        Returns a hieroglyphied number as a number.
        """
        if (n <= 9): 
            return self.numbers[n]

        return "+(" + self.hieroglyphyString(str(n)) + ")"


    def hieroglyphyScript (self, src):
        """
        Returns a hieroglyphied script.
        """
        return self.functionConstructor + "("  + self.hieroglyphyString(src) \
                + ")()"



if __name__ == "__main__":
    sys.stderr.write("# Copyright (c) <2012> <Matías Ariel Ré Medina>\n")
    sys.stderr.write("# Hieroglyphy, port from JavasCript version by ")
    sys.stderr.write("<Patricio Palladino>\n")
    
    hy = Hieroglyphy()

    if len(sys.argv) == 3:
        if 'script' == sys.argv[1]:
            try:
                f = open(sys.argv[2])
            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
            else:
                js = f.read();f.close()
                sys.stderr.write("[*] Encoded script below: " + sys.argv[2] + "\n")
                print hy.hieroglyphyScript(js.strip())

        elif 'number' == sys.argv[1]:
            sys.stderr.write("[*] Encoded number below: " + sys.argv[2] + "\n")
            print hy.hieroglyphyNumber(sys.argv[2])

        elif 'string' == sys.argv[1]:
            sys.stderr.write("[*] Encoded string below: " + sys.argv[2] + "\n")
            print hy.hieroglyphyString(sys.argv[2])

        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "[!] Usage: %s script <File>|number <Number>|string <String>" % sys.argv[0]
        print "[!] Examples:"
        print "\t %s script file.js" % sys.argv[0]
        print "\t %s string \"alert('xss')\"" % sys.argv[0]
        print "\t %s number 1337" % sys.argv[0]
        sys.exit(2)
