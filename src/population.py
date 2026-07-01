import numpy as np


def compute_non_residential_pop(A:np.ndarray,D:np.ndarray)-> np.ndarray:
    """
    Calculates the population in non-residential buildings at time t in each grid.
    
    Dimensions:
        N: Number of spatial grid cells.
        J: Number of non-residential building types.
        T: Number of time steps.

    Args:
        A (np.ndarray): Shape (N,J). The total area of each non-residential building type per grid cell.
        D (np.ndarray): Shape (J,T). The occupancy density for each building type at each time step.

    Returns:
        np.ndarray: Shape (N,T). The population in non-residential buildings at time t in each grid.
    """
    P_nres = np.dot(A,D)
    return P_nres


def compute_global_decrease_ratio(P_base:np.ndarray,P_nres) -> np.ndarray:
    """
    Calculates the average decreasing ratio of the population in residential buildings across all grids.

    Args:
        P_base (np.ndarray): Shape (N,). The base residential population within each grid cell.
        P_nres (np.ndarray): Shape (N,T). The  non-residential population within each grid cell at each time step.


    Returns:
        np.ndarray: Shape (T,). The average decreasing ratio of the population in residential buildings across all grids at each time step.
    """
    return np.sum(P_nres,axis=0) / np.sum(P_base)


def compute_residential_pop(P_base: np.ndarray,ratio:np.ndarray) -> np.ndarray:
    """
    Calculates the the population in residential buildings at time t in each grid.

    Args:
        P_base (np.ndarray): Shape (N,). The base residential population within each grid cell.
        ratio (np.ndarray): Shape (T,). The average decreasing ratio of the population in residential buildings across all grids at each time step.

    Returns:
        np.ndarray: Shape (N,T). The population in residential buildings at time t in each grid
    """
    P_res = P_base[:,np.newaxis] * (1-ratio)
    return P_res


def compute_grid_pop(P_res,P_nres):
    
    return P_res + P_nres

    

if __name__ == "__main__":
    a = np.array([1,2,3])
    b = np.array([
        [0,1,1,1],
        [0,2,1,2],
        [0,2,3,3]
        ])
    r = compute_global_decrease_ratio(a,b)
    C_r = compute_residential_pop(a,r)
    print(compute_grid_pop(C_r,b))