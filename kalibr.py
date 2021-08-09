import numpy as np

def getTMatrix(lines):
    T_row_0 = [float(e) for e in lines[0][5:-2].split(', ')]
    T_row_1 = [float(e) for e in lines[1][5:-2].split(', ')]
    T_row_2 = [float(e) for e in lines[2][5:-2].split(', ')]
    T_row_3 = [float(e) for e in lines[3][5:-2].split(', ')]
    
    return np.asarray([T_row_0, T_row_1, T_row_2, T_row_3])

def getArray(line):
    array_start = line.find('[') + 1
    return np.asarray([float(e.strip('[]')) for e in line[array_start:].split(', ')])

def stereofromKalibr(camchain_file_name, imu_file_name):
  # Camera parameters
  camchain_file = open(camchain_file_name, 'r')
  camchain_file_lines = camchain_file.readlines()

  camera0_parameters = {
    'topic' : camchain_file_lines[13].split()[1],
    'resolution' : getArray(camchain_file_lines[12].strip('\n')),
    'intrinsics' : getArray(camchain_file_lines[11].strip('\n')),
    'distortion' : getArray(camchain_file_lines[8].strip('\n') + camchain_file_lines[9].strip('\n')),
    'T_cam_imu' : getTMatrix(camchain_file_lines[2:6])
  }

  camera1_parameters = {
    'topic' : camchain_file_lines[32].split()[1],
    'resolution' : getArray(camchain_file_lines[31].strip('\n')),
    'intrinsics' : getArray(camchain_file_lines[30].strip('\n')),
    'distortion' : getArray(camchain_file_lines[27].strip('\n') + camchain_file_lines[28].strip('\n')),
    'T_cam_imu' : getTMatrix(camchain_file_lines[16:20])
  }

  # IMU parameters
  imu_file = open(imu_file_name, 'r')
  imu_file_lines = imu_file.readlines()

  imu_parameters = {
    'topic' : imu_file_lines[0].split()[1],
    'rate' : float(imu_file_lines[1].split()[1]),
    'acc_noise' : float(imu_file_lines[3].split()[1]),
    'acc_randomwalk' : float(imu_file_lines[4].split()[1]),
    'gyr_noise' : float(imu_file_lines[5].split()[1]),
    'gyr_randomwalk' : float(imu_file_lines[6].split()[1]),
  }

  return imu_parameters, camera0_parameters, camera1_parameters
