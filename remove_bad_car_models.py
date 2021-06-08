import numpy as np
import shutil


def remove_ids_from_folder(folder_root, ids):
    for bad_car_id in ids:
        path = folder_root.format(bad_car_id)
        print(f"Removing: {path}")
        shutil.rmtree(path, ignore_errors=True)


def main():
    bad_car_ids = [
        'e9bccdd7a52f13329b3f352e6fa9112e', '4b092065568af127d64c207b9313bbaf', 'fad616172dbd52649f06afd991af5139',
        '8f87755f22470873e6725f2a23469bfc', '4cecc9df9c777804816bd8f64e08b2bc', '36b23cc38786599285089a13cc567dbd',
        '8b8f4f12e5b142c016abce8cb03e7794', 'da5ee2c950a848f0af8a2e210ebd5168', 'e9c5e6d46c47129c5b72003cd427d0c1',
        'd2776550e240c0d642fb51f57882f419', '648ceaad362345518a6cf8c6b92417f2', '1c490bf1c6b32ef6ff213501a803f212',
        '5089b134ef31941edacf4de272c1e30', 'b88a4c0cb2092fa52fa4ad29a1236d7', 'fe8850296592f2b16abce8cb03e7794',
        'c8fa4fd7fc424121932abeb6e2fd4072', '50e986077b994d6aa848f24544821b25', '810476f203a99d3586b58a9b1f5938e0',
        '425ba801e904cb50f3aaed7e86215c7b', '4e9a489d830e285b59139efcde1fedcb', 'e0901a0a26daebea59139efcde1fedcb',
        'eb1bd7389854311c14f284ebe538e531', '657ea4181e337213fa7c23b34a0b219', '39b307361b650db073a425eed3ac7a0b',
        '4eb5ec5502561124875fb780d36841f', '11d1fdaedf3ab83b8fb28f8a689c8ba3', 'e2ceb9bf23b498dda7431386d9d22644',
        '8590a6c8270375e34b5a812ecf553410', 'e3dff7195a2026dba4db43fa521d5c03', '2c8e9ff5fd58ff3fcd046ccc4d5c3da2',
        'b8599e22b152b96e55e3ad998a1ecb4', 'f6ed076d16960558e6748b6322a06ee3', 'f48659c519f422132d54e7222448a731',
        '504793ed2da6cf7eba3e2415e22cd45c', '39d161909e94d99e61b9ff60b1be412', 'c1186d49101dcd513a0daf3e5400b95c',
        '1166b049a7230db9f50f5d46dfed0533', '431ca41fdf0897c628ccbb4eb8965b05', '67c229c70e64a25e69c2e0a91b39f742',
        '15e52e44cdcc80ed13ded1857c15b5b6', '6cd6f11fe76058089ed785be4fd72d3', '4e009085e3905f2159139efcde1fedcb',
        '7edb40d76dff7455c2ff7551a4114669', 'd80658a2f50c753cf1335b4fef92b83f', '3506955660641ce61d693e0a12bd4ff3',
        '714e69d3b56560ec41a5d15a014fb347', 'c53256341ac5693c66d89345e534c861', 'fed8994632223d52afe1d4530f4c6e24',
        '292f6606c6072b96715e04edb8af9c53', 'e4d396067b97f3676dd84bc138e22252', '1f5a6d3c74f32053b6163196882ac0ca',
        '8922c6c3435f16fee694960c91796f38', '86d9b82220d7ba342e56818be5fde856', 'd7b8287ca11d565bd9bd5ae694086d5',
        '4036332be89511e31141a7d4d06dc13', '2e1178d969bdb3849ea5c205086e2a63', 'de6b2f1796b1887d84e2301109bd5b05',
        'bc8e978655bb60c19fec71e8f4aac226', 'd967be366b99ac00bac978d4dc005d3', 'd3869e2527ff032623276041d0efb3cb',
        'd353bf0e0dfe3ac29cbc1c09129e1507', '56d463162ff5352cbd835ce3c63f4d10', '7478183ebde9c6c2afe717997470b28d',
        '202fbaeffaf49f4b61c6c61410fc904b', 'cb9577139b34703945e8a12904b50643', '876d92ce6a0e4bf399588eee976baae',
        '1c86d4441f5f38d552c4c70ef22e33be', '98fa551211d228ef6a089bd459bbc1be', 'ff809d58a66fb4e85174ee1075ae80c1',
        '53c118280e60df0bd2350421a9405ba', '4c60f32b6efdc7217dfb1ee6a4b12bf8', '5a5b0e1cbb38bdb12d08a76380360b3b',
        'ddb4ad84abca0edcdb8ce1e61248143', '71304f56bb1165e7f42b5c72b4901f94', 'a4d535e1b1d3c153ff23af07d9064736',
        'c5bdc334a3df466e8e1630a4c009bdc0', '846f4ad1db06d8791e0b067dee925db4', '24b9180ac3f89ba4715e04edb8af9c53',
        'e4886a4d0c6ea960fe21694bd5f519d1', '6fcd4ab4d968a975715e04edb8af9c53', 'c916164d0e5c667a75ef328fc121b1c5',
        '9171272d0e357c40435b5ce06ecf3e86', '7d099ac5bcc09250e61b9ff60b1be412', 'd43dc96daed9ba0f91bfeeca48a08b93',
        'e01a56af0788551e7aa225b44626f301', '6c6254a92c485787f1ca7626ddabf47', '43a723b6845f6f90b1eebe42821a51d7',
        'a6fe523f0ef082a2715e04edb8af9c53', '9c27cdc4feb2fa5d4244558fce818712', '525c1f2526cf22be5909c35c7b6459c6',
        '65d6433043c40046b82c0841410a924f', '1e0ada2b1891ea39e79e3bf25d5c768e', 'affba519865b72fc2c95ae1829869305',
        'c0db588c8c816cd2dc668d3d64c871ae', '721ef3846535bfad179005454847728d', '78c5d8e9acc120ce16abce8cb03e7794',
        '260f0644b293fccbfbc06ad9015523cf', '95ebb3fd80f885ad676f197a68a5168a', 'ae9b244f9bee122ba35db63c2ad6fc71'
    ]

    # For a single folder
    root_folder = '/samsung_hdd/Files/AI/TNO/shapenet_renderer/car_view_synthesis_test_set/{}'
    root_folder = '/samsung_hdd/Files/AI/TNO/shapenet_renderer/car_view_synthesis_test_set/{}'
    root_folder = '/samsung_hdd/Files/AI/TNO/remote_folders/train_pose_from_test_image_remotes/car_view_synthesis_test_set_output/car_view_synthesis_test_set_output/{}'
    root_folder = '/samsung_hdd/Files/AI/TNO/shapenet_renderer/car_recognition_validation_set/{}'
    root_folder = '/samsung_hdd/Files/AI/TNO/pixel-nerf/datasets/02958343/{}'

    remove_ids_from_folder(folder_root=root_folder, ids=bad_car_ids)
    # # For test/train/val split
    # root_folder = '/scratch/s2576597/pixel_nerf_datasets/car_renders_train_upper_hemisphere_30_fov_pixel_nerf/cars_test/{}'
    # remove_ids_from_folder(folder_root=root_folder, ids=bad_car_ids)
    #
    # root_folder = '/scratch/s2576597/pixel_nerf_datasets/car_renders_train_upper_hemisphere_30_fov_pixel_nerf/cars_train/{}'
    # remove_ids_from_folder(folder_root=root_folder, ids=bad_car_ids)
    #
    # root_folder = '/scratch/s2576597/pixel_nerf_datasets/car_renders_train_upper_hemisphere_30_fov_pixel_nerf/cars_val/{}'
    # remove_ids_from_folder(folder_root=root_folder, ids=bad_car_ids)

#/scratch/s2576597/new_view_synthesis_datasets/car_view_synthesis_test_set
main()
