#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# First file editing:
# 24-09-2016 23h33:00 (UTC+1)
#
# Copyright (c) 2016, Samuel Prevost <samuel.prevost@gmx.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of CanoniPy nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Import modules for CGI handling
import cgi, cgitb
from cmath import *

print "Content-type:text/html\r\n\r\n"

print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>CanoniPy V2.0 - Par Samuel Prevost</title>"
print "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css\">"
print "<style> .bigger { font-size: 2em; } input { width: 50px;} .smaller { font-size: 0.6em;} .top{border-bottom:solid black 1px; display:inline-block; float:left; text-align: center;} .bottom{ display:inline-block; clear:left; float:left; text-align: center;} body { padding-left: 30px; }</style>"
print "<script type=\"text/javascript\" async src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML\"></script>"
print "</head>"
print "<body>"
print "<h2> CanoniPy V3.0 - Par Samuel Prevost </h2>"
print "<h3>Algorithme de résolution de polynômes du second degré</h3>"
print "<h4>Avantages:</h4>"
print "<ul>"
print "<li>Très rapide</li>"
print "<li>Supporte aussi bien les nombres réels que les nombres complexes</li>"
print "<li>Permet de tester la concordance de la forme canonique et développée</li>"
print "<li>Testé et fiable</li>"
print "<li>Simple d'utilisation</li>"
print "</ul></br><hr>"

print "</br>"
print "<h2>Entrez le polynôme à tester :</h2>"
print "<form method=\"GET\"><h1><input name=\"a\" value=\"2\">`x^2+`<input name=\"b\" value=\"9\">`x+`<input name=\"c\" value=\"1\"></h2>"
print "</br><button type=\"submit\">Inspecter</button></form></br>"
print "<hr>"

try:
    # Create instance of FieldStorage
    form = cgi.FieldStorage()

    # Get data from fields

    a = complex(form.getvalue('a'))
    b = complex(form.getvalue('b'))
    c = complex(form.getvalue('c'))
except:
    print "<h4>a, b et c sont les coefficients du polynôme du second degré de forme</h4>"
    print "<i>ax&sup2; + bx + c </i></br>"
    print "<p>Les nombres complexes sont notés a + bj avec j&sup2; = -1 et (a,b) € |R</p>"
    print "<hr>"
    print "<center><i class=\"text-muted smaller\">Écrit à 1h du mat, un dimanche matin/samedi soir, à moitié saoul</i></center>"
    print "</body>"
    print "</html>"
    exit()


if a.imag == 0 and b.imag == 0 and c.imag == 0:
    a = a.real
    b = b.real
    c = c.real

print "<h2>Propriétés de `{}x^2+{}x+{} = 0`</h2>".format(a, b, c)

print "<ul>"
delta = pow(b, 2) - (4 * a * c)
print "<li> <span class=\"bigger\">`\\Delta = {}{:+}j`</span></li>".format(delta.real, delta.imag)

alpha = -1 * (b / (2 * a))
print "<li> <span class=\"bigger\">`\\alpha = {}{:+}j`</span></li>".format(alpha.real, alpha.imag)

beta = -1 * (delta / (4 * a))
print "<li> <span class=\"bigger\">`\\beta = {}{:+}j`</span></li>".format(beta.real, beta.imag)

if alpha.imag == 0 and beta.imag == 0 and delta.imag == 0:
    alpha = alpha.real
    beta = beta.real
    delta = delta.real

r1 = (-b-sqrt(delta))/(2*a)
r2 = (-b+sqrt(delta))/(2*a)

if(delta.real >= 0 and a.imag == 0 and b.imag == 0 and c.imag == 0):
    canonique = "`{}(x {:+})^2 {:+}`".format(a, -alpha, beta)
    print "<li><h3>Forme canonique :</h3> <span class=\"bigger\">{}</span></li></br></br>".format(canonique)
    print "<li><h3>Racine 1 : </h3><span class=\"bigger\">`x_1 = (-{}-sqrt({}))/(2*{})={} `</span></li></br></br>".format(b, delta, a, r1.real)
    print "<li><h3>Racine 2 : </h3><span class=\"bigger\">`x_2 = (-{}+sqrt({}))/(2*{})={} `</span></li></br></br>".format(b, delta, a, r2.real)
    print "<li><h3>Forme factorisée :</h3> <span class=\"bigger\">`{}(x {:+})(x {:+})`</span></li></br></br>".format(a, -r1.real, -r2.real)
else:
    if a.imag == 0:
        a = a.real
    if b.imag == 0:
        b = b.real
    if c.imag == 0:
        c = c.real

    canonique = "`{}(x {:+}{:+}j)^2 {:+}{:+}j`".format(a, -alpha.real, alpha.imag, beta.real, beta.imag)
    print "<li><h3>Forme canonique :</h3> <span class=\"bigger\">{}</span></li></br></br>".format(canonique)
    print "<center style=\"font-size: 2.0em;\">Avec `j^2 = -1`</center>"
    print "<li><h3>Racine complexe 1 : </h3><span class=\"bigger\">`x_1 = (-{}-sqrt({}))/(2*{})={} `</span></li></br></br>".format(b, delta, a, r1)
    print "<li><h3>Racine complexe 2 : </h3><span class=\"bigger\">`x_2 = (-{}+sqrt({}))/(2*{})={} `</span></li></br></br>".format(b, delta, a, r2)
    print "<li><h3>Forme factorisée :</h3> <span class=\"bigger\">`{}(x {:+}{:+}j)(x {:+}{:+}j)`</span></li></br></br>".format(a, -r1.real, r1.imag, -r2.real, r2.imag)

print "</ul>"
print "</br>"
print "</br><hr>"
print "<center><a href=\"http://sa.muel.coffee\"><i class=\"text-muted\">Coded &amp; Designer by Samuel Prevost &copy; 2015 - 2017</i></a></center>"
print "</body>"
print "</html>"
