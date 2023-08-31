
# Define a dictionary to map the original substrings to their corresponding replacements
replacement_dict = {
    'allframes.meanshifts': 'rec.chemicalshifts',
    'clus0.meanshifts': 'clus0.shifts',
    'clus1.meanshifts': 'clus1.shifts',
    'clus2.meanshifts': 'clus2.shifts',
    'clus3.meanshifts': 'clus3.shifts',
    'clus4.meanshifts': 'clus4.shifts',
    'clus5.meanshifts': 'clus5.shifts',
    'clus6.meanshifts': 'clus6.shifts',
    'clus7.meanshifts': 'clus7.shifts',
    'clus8.meanshifts': 'clus8.shifts',
    'clus9.meanshifts': 'clus9.shifts'
}

def preprocess_dCScalc_file_names(input_str):
    """
    Preprocess the dCScalc_file names to make them consistent.

    Parameters:
    input_str (str): The original dCScalc_file name or any string that needs preprocessing.

    Returns:
    str: The preprocessed dCScalc_file name or string.
    """
    for original, replacement in replacement_dict.items():
        input_str = input_str.replace(original, replacement)
    return input_str
