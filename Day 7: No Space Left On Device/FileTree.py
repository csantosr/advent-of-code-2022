class FileTree:
    def __init__(self, name, is_dir, size=None):
        self.name = name
        self.is_dir = is_dir
        self.size = size
        self.children = []
        self.parent = None

    def get_child(self, name):
        return next(child for child in self.children if child.name == name)

    def add_child(self, child):
        self.children.append(child)
        child.set_parent(self)

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_size(self):
        if not self.is_dir:
            return self.size
        sum_size = 0
        for child in self.children:
            sum_size += child.get_size()
        return sum_size

    def get_all_dirs(self):
        dirs = []
        if self.is_dir:
            dirs.append(self)
            for child in self.children:
                dirs.extend(child.get_all_dirs())
        return dirs

    def __str__(self, deep=0):
        result = ['{}- {} ({})'.format(
            ' '*(4*deep),
            self.name,
            'dir, size={}'.format(self.get_size()) if self.is_dir else 'file, size={}'.format(self.size)
        )]
        for child in self.children:
            result.append(child.__str__(deep+1))
        return '\n'.join(result)
