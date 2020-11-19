def energy(density, coeff=1.0):
    """ 
    Energy associated with the diffusion model

    Parameters
    ----------

    density: array of positive integers
        Number of particles at each position i in the array
    coeff: float
        Diffusion coefficient.
    """
  # implementation goes here
    from numpy import array, any, sum

    # Make sure input is an numpy array
    density = array(density)

    # ...of the right kind (integer). Unless it is zero length, 
    #    in which case type does not matter.
      
    if density.dtype.kind != 'i' and len(density) > 0:
        raise TypeError("Density should be a array of *integers*.")
    # and the right values (positive or null)
    if any(density < 0):
        raise ValueError("Density should be an array of *positive* integers.")
    if density.ndim != 1:
        raise ValueError("Density should be an a *1-dimensional*" + 
                         "array of positive integers.")
    
    return sum(density * (density - 1))