import numpy as np

from kalibr import stereoFromKalibr
from msckf import toMSCKF

imu_params, cam0_params, cam1_params = stereoFromKalibr('data/camchain-imucam.yaml', 'data/imu_pixhawk.yaml')

T_cn_cnm1 = np.matmul(cam1_params['T_cam_imu'], np.linalg.inv(cam0_params['T_cam_imu']))

toMSCKF(
  'data/',
  'camchain_msckf.yaml',
  T_cn_cnm1, cam0_params, cam1_params)