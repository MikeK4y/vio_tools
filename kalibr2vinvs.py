import numpy as np

from kalibr import stereoFromKalibr
from vins import toVINSStereo

imu_params, cam0_params, cam1_params = stereoFromKalibr('data/camchain-imucam.yaml', 'data/imu_pixhawk.yaml')

cam0_params['T_cam_imu'] = np.linalg.inv(cam0_params['T_cam_imu'])
cam1_params['T_cam_imu'] = np.linalg.inv(cam1_params['T_cam_imu'])

toVINSStereo(
  'data/',
  'cam0_pihole.yaml', 'cam1_pihole.yaml', 'stereo_imu_config.yaml',
  cam0_params, cam1_params, imu_params
)
