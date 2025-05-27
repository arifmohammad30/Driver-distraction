import os

# Define paths to label directories
label_dirs = [
    'labels/train',
    'labels/valid',
    'labels/test',
]

# Mapping: old class ID → new class ID
class_map = {
    1: 0,  # Left Hand
    7: 1,  # Right Hand
    8: 2,  # Steering Wheel
    6: 3   # Radio
}

for label_dir in label_dirs:
    for filename in os.listdir(label_dir):
        if filename.endswith(".txt"):
            new_lines = []
            with open(os.path.join(label_dir, filename), 'r') as f:
                for line in f:
                    parts = line.strip().split()
                    class_id = int(parts[0])
                    if class_id in class_map:
                        parts[0] = str(class_map[class_id])
                        new_lines.append(' '.join(parts) + '\n')

            # Overwrite the file with only relevant labels
            with open(os.path.join(label_dir, filename), 'w') as f:
                f.writelines(new_lines)
