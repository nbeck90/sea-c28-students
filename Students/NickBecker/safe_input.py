def safe_input(prompt):
    try:
        input = raw_input(prompt)
    except EOFError:
        print "EOFError, try again"
        return None
    except KeyboardInterrupt:
        print "You interrupted with your keyboard, sorry."
        return None
    return input
