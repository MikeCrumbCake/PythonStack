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

