def toVINSStereo(path,
                 cam0_file, cam1_file, stereo_file,
                 cam0_params, cam1_params, imu_params):
  # Camera 0 file
  writeCameraPinholeFile(path + cam0_file, cam0_params)

  # Camera 1 file
  writeCameraPinholeFile(path + cam1_file, cam1_params)

  # Stereo Config file
  writeStereoConfigFile(path + stereo_file, cam0_file, cam1_file, cam0_params, cam1_params, imu_params)

def writeCameraPinholeFile(file_name, camera_parameters):
    file = open(file_name, 'w')

    file.write('%YAML:1.0\n')
    file.write('---\n')
    file.write('model_type: PINHOLE\n')
    file.write('camera_name: camera\n')
    file.write('image_width: {:d}\n'.format(int(camera_parameters['resolution'][0])))
    file.write('image_height: {:d}\n'.format(int(camera_parameters['resolution'][1])))
    file.write('distortion_parameters:\n')
    file.write('   k1: {:.12e}\n'.format(camera_parameters['distortion'][0]))
    file.write('   k2: {:.12e}\n'.format(camera_parameters['distortion'][1]))
    file.write('   p1: {:.12e}\n'.format(camera_parameters['distortion'][2]))
    file.write('   p2: {:.12e}\n'.format(camera_parameters['distortion'][3]))
    file.write('projection_parameters:\n')
    file.write('   fx: {:.12e}\n'.format(camera_parameters['intrinsics'][0]))
    file.write('   fy: {:.12e}\n'.format(camera_parameters['intrinsics'][1]))
    file.write('   cx: {:.12e}\n'.format(camera_parameters['intrinsics'][2]))
    file.write('   cy: {:.12e}\n'.format(camera_parameters['intrinsics'][3]))

def writeStereoConfigFile(file_name,
                          cam0_calib_file, cam1_calib_file,
                          cam0_params, cam1_params, imu_params):
    file = open(file_name, 'w')

    file.write('%YAML:1.0\n\n')

    file.write('# Common parameters\n')
    file.write('imu: 1\n')
    file.write('num_of_cam: 2\n\n')

    file.write('imu_topic: {:s}\n'.format(imu_params['topic']))
    file.write('image0_topic: {:s}\n'.format(cam0_params['topic']))
    file.write('image1_topic: {:s}\n'.format(cam1_params['topic']))
    file.write('output_path: "~/output/"\n\n')

    file.write('cam0_calib: {:s}\n'.format(cam0_calib_file))
    file.write('cam1_calib: {:s}\n'.format(cam1_calib_file))
    file.write('image_width: {:d}\n'.format(int(cam0_params['resolution'][0])))
    file.write('image_height: {:d}\n\n'.format(int(cam0_params['resolution'][1])))

    file.write('# Extrinsic parameter between IMU and Camera\n')
    file.write('estimate_extrinsic: 0\n\n')

    file.write('body_T_cam0: !!opencv-matrix\n')
    file.write('   rows: 4\n')
    file.write('   cols: 4\n')
    file.write('   dt: d\n')
    file.write('   data: [{: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(cam0_params['T_cam_imu'][0][0], cam0_params['T_cam_imu'][0][1], cam0_params['T_cam_imu'][0][2], cam0_params['T_cam_imu'][0][3]))
    file.write('          {: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(cam0_params['T_cam_imu'][1][0], cam0_params['T_cam_imu'][1][1], cam0_params['T_cam_imu'][1][2], cam0_params['T_cam_imu'][1][3]))
    file.write('          {: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(cam0_params['T_cam_imu'][2][0], cam0_params['T_cam_imu'][2][1], cam0_params['T_cam_imu'][2][2], cam0_params['T_cam_imu'][2][3]))
    file.write('          {: .12e}, {: .12e}, {: .12e}, {: .12e}]\n\n'.format(cam0_params['T_cam_imu'][3][0], cam0_params['T_cam_imu'][3][1], cam0_params['T_cam_imu'][3][2], cam0_params['T_cam_imu'][3][3]))

    file.write('body_T_cam1: !!opencv-matrix\n')
    file.write('   rows: 4\n')
    file.write('   cols: 4\n')
    file.write('   dt: d\n')
    file.write('   data: [{: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(cam1_params['T_cam_imu'][0][0], cam1_params['T_cam_imu'][0][1], cam1_params['T_cam_imu'][0][2], cam1_params['T_cam_imu'][0][3]))
    file.write('          {: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(cam1_params['T_cam_imu'][1][0], cam1_params['T_cam_imu'][1][1], cam1_params['T_cam_imu'][1][2], cam1_params['T_cam_imu'][1][3]))
    file.write('          {: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(cam1_params['T_cam_imu'][2][0], cam1_params['T_cam_imu'][2][1], cam1_params['T_cam_imu'][2][2], cam1_params['T_cam_imu'][2][3]))
    file.write('          {: .12e}, {: .12e}, {: .12e}, {: .12e}]\n\n'.format(cam1_params['T_cam_imu'][3][0], cam1_params['T_cam_imu'][3][1], cam1_params['T_cam_imu'][3][2], cam1_params['T_cam_imu'][3][3]))

    file.write('# Multiple thread support\n')
    file.write('multiple_thread: 1\n\n')

    file.write('# Feature tracker parameters\n')
    file.write('max_cnt: 150                 # max feature number in feature tracking\n')
    file.write('min_dist: 30                 # min distance between two features \n')
    file.write('freq: 10                     # frequence (Hz) of publish tracking result. At least 10Hz for good estimation. If set 0, the frequence will be same as raw image \n')
    file.write('F_threshold: 1.0             # ransac threshold (pixel)\n')
    file.write('show_track: 1                # publish tracking image as topic\n')
    file.write('flow_back: 1                 # perform forward and backward optical flow to improve feature tracking accuracy\n\n')

    file.write('# Optimization parameters\n')
    file.write('max_solver_time: 0.04        # max solver itration time (ms), to guarantee real time\n')
    file.write('max_num_iterations: 8        # max solver itrations, to guarantee real time\n')
    file.write('keyframe_parallax: 10.0      # keyframe selection threshold (pixel)\n\n')

    file.write('# IMU parameters\n')
    file.write('acc_n: {:.4e}            # accelerometer measurement noise standard deviation\n'.format(imu_params['acc_noise']))
    file.write('gyr_n: {:.4e}            # gyroscope measurement noise standard deviation\n'.format(imu_params['gyr_noise']))
    file.write('acc_w: {:.4e}            # accelerometer bias random work noise standard deviation\n'.format(imu_params['acc_randomwalk']))
    file.write('gyr_w: {:.4e}            # gyroscope bias random work noise standard deviation\n'.format(imu_params['gyr_randomwalk']))
    file.write('g_norm: 9.81007              # gravity magnitude\n\n')

    file.write('# Unsynchronization parameters\n')
    file.write('estimate_td: 0               # online estimate time offset between camera and imu\n')
    file.write('td: 0.0                      # initial value of time offset. unit: s. Read image clock + td = real image clock (IMU clock)\n\n')

    file.write('# Loop closure parameters\n')
    file.write('load_previous_pose_graph: 0                      # load and reuse previous pose graph; load from "pose_graph_save_path"\n')
    file.write('pose_graph_save_path: "~/output/pose_graph/"     # save and load path\n')
    file.write('save_image: 1                                    # save image in pose graph for visualization purpose; you can close this function by setting 0\n')