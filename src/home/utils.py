# utils.py

def predict_label(layout_xml_paths, category=None, memory_points=None, get_real_label=False):
    if isinstance(layout_xml_paths, list):
        label_list = []
        for path in layout_xml_paths:
            try:
                # Perform XML processing or prediction logic here
                label = process_single_xml(path, category, memory_points, get_real_label)
                label_list.append(label)
            except Exception as e:
                label_list.append(None)
                print(f"Error processing {path}: {str(e)}")
        if get_real_label:
            return label_list
        else:
            first_label = next((label for label in label_list if label is not None), None)
            return [first_label] * len(label_list)
    else:
        try:
            # Process single XML file
            label = process_single_xml(layout_xml_paths, category, memory_points, get_real_label)
            return [label]
        except Exception as e:
            print(f"Error processing {layout_xml_paths}: {str(e)}")
            return [None]

def process_single_xml(xml_path, category=None, memory_points=None, get_real_label=False):
    # Placeholder function for processing XML files or paths
    # Example logic, replace with your actual processing code
    if get_real_label:
        return f"RealLabel_{xml_path}"
    else:
        return f"PredictedLabel_{xml_path}"
