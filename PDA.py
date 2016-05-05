#include <iostream>
#include <vector>
#include <stdlib.h>
using namespace std

def pad(self, str, width, bool):
def expand(self, str):
class PDAprivate:
    string states[5] = {"p", "q", "q_a", "q_b", "q_$"
	                string rules[8] = {"(p, e, e) . (q, S)", "(q_a, e, S) . (q_a, aSb)", "(q_b, e, S) . (q_b, e)", "(q, a, e) . (q_a, e)", 
					   "(q_a, e, a) . (q, e)", "(q, b, e) . (q_b, e)", "(q_b, e, b) . (q, e)", "(q, $, e) . (q_$, e)"
	                                   header = pad("Step", 6, True) + pad("State", 8, True) + pad("String", 30, True) + pad("Stack", 30, True) +
					   pad("Rule used", 10, True)
	                                   void delta(string &stack, &str, &state, step)
	                                   void init(string &stack, &str, &state)
	                                   void print(string stack, str, state, step, r)

public:
	                                   PDA(); #set first two lines of table in constructor 
	void process(string var)


PDA.PDA() {
def process(self, var):	cout << header << endl
    stack = ""
    str = ""
	if var.size() > 2) str = expand(var:
	                                str = var
	                                str += "$"
	                                state = 0
	                                step = 0
	while(state != 4)		delta(stack, str, state, step)
		                        step++

	cout << "finished" << endl
	if(stack.size() == 0 and str.size() == 0) cout << "The string is parsable" << endl



void PDA.print(string stack, str, state, step, r) { 
    tbr = ""; 
	if(stack.size() == 0) stack = "e"
	if(str.size() == 0) str = "e"
    tbr += pad(to_string(step), 6, True)
    tbr += pad(states[state], 8, True)
    tbr += pad(str, 30, True)
    tbr += pad(stack, 30, True)
	if r > 0)tbr += pad(to_string(r) + ": " + rules[r-1], 10, True:
	else  tbr += pad("-", 10, True)
	                    cout << tbr << endl;

def delta(self, &stack, &str, &state, step):	int r; 
	if(step == 0) r = -1
	elif state == 0:		state = 1
		            stack += "S"
		            r = 1

	elif state == 1:		if str.front() == 'a':			state = 2
			    str.erase(str.begin())
			    r = 4

		elif(str.front() == 'b') { 
			state = 3
			str.erase(str.begin())
			r = 6

		elif str.front() == '$':			state = 4
			str.erase(str.begin())
			r = 8


	elif state == 2:		if stack.front() == 'a':			stack.erase(stack.begin())
			state = 1
			r = 5

		elif stack.front() == 'S':			stack.erase(stack.begin())
			stack = "aSb" + stack
			r = 3


	elif state == 3:		if stack.front() == 'b':			stack.erase(stack.begin())
			state = 1
			r = 7

		elif stack.front() == 'S':			stack.erase(stack.begin())
			r = 2


		print(stack, str, state, step, r)


string pad(string str, width, direction) { #string justification
	if(str.length() > width) return str
    b = " "
	if(direction) { 
		while(str.length()!=width) {str+=b;
		return str

	while(str.length()!=width) { str = b + str;
	return str

def expand(self, str):	a_str = ""
	                             b_str = ""
	                             x = atoi(&str[1])
	for(i = 0; i < x; i++) a_str+="a"; 
	                             y = atoi(&str[3])
	for(i = 0; i < x; i++) b_str += "b"
	return a_str + b_str


