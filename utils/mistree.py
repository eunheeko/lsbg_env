from scipy.sparse.csgraph import minimum_spanning_tree
from sklearn.neighbors import kneighbors_graph
import numpy as np

def construct_mst(x, y, z, k_neighbours =20):

    vertices = np.array([x, y, z]).T
    k_nearest_neighbour_graph = kneighbors_graph(vertices, n_neighbors=k_neighbours, mode='distance')

    tree = minimum_spanning_tree(k_nearest_neighbour_graph, overwrite=True)
    tree = tree.tocoo()
    edge_length = tree.data
    index1 = tree.row
    index2 = tree.col

    x1 = x[index1]
    x2 = x[index2]
    edge_x = np.array([x1, x2])
    y1 = y[index1]
    y2 = y[index2]
    edge_y = np.array([y1, y2])
    z1 = z[index1]
    z2 = z[index2]
    edge_z = np.array([z1, z2])

    # A 2 dimensional array, containing the node indexes on either side of each edge.
    edge_index = np.array([index1, index2])

    return edge_length, edge_x, edge_y, edge_z, edge_index


def get_graph_degree(edge_index, number_of_nodes):
    index1, index2 = edge_index[0], edge_index[1]
    number_of_edges = len(index1)
    
    degree = np.zeros(number_of_nodes).astype(int)

    for i in range(number_of_edges):
        degree[index1[i]] += 1
        degree[index2[i]] += 1    

    edge_degree = np.array([degree[index1], degree[index2]])

    return degree, edge_degree



def get_branch_index(edge_index, edge_degree, branch_cutting_frequency=1000):

    degree1 = edge_degree[0]
    degree2 = edge_degree[1]
    index1 = edge_index[0]
    index2 = edge_index[1]
    condition = np.where((degree1 == 2.) & (degree2 == 2.))[0]
    index_branch_mid = condition
    index_branch_mid1 = index1[index_branch_mid]
    index_branch_mid2 = index2[index_branch_mid]
    condition = np.where(((degree1 == 2.) & (degree2 != 2.)) | ((degree1 != 2.) & (degree2 == 2.)))[0]
    index_branch_end = condition
    index_branch_end1 = index1[index_branch_end]
    index_branch_end2 = index2[index_branch_end]
    degree_branch_end1 = degree1[index_branch_end]
    degree_branch_end2 = degree2[index_branch_end]
    check_mid = np.ones(len(index_branch_mid))
    check_end = np.ones(len(index_branch_end))
    branch_index = []
    branch_index_rejected = []
    mask_end = np.ones(index_branch_end.shape, dtype=bool)
    mask_mid = np.ones(index_branch_mid.shape, dtype=bool)
    count = 0
    item = 0

    while item < len(index_branch_end):
        if check_end[item] == 1.:
            check_end[item] = 0.
            done = 0.
            _twig = []
            _twig.append(index_branch_end[item])
            if degree_branch_end1[item] == 2.:
                node_index = index_branch_end1[item]
            elif degree_branch_end2[item] == 2.:
                node_index = index_branch_end2[item]
            else:
                assert ValueError("branch edge incorrect.")
            mask_end[item] = False
            while done == 0.:
                condition = np.where(((check_mid == 1.) & (index_branch_mid1 == node_index)) |
                                        ((check_mid == 1.) & (index_branch_mid2 == node_index)))[0]
                if len(condition) == 0:
                    condition = np.where(((check_end == 1.) & (index_branch_end1 == node_index)) |
                                            ((check_end == 1.) & (index_branch_end2 == node_index)))[0]
                    if len(condition) == 0:
                        branch_index_rejected = branch_index_rejected + \
                                                np.ndarray.tolist(np.ndarray.flatten(np.array(_twig)))
                        done = 1.
                    else:
                        check_end[condition] = 0.
                        _twig.append(index_branch_end[condition])
                        done = 1.
                        mask_end[condition] = False
                        branch_index.append(np.ndarray.tolist(np.ndarray.flatten(np.array(_twig, dtype=object))))
                else:
                    if len(condition) == 1:
                        check_mid[condition] = 0.
                        _twig.append(index_branch_mid[condition])
                        if index_branch_mid1[condition] == node_index:
                            node_index = index_branch_mid2[condition]
                        elif index_branch_mid2[condition] == node_index:
                            node_index = index_branch_mid1[condition]
                        else:
                            assert ValueError("Identification error.")
                        mask_mid[condition] = False
                    else:
                        assert ValueError("Found more than one vertex.")
        else:
            pass
        if count % branch_cutting_frequency == 0 and count != 0:
            index_branch_end = index_branch_end[mask_end]
            check_end = check_end[mask_end]
            index_branch_end1 = index_branch_end1[mask_end]
            index_branch_end2 = index_branch_end2[mask_end]
            degree_branch_end1 = degree_branch_end1[mask_end]
            degree_branch_end2 = degree_branch_end2[mask_end]
            index_branch_mid = index_branch_mid[mask_mid]
            check_mid = check_mid[mask_mid]
            index_branch_mid1 = index_branch_mid1[mask_mid]
            index_branch_mid2 = index_branch_mid2[mask_mid]
            mask_end = mask_end[mask_end]
            mask_mid = mask_mid[mask_mid]
            count = count + 1
            item = 0
        elif count % 1001 == 0:
            count = count + 1
            item = item + 1
        elif item == len(index_branch_end) - 1:
            index_branch_end = index_branch_end[mask_end]
            check_end = check_end[mask_end]
            index_branch_end1 = index_branch_end1[mask_end]
            index_branch_end2 = index_branch_end2[mask_end]
            degree_branch_end1 = degree_branch_end1[mask_end]
            degree_branch_end2 = degree_branch_end2[mask_end]
            index_branch_mid = index_branch_mid[mask_mid]
            check_mid = check_mid[mask_mid]
            index_branch_mid1 = index_branch_mid1[mask_mid]
            index_branch_mid2 = index_branch_mid2[mask_mid]
            mask_end = mask_end[mask_end]
            mask_mid = mask_mid[mask_mid]
            count = count + 1
            item = 0
        else:
            count = count + 1
            item = item + 1
        branch_index_rejected = branch_index_rejected + np.ndarray.tolist(np.ndarray.flatten(np.array(index_branch_mid)))
        branch_index = [np.ndarray.tolist(np.hstack(np.array(branch_index[i], dtype=object))) for i in range(0, len(branch_index))]
        
        if len(branch_index_rejected) != 0:
            branch_index_rejected = np.ndarray.tolist(np.hstack(np.array(branch_index_rejected)))
        return branch_index, branch_index_rejected


def get_branch_end_index(edge_index, edge_degree, branch_index):
    
    branch_edge_index_end1 = [i[0] for i in branch_index]
    branch_edge_index_end2 = [i[len(i) - 1] for i in branch_index]
    edge_degree_end12 = edge_degree[1][branch_edge_index_end1]
    index11 = edge_index[0][branch_edge_index_end1]
    index12 = edge_index[1][branch_edge_index_end1]
    condition = np.where(edge_degree_end12 != 2.)[0]
    branch_index_end1 = np.copy(index11)
    branch_index_end1[condition] = index12[condition]
    edge_degree22 = edge_degree[1][branch_edge_index_end2]
    index21 = edge_index[0][branch_edge_index_end2]
    index22 = edge_index[1][branch_edge_index_end2]
    condition = np.where(edge_degree22 != 2.)[0]
    branch_index_end2 = np.copy(index21)
    branch_index_end2[condition] = index22[condition]
    branch_end = np.array([branch_index_end1, branch_index_end2])
    return branch_end
