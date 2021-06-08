from car_train_test_val import train, test, val


root_dir = './car_renders_train_upper_hemisphere_30_fov_v2'
dest_dir = './car_renders_train_upper_hemisphere_30_fov_v2_pixel_nerf'
bash_script_name = 'car_train_val_test_split_bash.sh'
ds_name = 'cars'

print(len(test))
output_lines = []
for obj_id in train:
    output_lines.append(f"cp -r {root_dir}/{obj_id} {dest_dir}/{ds_name}_train")

for obj_id in test:
    output_lines.append(f"cp -r {root_dir}/{obj_id} {dest_dir}/{ds_name}_test")

for obj_id in val:
    output_lines.append(f"cp -r {root_dir}/{obj_id} {dest_dir}/{ds_name}_val")


with open(bash_script_name, 'w') as f:
    f.write("\n".join(output_lines))
