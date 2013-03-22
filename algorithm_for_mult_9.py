#! /usr/bin/env python

# This was discovered by me and my wife during our anniversary dinner.
# Talk about true nerds.  Thankfully my wife is willing to put up with
# my weirdness.

def main():

    # Algorithm for multiplying by 9
    # num_a = (num - tens) * 10
    # goal = num_a - ones

    print
    print """This is an algorithm that will multiply any number by 9.  This action is completed without using the multiply function but rather completes everything manually."""
    print

    # Get list of variables

    print "We will have 3 different variables in this algorithm:"

    print "1. The number given"
    raw_input()

    print "2. The tens place of the number.  This is found by dividing the number given by 10 and truncating the decimal."
    raw_input()

    print "3. The ones place.  This is simply the ones place digit."
    raw_input()

    # Perform the function

    num = input("Number to multiply by 9: ") # the given number
    tens = num / 10 # the tens place digit forward
    ones = num % 10 # the ones place digit

    # Step 1
    print
    print "Step 1"
    while True:
        print "Take the number given (%i) and minus the tens digit (%i) from it." % (num, tens)
        num_a = num - tens
        ans = input("Answer: ")
        if ans != num_a:
            print
            print "That was incorrect."
            print
            continue
        else:
            break
    
    # Step 2
    print
    print "Step 2"
    while True:
        print "Multiply that number (%i) by 10." % (num_a)
        num_b = num_a * 10
        ans = input("Answer: ")
        if ans != num_b:
            print
            print "That was incorrect."
            print
            continue
        else:
            break

    # Step 3
    print
    print "Step 3"
    while True:
        print "Minus the ones place digit (%i) from that answer (%i)." % (ones, num_b)
        goal = num_b - ones
        ans = input("Answer: ")
        if ans != goal:
            print
            print "That was incorrect."
            print
            continue
        else:
            break

    print
    print "You now have the solution."
    print
    print "%i * 9 = %i" % (num, goal)
    print

if __name__=="__main__":
	main()
