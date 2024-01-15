import sys

try:
    if len(sys.argv) == 2:

        # Read entry time
        with open(sys.argv[1], "rt") as file:
            
            time_1 = []
            
            for line in file:
                lines = line.split(",")
                time_1.append(lines)
                    
            time_1.pop(-1)
            
            entry_time = []
            
            for i in time_1:
                entry_time.append(int(i[1]))
            
        # Read exit time
        with open(sys.argv[1], "rt") as file:
            
            time_2 = []
            
            for line in file:
                lines = line.split(",")
                time_2.append(lines)
                    
            time_2.pop(-1)
            
            exit_time = []
            
            for i in time_2:
                exit_time.append(int(i[2]))
            
        # Read cat ownership
        with open(sys.argv[1], "rt") as file:
            
            cat_own = []
            
            for line in file:
                lines = line.split(",")
                cat_own.append(lines)
                    
            cat_own.pop(-1)
            
            owner = []
            
            for i in cat_own:
                owner.append(i[0])
            
        # Time difference
        time_diff = []

        for i in range(len(exit_time)):
            time_diff.append(exit_time[i] - entry_time[i])

        #Count no of entries

        intruder = 0
        ours = 0
        
        for i, l in enumerate(time_diff):
            if l == 1 and owner[i] == "THEIRS":
                intruder += 1
            
            if owner[i] == "OURS":
                ours += 1
                
        print()
        print("Log File Analysis")
        print("=================")
        print()
                
        print(f"Cat visits: {ours}")
        print(f"Other Cats: {intruder}")
        print()

        # Time the cat was inside

        time_stayed = 0

        for i in range(len(time_diff)):
            if owner[i] == "OURS":
                time_stayed += time_diff[i]
                
        hrs = time_stayed // 60
        mins = time_stayed % 60
                
        print(f"Total Time in House: {hrs} hours {mins} minutes\n" if time_stayed % 60 != 0 else f"Total Time in House: {hrs} hours\n")

        # Longest and shortest time:

        longest = max(time_diff)
        
        l1 = longest // 60
        l2 = longest % 60

        time_diff_1 = time_diff[:]

        for i, j in enumerate(time_diff):
            if owner[i] == "THEIRS":
                time_diff_1[i] = 1441
                
        shortest = min(time_diff_1)
        
        s1 = shortest // 60
        s2 = shortest % 60

        # Average time:

        total = 0
        count = 0

        for i in time_diff_1:
            if i != 1441:
                total += i
                count += 1

        avg = total // count
        
        a1 = avg // 60
        a2 = avg % 60

        print(f"Longest visit: {longest} minutes" if longest < 60 else f"Longest visit: {l1} hours {l2} minutes")
        print(f"Shortest visit: {shortest} minutes" if shortest < 60 else f"Shortest visit: {s1} hours {s2} minutes")
        print(f"Average visit: {avg} minutes" if avg < 60 else f"Average visit: {a1} hours {a2} minutes")
        
    elif len(sys.argv) == 1:
        print("\nNo arguments provided, please send a value!\n")
    
    else:
        print("\nToo many arguments!\n")
    
except FileNotFoundError:
    print("\nThat file doesn't exist, Enter a valid file name\n")
    