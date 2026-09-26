# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        
        node_queue = [root]
        output_list = []

        while len(node_queue) > 0:
            node = node_queue.pop(0)
            # do something here
            value = node.val
            if value is None:
                value = "null"
            output_list.append(str(value))

            if value != "null":
                if node.left:
                    # do something
                    node_queue.append(node.left)
                else:
                    node_queue.append(TreeNode(None))

                if node.right:
                    # do something
                    node_queue.append(node.right)
                else:
                    node_queue.append(TreeNode(None))

        return ",".join(output_list)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        
        output_list = data.split(",")
        length = len(output_list)
        virtual_root = TreeNode(None)
        virtual_root.left = TreeNode(None)
        node_queue = [[virtual_root,"left"]]
        index = 0

        while index < length:
            str_val = output_list[index]
            node_info = node_queue.pop(0)
            node = node_info[0]
            direction = node_info[1]

            if str_val == "null":
                # this node is None
                if direction == "left":
                    node.left = None
                else:
                    node.right = None
            else:
                if direction == "left":
                    node = node.left
                else:
                    node = node.right
                node.val = int(str_val)
                node.left = TreeNode(None)
                node.right = TreeNode(None)
                node_queue.append([node,"left"])
                node_queue.append([node,"right"])
            index += 1
        
        return virtual_root.left