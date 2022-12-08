class Directory:
    def __init__(self, name, parent=None):
        self.name = str(name)
        self.children = {}
        self.parent = parent
        self.files = []
        self.size = 0

    def add_child(self, child):
        self.children[child.name] = child
        child.parent = self

    def add_file(self, file):
        self.files.append(file)

    def return_smalls(self, smalls=[]): #Part 1
        if self.size<=100000:
            smalls.append(self.size)
        for child in self.children:
            self.children[child].return_smalls(smalls)
        return smalls

    def find_options(self, needed_space, options=[]): #Part 2
        if self.size>=needed_space:
            options.append(self.size)

        for child in self.children:
            self.children[child].find_options(needed_space, options)

        return options


    def bubble_size(self, size):
        print('bubble_size called on', self.name, 'with size', size)
        self.size+=size
        if self.parent:
            self.parent.bubble_size(size)

    def __repr__(self):
        return f'{self.name} with children {self.children} and size {self.size}'


def solve(lines):
    directories = {}
    sizes = []
    root = Directory('/')
    current_dir = root

    for i in range(1, len(lines)):
        if lines[i][0]=='$':
            current_dir = execute(lines, i, root, current_dir)

    needed_space = 30000000-(70000000-root.size)
    return min(root.find_options(needed_space))



def execute(lines, i, root, current_dir):
    if lines[i][2:4]=='cd':
        if lines[i][5:]=='..':
            current_dir = current_dir.parent
        elif lines[i][5:]=='/':
            current_dir = root
        else:
            current_dir = current_dir.children[lines[i][5:]]

    elif lines[i][2:4]=='ls':
        while i+1 < len(lines) and lines[i+1][0]!='$':
            if lines[i+1][:3]=='dir':
                if lines[i+1][4:] not in current_dir.children.keys():
                    child = Directory(lines[i+1][4:], current_dir)
                    current_dir.add_child(child)

            else:
                file = lines[i+1].split(' ')
                current_dir.bubble_size(int(file[0]))
            i+=1
    
    return current_dir
            



def main():
    text = open('day7input.txt', 'r')
    lines = []
    for line in text:
        lines.append(line.rstrip())
        
    print(solve(lines))


if __name__ == '__main__':
    main()