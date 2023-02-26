"""
Functions
calculate_score (Parent,Child,Target)
pos_to_node
"""
class Astar:
    def __init__(self, map, start, target):
        self.map = map
        self.start = start
        self.target = target
        self.nodes_found = []
        self.nodes_checked = []

    def calculate_score(self,parent,child,target):
        """
        Calculates the heuristic value of a node
        Args:
            Parent(Node):The previous node being explored
            Child(Node):The node being scored
            Target(tuple): The tuple containing the x and y position of the target
        Returns:
            Score (Double):The heuristic value of the node
        """
        _current_pos=child.coords()
        _target_pos=self.target
        _dist_to_target=((_current_pos[0]-_target_pos[0])**2+(_current_pos[1]-_target_pos[1])**2)**0.5
        score=_dist_to_target+parent.heuristic()+self.map.drone_dim

        return score

    def pos_to_node(self,pos,map):
        """
        Finds the closest node to the given position
        Args:
            pos(tuple): The tuple containing an x and y position in the map frame
            map(Map): the map of nodes for the position coords
        Returns:
            closest_node (Node):The node closest to the position
        """
        node_x = pos[0]//map.drone_dim
        node_y = pos[1]//map.drone_dim
        closest_node = map.array[node_x][node_y]
        return closest_node

    def a_star_search(self):
        """
        Calculates the heuristic value of a node
        Args:
            map(map):the map with the expected obstacles
            start(tuple):The drone start position
            target(tuple): The tuple containing the x and y position of the target
        Returns:
            path (List):The list of tuples defining the drone path
        """

        self.nodes_found.append(self.pos_to_node(self.start))

        while True:
            if len(self.nodes_found) == 0:
                print("Tough luck, we couldn't find a solution")
                break
            
            #Find the next node to check
            self.nodes_found.sort()
            node_to_check = self.nodes_found.pop(0)

            self.nodes_checked.append(node_to_check)

            #Yay, we found the target! Time to find the path.
            if node_to_check == self.pos_to_node(self.target):
                path = [node_to_check]
                node = node_to_check.parent
                while True:
                    path.append(node)
                    if node.parent in None:
                        break
                    node = node.parent
                trajectory = []
                for traj_node in path:
                   trajectory.append(node.coords)
                return path
            
            new_nodes = find_nodes(node_to_check)
            for node in new_nodes:
                node.heuristic=calculate_score(node_to_check,node,target,map)
                if node not in nodes_found and node not in nodes_checked:
                    node.parent=node_to_check
                    nodes_found.append(node)
                elif node in nodes_found and node.parent != node_to_check:
                    for node in self.opened:
                        if node.value == node_value: