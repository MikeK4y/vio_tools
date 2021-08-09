from kalibr import stereofromKalibr
from vins import toVINSStereo

imu_params, cam0_params, cam1_params = stereofromKalibr('data/camchain-imucam.yaml', 'data/imu_pixhawk.yaml')
toVINSStereo(
  'data/cam0_pihole.yaml', 'data/cam1_pihole.yaml', 'data/stereo_imu_config.yaml',
  cam0_params, cam1_params, imu_params
)
