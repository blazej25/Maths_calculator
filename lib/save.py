def read():
    with open('lib/memory.txt', 'r') as mem:
        record = mem.read()

    return record

def save(action, result):
    result = str(result)
    
    with open('lib/memory.txt', 'r') as mem:
        nlines = len(mem.readlines()) 

    if nlines < 10:
        with open('lib/memory.txt', 'a') as mem:
            mem.write(f'{action}: {result}\n')
            mem.close()
    else:
        with open('lib/memory.txt', 'r') as mem:
            lines = mem.readlines()

        lines.pop()
        lines.insert(0, f'{action}: {result}\n')

        with open('lib/memory.txt', 'w') as mem:
            mem.writelines(lines)

def clear():
    with open('lib/memory.txt', 'w') as mem:
        mem.writelines('')