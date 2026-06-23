import numpy as np


def chronotope_non_residential(B:np.ndarray,O:np.ndarray)-> np.ndarray:
    """
    Calculates the population in non-residential buildings at time t in each grid.
    
    Dimensions:
        N: Number of spatial grid cells.
        J: Number of non-residential building types.
        T: Number of time steps.

    Args:
        B (np.ndarray): Shape (N,J). The total floor area of each non-residential building type per grid cell.
        O (np.ndarray): Shape (J,T). The occupancy density for each building type at each time step.

    Returns:
        np.ndarray: Shape (N,T). The population in non-residential buildings at time t in each grid.
    """
    C_n = np.dot(B,O)
    return C_n


def ratio(P_r:np.ndarray,C_n) -> np.ndarray:
    """
    Calculates the average decreasing ratio of the population in residential buildings.

    Args:
        P_r (np.ndarray): Shape (N,). The base residential population within each grid cell.
        C_n (np.ndarray): Shape (N,T). The  non-residential population within each grid cell at each time step.


    Returns:
        np.ndarray: Shape (T,). The average decreasing ratio of the population in residential buildings across all grids at each time step.
    """
    return np.sum(C_n,axis=0) / np.sum(P_r)


def Chronotope_residential(P_r: np.ndarray,ratio:np.ndarray) -> np.ndarray:
    """
    Calculates the the population in residential buildings at time t in each grid.

    Args:
        P_r (np.ndarray): Shape (N,). The base residential population within each grid cell.
        ratio (np.ndarray): Shape (T,). The average decreasing ratio of the population in residential buildings across all grids at each time step.

    Returns:
        np.ndarray: Shape (N,T). The population in residential buildings at time t in each grid
    """
    C_r = P_r[:,np.newaxis] * (1-ratio)
    return C_r


def Chronotope_grid(C_r,C_n):
    
    return C_r+C_n

    

if __name__ == "__main__":
    a = np.array([1,2,3])
    b = np.array([
        [0,1,1,1],
        [0,2,1,2],
        [0,2,3,3]
        ])
    r = ratio(a,b)
    C_r = Chronotope_residential(a,r)
    print(Chronotope_grid(C_r,b))