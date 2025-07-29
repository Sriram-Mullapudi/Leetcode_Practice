from collections import defaultdict

class Node:
    def __init__(self):
        self.children = {}
        self.delete = False

class Solution:
    def deleteDuplicateFolder(self, paths):
        root = Node()
        
        # 1. Build the folder tree
        for path in paths:
            cur = root
            for name in path:
                if name not in cur.children:
                    cur.children[name] = Node()
                cur = cur.children[name]
        
        serial_map = defaultdict(list)
        
        # 2. Serialize subtrees
        def serialize(node):
            if not node.children:
                return "()"
            parts = []
            for name in sorted(node.children.keys()):
                parts.append(name + serialize(node.children[name]))
            serial = "(" + "".join(parts) + ")"
            serial_map[serial].append(node)
            return serial
        
        serialize(root)
        
        # 3. Mark duplicates
        for serial, nodes in serial_map.items():
            if len(nodes) > 1:
                for node in nodes:
                    node.delete = True
        
        ans = []
        
        # 4. Collect remaining paths
        def dfs(node, path):
            for name, child in node.children.items():
                if not child.delete:
                    new_path = path + [name]
                    ans.append(new_path)
                    dfs(child, new_path)
        
        dfs(root, [])
        return ans
