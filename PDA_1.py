# This is the PDA driver file

class PDA():
    states[5] = {"p", "q", "q_a", "q_b", "q_"}
    rules[8] = {"(p, e, e) -> (q, S)", "(q_a, e, S) -> (q_a, aSb)",
                "(q_b, e, S) -> (q_b, e)", "(q, a, e) -> (q_a, e)",
				"(q_a, e, a) -> (q, e)", "(q, b, e) -> (q_b, e)",
                "(q_b, e, b) -> (q, e)", "(q, $, e) -> (q_$, e)" }
    header =  "Step" + "State" + "String" + "Stack" + "Rule used"
    def delta(stack, str, state, step):
        r = 0
        if step == 0:
            r= -1
        elif state == 0:
            state = 1
            stack += "S"
            r = 1
        elif state == 1:
            if str[0] == 'a':
                state = 2
                str = str[1:]
                r = 4
            elif str[0] == 'b':
                state = 3
                str = str[1:]
                r = 6
            elif str[0] == '$':
                state = 4
                str = str[1:]
                r = 8
        elif state == 2:
            if stack[0] == 'a':
                state = 1
                stack = stack[1:]
                r = 5
            elif stack[0] == 'S':
                stack = stack[1:]
                stack = "aSb" + stack
                r = 3
	elif state == 3:
		if stack[0] == 'b':
			stack = stack[1:]
			state = 1
			r = 7
		elif stack[0] == 'S':
			stack = stack[1:]
			r = 2
		print(stack, str, state, step, r)
        #This will be built out tomorrow
    def init(stack, str, state):
        #not quite sure what this does....
        return foo
    def process(var):
        print header
        stack = ""
        str = ""
        if(len(var) > 2):
            str.extend(var)
        else:
            str = var
        str += "$"
        state = 0
        step = 0
        while(state != 4):
            delta(stack, str, state, step)
            step += 1
        print "Finshed"
        if(len(stack) == 0 && len(str) == 0):
            print "The String is parsable"

