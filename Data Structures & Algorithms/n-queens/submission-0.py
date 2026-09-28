class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        line_index2left_elements_ref_dict: Dict[int,Node] = self.initialise_index2left_elements_ref_dict()
        layouts = self.recur(0, line_index2left_elements_ref_dict)
        return self.generate_solution_according_to_paths(layouts)

    def generate_solution_according_to_paths(self, layouts):
        results = []
        for layout in layouts:
            result = self.create_scratch()
            for q_element in layout:
                result[q_element.row][q_element.col] = "Q"
            results.append(list(map(lambda x: "".join(x), result)))
        return results
    
    def create_scratch(self):
        scratch = []
        for _ in range(self.n):
            scratch.append(["."] * self.n)
        return scratch

    def initialise_index2left_elements_ref_dict(self):
        ref_dict = {}
        for i in range(self.n):
            ref_dict[i] = [Node(i, j) for j in range(self.n)]
        return ref_dict

    def update_left_elements_in_the_following_lines(self, line_index2left_elements_ref_dict, element, new_line_cursor):
        new_ref_dict = {}

        # remove vertical
        for line_index in range(new_line_cursor, self.n):
            this_line_left_elements = []
            left_elements = line_index2left_elements_ref_dict[line_index]
            for left_element in left_elements:
                if not (self.is_vertical(left_element, element) or self.is_diagonal(left_element, element)):
                    this_line_left_elements.append(left_element)
            
            new_ref_dict[line_index] = this_line_left_elements
        return new_ref_dict

    def is_vertical(self, this_element, target_element):
        return this_element.col == target_element.col

    def is_diagonal(self, this_element, target_element):
        return abs(this_element.row - target_element.row) == abs(this_element.col - target_element.col)

    def recur(self, line_cursor, line_index2left_elements_ref_dict):
        left_elements = line_index2left_elements_ref_dict[line_cursor] # request self.line_index2left_elements_ref_dict to get a list
        if len(left_elements) == 0:
            return None

        layouts = []
        new_line_cursor = line_cursor + 1
        for element in left_elements:
            if new_line_cursor != self.n:
                updated_line_index2left_elements_ref_dict = self.update_left_elements_in_the_following_lines(line_index2left_elements_ref_dict, element, new_line_cursor) # update self.line_index2left_elements_ref_dict according to the rule of n queens
                child_layouts = self.recur(new_line_cursor, updated_line_index2left_elements_ref_dict)
            else:
                child_layouts = [[]]

            if child_layouts is not None:
                for child_layout in child_layouts:
                    layout = child_layout
                    layout.append(element)
                    layouts.append(layout)

        return layouts
    
class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
