# -*- encoding: utf-8 -*-
# Module max_tree_alpha

from morph_tree_alpha import MorphTreeAlpha
from max_tree_alpha_methods import draw1DImageTree, vmax, hmax, computeHeight, computeVolume, computeStabilityMeasure,\
                                   computeExtinctionValues, getSignature, extinctionFilter, mmsT, mmsMSER 
                                   

from max_tree_alpha_aux import compute_height_aux_c, compute_volume_aux_c, compute_stability_measure_aux_c, \
                               compute_extinction_values_aux_c, get_signature_aux_c, extinction_filter_aux_c, \
                               mms_t_aux_c, mms_mser_aux_c
  

from max_tree_alpha_aux_py import compute_height_aux_py, compute_volume_aux_py, compute_stability_measure_aux_py, \
                                  compute_extinction_values_aux_py, get_signature_aux_py, extinction_filter_aux_py, \
                                  mms_t_aux_py, mms_mser_aux_py

from morph_tree_alpha import MorphTreeAlpha
                                     
class MaxTreeAlpha(MorphTreeAlpha):
  """
  This class builds the max-tree corresponding to a 8-bit grayscale image.
  Many methods,to extract attributes and filter the max-tree are available.
  **Input:**
  img -> uint8 image, may be either 2D or 3D. When working with 1D signals use
  a 2D array with the shape 1xW.
  Bc -> Boolean array corresponding to the connectivity to be used during the
  tree construction. The convention is that coordinates (0,0) or (0,0,0) are
  in the center of the array.
  """

  hmax = hmax
  vmax = vmax
  draw1DImageTree = draw1DImageTree
  computeHeight = computeHeight
  computeVolume = computeVolume
  computeStabilityMeasure = computeStabilityMeasure
  computeExtinctionValues = computeExtinctionValues
  getSignature = getSignature
  extinctionFilter = extinctionFilter
  mmsT = mmsT
  mmsMSER = mmsMSER

  def __init__(self, img, Bc, implementation = 'c'):
    MorphTreeAlpha.__init__(self,img, Bc,option = 'max_tree',implementation = implementation)

    if self.implementation == 'c':
        self.compute_height_aux = compute_height_aux_c
        self.compute_volume_aux = compute_volume_aux_c
        self.compute_stability_measure_aux = compute_stability_measure_aux_c
        self.compute_extinction_values_aux = compute_extinction_values_aux_c
        self.get_signature_aux = get_signature_aux_c
        self.extinction_filter_aux = extinction_filter_aux_c
        self.mms_t_aux = mms_t_aux_c
        self.mms_mser_aux = mms_mser_aux_c
    else:
        self.compute_height_aux = compute_height_aux_py
        self.compute_volume_aux = compute_volume_aux_py
        self.compute_stability_measure_aux = compute_stability_measure_aux_py
        self.compute_extinction_values_aux = compute_extinction_values_aux_py
        self.get_signature_aux = get_signature_aux_py
        self.extinction_filter_aux = extinction_filter_aux_py
        self.mms_t_aux = mms_t_aux_py
        self.mms_mser_aux = mms_mser_aux_py

