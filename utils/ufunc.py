
from astropy import units as u
from astropy.coordinates import SkyCoord

import numpy as np

from scipy import spatial

from astropy.cosmology import FlatLambdaCDM
cosmo = FlatLambdaCDM(H0=70, Om0=0.3, Tcmb0=2.725)

from utils.mistree import construct_mst

h =  cosmo.H(0).value / 100

def coords_to_xyz(ra, dec, redshift):
    
    
    dist_grp = cosmo.comoving_distance(redshift).value #Mpc
    coords = SkyCoord(ra = ra * u.degree, dec = dec * u.degree, distance = dist_grp * u.Mpc)

    x = coords.cartesian.x
    y = coords.cartesian.y
    z = coords.cartesian.z
    
    return x, y, z

def cal_r200(hmass, redshift):
    
    Hs = cosmo.H(redshift).value
 
    G = 4.2e-3 * 1e-6 # Mpc M_sun-1 (km/s)^2

    r200 = (( hmass * G / 100 / Hs**2 )**(1/3)).value #mpc
    
    return r200


class CW():
    
    def __init__(self, coords_grp, coords_gal, ll_cl = 5.75, ll_fil = 4.12, ll_tdr = 3.0):
        
        self.x_grp, self.y_grp, self.z_grp = coords_grp
        self.x_gal, self.y_gal, self.z_gal = coords_gal
        
        self.ll_cl = ll_cl
        self.ll_fil = ll_fil
        self.ll_tdr = ll_tdr
        
    def cal_mask_cluster(self, r200, k_neighbours = 20):
        
        edge_length, edge_x, edge_y, edge_z, edge_index = construct_mst(self.x_grp, self.y_grp, self.z_grp, k_neighbours)
        self.edge_lengh = edge_length
        
        tree = spatial.cKDTree(np.array([self.x_grp, self.y_grp, self.z_grp]).T)
        d_node_1 = tree.query(np.array([self.x_gal, self.y_gal, self.z_gal]).T, k = 1)
        
        mask_cluster = (d_node_1[0] < r200[d_node_1[1]])
        self.mask_cluster = mask_cluster
        
        d_node = tree.query(np.array([self.x_gal, self.y_gal, self.z_gal]).T, k = 2)
        self.d_node = d_node
        
        return mask_cluster
    
    def cal_mask_filament(self):
        mask_link = self.edge_lengh < self.ll_cl / h
        grp_index = np.where(mask_link)[0]
        
        mask_cand1 = np.isin(self.d_node[1][:, 0], grp_index)
        mask_cand2 = np.isin(self.d_node[1][:, 1], grp_index)
        mask_cand = mask_cand1 & mask_cand2
        
        P1 = np.array([self.x_grp[self.d_node[1][:, 0]], self.y_grp[self.d_node[1][:, 0]], self.z_grp[self.d_node[1][:, 0]]]).T
        P2 = np.array([self.x_grp[self.d_node[1][:, 1]], self.y_grp[self.d_node[1][:, 1]], self.z_grp[self.d_node[1][:, 1]]]).T

        Pgal = np.array([self.x_gal, self.y_gal, self.z_gal]).T
        
        d_fil = np.linalg.norm(
            np.cross(P2 - Pgal, P1 - Pgal)
            , axis = 1) / np.linalg.norm(P2 - P1, axis = 1) 
        self.d_fil = d_fil
        
        mask_filament = mask_cand & ~self.mask_cluster & (d_fil < self.ll_fil / 0.7)
        self.mask_filament = mask_filament
        
        return mask_filament
        
    
    def cal_mask_tendril(self, k_neighbours = 20):
        mask_remain = (~self.mask_filament & ~self.mask_cluster)
        number_of_nodes_t = len(self.x_gal[mask_remain])
        
        edge_length_t, edge_x_t, edge_y_t, edge_z_t, edge_index_t = construct_mst(self.x_gal[mask_remain], self.y_gal[mask_remain], self.z_gal[mask_remain], k_neighbours)

        mask_link_t = edge_length_t < self.ll_tdr / 0.7 # flag for mask_remain
        mask_tendril = np.zeros(shape = len(self.mask_cluster), dtype = bool)

        mask_tendril[
            np.where(mask_remain)[0][edge_index_t[0][mask_link_t]]
        ] = True

        mask_tendril[
            np.where(mask_remain)[0][edge_index_t[1][mask_link_t]]
        ] = True

        mask_tendril[self.mask_cluster] = False
        mask_tendril[self.mask_filament] = False
        self.mask_tendril = mask_tendril
        
        return mask_tendril

    def cal_mask_void(self):
        
        mask_void = ~self.mask_cluster & ~self.mask_filament & ~self.mask_tendril
        self.mask_void = mask_void
        
        return mask_void