# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assignment 4: Programming Exercise 1 (Extract Even and Odd Numbers)


# read numbers file
with open("numbers.txt") as my_file:
    # for each line
     for i in my_file:
        # parse integers
         if i.strip:
            num = int(i)
            # extract even integers
            if (num % 2 == 0):
                # append even file
                even = open("even.txt", "a")
                even.write(str(num))
            # extract odd integers
             
                # append odd text file