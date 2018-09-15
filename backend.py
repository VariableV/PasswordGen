# author: Maheen Hussain
from flask import Flask, render_template, request, jsonify
from itertools import zip_longest
import string

web = Flask(__name__)

symbol_map = "!@#$%^&*()"
def gen_pw(website):
	website = ''.join(filter(lambda c : c in set(string.ascii_letters), website))
	website = website.lower()
	strlen = len(website)
	# swap letters in groups of two
	swap = ""
	for i in range(0, strlen, 2):
		swap += website[i:i+2][::-1]
	# reverse string
	swap = swap[::-1]
	# get numerical representation of number
	# shift each number by string length
	# multiply by strlen/2
	nums = []
	for i in range(0, strlen):
		num_rep = ord(swap[i:i+1]) - ord('a')
		shifted = (num_rep + strlen)%26
		shifted *= strlen//2
		nums.append(chr(shifted%26 + ord('a')))
	website = ''.join(nums)
	# capitalize last and first characters
	website = website[0:1].upper() + website[1:strlen-1] + website[strlen-1:].upper()
	# add symbols
	final = ""
	stuff =  strlen//2
	for a,b in zip_longest(website[::2], website[1::2], fillvalue=""):
		if (len(b)==0):
			break
		symbol = symbol_map[ord(b)%9]
		final += a + symbol + b
	if (strlen % 2 != 0):
		final += website[strlen-1:]
	return final

@web.route("/")
def index_html():
	return render_template("index.html")

@web.route("/genpw", methods=["POST"])
def pwreq():
	website_name = request.form["webname"]
	return jsonify({"retn":gen_pw(website_name)})

if (__name__ == "__main__"):
	web.run()