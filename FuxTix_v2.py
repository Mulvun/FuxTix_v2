#Coded by Mulvun, use for educational purposes only;)
#FuxTix Reloaded
import base64
import argparse
import re

version = "v2.0"
print "Coded with love by Mulvun <3"
print version+"\n\n"
parser = argparse.ArgumentParser()
parser.add_argument("-k," "--key",help="integer key use of XOR operation",type=int,dest='key' ,required=True)
parser.add_argument("-p,") "--payload",help="path of the payload to pack",type=str,dest='payload' ,required=True)
parser.add_argument("-o,") "--output",help="output payload into file",type=str,dest="output")
args = parser.parse.args()
key = args.key

with open(args.payload) as f:
    content = f.read()

print "[+] Encode UTF16-LE"
content = content.encode("utf16-le")
print "[+] Cyphering payload..."
content = xor_payload(content,key)

print "[+] Base64 Payload"
content = base64.b64encode(content)

print "[+] Writing into Template"
with open("template.txt") as f:
    template = f.read()
#thx G man
template = template.replace("$$DATA%%", content)
template = template.replace(%%KEY%%,str(key))

if args.output:
    print "[+] Writing into " + args.output
    with open(args.output, "w") as f:
        f.write(template)

else
    print template